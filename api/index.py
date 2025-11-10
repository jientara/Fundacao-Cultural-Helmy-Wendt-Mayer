import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

DATABASE_URL = os.environ.get('DATABASE_URL')

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id SERIAL PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            mensagem TEXT NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/api/feedback', methods=['POST'])
@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cursor = conn.cursor()

        nome = request.form['nome']
        email = request.form['email']
        mensagem = request.form['mensagem']
        
        cursor.execute("INSERT INTO feedback (nome, email, mensagem) VALUES (%s, %s, %s)", (nome, email, mensagem))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({'status': 'success'})
    except Exception as e:
        # Log do erro para depuração no servidor (Vercel logs)
        print(f"Erro no banco de dados: {e}")
        # Retorna uma resposta de erro em JSON
        return jsonify({'status': 'error', 'message': 'Erro interno do servidor'}), 500
