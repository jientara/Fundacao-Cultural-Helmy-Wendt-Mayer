# Fundação Cultural Helmy Wendt Mayer - Site Institucional

## 📋 Sobre o Projeto
Site institucional da Fundação Cultural Helmy Wendt Mayer de Canoinhas/SC, apresentando informações sobre o Museu, Biblioteca e Arquivo Histórico.

## 🛠️ Tecnologias Utilizadas

### Frontend
- **HTML5**: Estrutura das páginas
- **CSS3**: Estilização e responsividade
- **JavaScript**: Interatividade e comunicação com a API

### Backend
- **Python 3**: Linguagem de programação da API
- **psycopg2**: Biblioteca para conexão com PostgreSQL
- **Vercel Serverless Functions**: Hospedagem da API

### Banco de Dados
- **Supabase (PostgreSQL)**: Armazenamento dos feedbacks

### Hospedagem
- **Vercel**: Deploy automático via GitHub

## 📁 Estrutura do Projeto

```
├── api/
│   └── feedback.py          # API serverless para processar feedbacks
├── public/
│   ├── CSS/
│   │   └── style.css        # Estilos do site
│   ├── Imagens/             # Imagens e ícones
│   ├── index.html           # Página inicial
│   ├── museu.html           # Página do museu
│   ├── biblioteca.html      # Página da biblioteca
│   └── arquivo.html         # Página do arquivo histórico
├── requirements.txt         # Dependências Python
├── vercel.json             # Configuração do Vercel
└── README.md               # Este arquivo
```

## 🔄 Fluxo de Funcionamento do Sistema de Feedback

### 1. Frontend (index.html)
- Usuário preenche o formulário com nome, email e mensagem
- JavaScript captura o evento de submit
- Dados são convertidos para formato URL-encoded
- Requisição POST é enviada para `/api/feedback`

### 2. API (api/feedback.py)
- Recebe a requisição POST
- Conecta ao banco de dados Supabase via PostgreSQL
- Cria a tabela `feedback` se não existir
- Valida os dados recebidos
- Insere o feedback no banco de dados
- Retorna resposta JSON com status de sucesso ou erro

### 3. Banco de Dados (Supabase)
- Armazena os feedbacks na tabela `feedback`
- Estrutura da tabela:
  - `id`: Identificador único (auto-incremento)
  - `nome`: Nome do usuário
  - `email`: Email do usuário
  - `mensagem`: Mensagem do feedback
  - `created_at`: Data e hora do registro

## 🔐 Variáveis de Ambiente

Para o funcionamento correto, é necessário configurar no Vercel:

- `DATABASE_URL`: String de conexão com o Supabase
  - Formato: `postgresql://postgres.[PROJECT-REF]:[PASSWORD]@[HOST].pooler.supabase.com:6543/postgres`

## 🚀 Como Visualizar os Feedbacks

### Opção 1: Supabase Dashboard
1. Acesse [supabase.com](https://supabase.com)
2. Entre no projeto
3. Clique em "Table Editor"
4. Selecione a tabela "feedback"

### Opção 2: SQL Editor
1. No Supabase, vá em "SQL Editor"
2. Execute: `SELECT * FROM feedback ORDER BY created_at DESC;`

## 📦 Deploy

O site está configurado para deploy automático:
1. Push para o repositório GitHub
2. Vercel detecta as mudanças
3. Build e deploy automático
4. Site atualizado em produção

## 🔗 Links Úteis

- **Site em Produção**: [Inserir URL do Vercel]
- **Repositório GitHub**: [Inserir URL do GitHub]
- **Supabase Dashboard**: [Inserir URL do projeto Supabase]

## 👨‍💻 Desenvolvimento

Para rodar localmente:
1. Clone o repositório
2. Configure as variáveis de ambiente
3. Instale as dependências: `pip install -r requirements.txt`
4. Use o Vercel CLI para testar: `vercel dev`

## 📝 Observações Técnicas

- A API usa SSL obrigatório (`sslmode='require'`) para conexão segura com o Supabase
- O formulário envia dados em formato `application/x-www-form-urlencoded`
- CORS está habilitado para permitir requisições do frontend
- A tabela é criada automaticamente na primeira execução
- Validação de campos obrigatórios no backend
