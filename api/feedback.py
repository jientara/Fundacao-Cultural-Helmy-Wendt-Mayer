import os
import psycopg2
from urllib.parse import parse_qs

DATABASE_URL = os.environ.get('DATABASE_URL')

def handler(request):
    if request.method != 'POST':
        return {
            'statusCode': 405,
            'body': '{"status": "error", "message": "Method not allowed"}'
        }
    
    try:
        body = request.body.decode('utf-8')
        params = parse_qs(body)
        
        nome = params.get('nome', [''])[0]
        email = params.get('email', [''])[0]
        mensagem = params.get('mensagem', [''])[0]
        
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO feedback (nome, email, mensagem) VALUES (%s, %s, %s)",
            (nome, email, mensagem)
        )
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return {
            'statusCode': 200,
            'headers': {'Content-Type': 'application/json'},
            'body': '{"status": "success"}'
        }
    except Exception as e:
        print(f"Erro: {e}")
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': '{"status": "error", "message": "Erro interno"}'
        }
