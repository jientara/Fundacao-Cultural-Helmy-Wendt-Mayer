import os
import json
import psycopg2
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("Requisição POST recebida")
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            print(f"Content-Length: {content_length}")
            
            body = self.rfile.read(content_length).decode('utf-8')
            print(f"Body recebido: {body}")
            
            params = parse_qs(body)
            print(f"Params parseados: {params}")
            
            nome = params.get('nome', [''])[0]
            email = params.get('email', [''])[0]
            mensagem = params.get('mensagem', [''])[0]
            
            print(f"Dados: nome={nome}, email={email}")
            
            DATABASE_URL = os.environ.get('DATABASE_URL')
            if not DATABASE_URL:
                raise Exception("DATABASE_URL não configurada")
            
            print("Conectando ao banco...")
            conn = psycopg2.connect(DATABASE_URL)
            cursor = conn.cursor()
            
            print("Inserindo dados...")
            cursor.execute(
                "INSERT INTO feedback (nome, email, mensagem) VALUES (%s, %s, %s)",
                (nome, email, mensagem)
            )
            
            conn.commit()
            cursor.close()
            conn.close()
            print("Sucesso!")
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success'}).encode())
        except Exception as e:
            print(f"ERRO: {type(e).__name__}: {str(e)}")
            import traceback
            traceback.print_exc()
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'error', 'message': str(e)}).encode())
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
