# API Serverless para receber feedbacks e armazenar no Supabase (PostgreSQL)
import os
import json
import psycopg2
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            # Conectar ao banco de dados Supabase
            DATABASE_URL = os.environ.get('DATABASE_URL')
            if not DATABASE_URL:
                raise Exception("DATABASE_URL não configurada")
            
            conn = psycopg2.connect(DATABASE_URL, sslmode='require')
            cursor = conn.cursor()
            
            # Criar tabela se não existir
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
            
            # Ler e parsear dados do formulário
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(body)
            
            nome = params.get('nome', [''])[0]
            email = params.get('email', [''])[0]
            mensagem = params.get('mensagem', [''])[0]
            
            if not nome or not email or not mensagem:
                raise Exception("Todos os campos são obrigatórios")
            
            # Inserir feedback no banco
            cursor.execute(
                "INSERT INTO feedback (nome, email, mensagem) VALUES (%s, %s, %s) RETURNING id",
                (nome, email, mensagem)
            )
            
            inserted_id = cursor.fetchone()[0]
            conn.commit()
            cursor.close()
            conn.close()
            
            # Retornar sucesso
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success', 'id': inserted_id}).encode())
            
        except Exception as e:
            print(f"ERRO: {str(e)}")
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
