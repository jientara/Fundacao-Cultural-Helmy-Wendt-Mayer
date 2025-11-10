import os
import json
import psycopg2
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        print("Requisição POST recebida")
        try:
            DATABASE_URL = os.environ.get('DATABASE_URL')
            if not DATABASE_URL:
                raise Exception("DATABASE_URL não configurada no Vercel")
            
            print(f"Conectando ao banco... (URL: {DATABASE_URL[:30]}...)")
            # Adicionar SSL para Supabase
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            cursor = conn.cursor()
            print("Conexão estabelecida!")
            
            # Criar tabela se não existir
            print("Verificando tabela...")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS feedback (
                    id SERIAL PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    mensagem TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            print("Tabela OK!")
            
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            print(f"Body raw: {body}")
            
            params = parse_qs(body)
            print(f"Params parsed: {params}")
            
            nome = params.get('nome', [''])[0]
            email = params.get('email', [''])[0]
            mensagem = params.get('mensagem', [''])[0]
            
            print(f"Nome: '{nome}', Email: '{email}', Mensagem: '{mensagem}'")
            
            if not nome or not email or not mensagem:
                raise Exception(f"Dados vazios - nome: {bool(nome)}, email: {bool(email)}, mensagem: {bool(mensagem)}")
            
            cursor.execute(
                "INSERT INTO feedback (nome, email, mensagem) VALUES (%s, %s, %s) RETURNING id",
                (nome, email, mensagem)
            )
            
            inserted_id = cursor.fetchone()[0]
            print(f"Registro inserido com ID: {inserted_id}")
            
            conn.commit()
            
            # Verificar o registro inserido
            cursor.execute("SELECT nome, email, mensagem FROM feedback WHERE id = %s", (inserted_id,))
            registro = cursor.fetchone()
            print(f"Registro salvo: nome='{registro[0]}', email='{registro[1]}', mensagem='{registro[2]}'")
            
            cursor.execute("SELECT COUNT(*) FROM feedback")
            total = cursor.fetchone()[0]
            print(f"Total de registros: {total}")
            
            cursor.close()
            conn.close()
            print("Sucesso!")
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success', 'id': inserted_id}).encode())
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
