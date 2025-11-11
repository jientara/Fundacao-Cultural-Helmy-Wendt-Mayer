# Fundação Cultural Helmy Wendt Mayer - Site Institucional

##  Sobre o Projeto
Site institucional da Fundação Cultural Helmy Wendt Mayer de Canoinhas/SC, apresentando informações sobre o Museu, Biblioteca e Arquivo Histórico.

** Site:** https://fchwm.vercel.app

##  Tecnologias Utilizadas

### Frontend
- **HTML5**: Estrutura semântica das páginas
- **CSS3**: Estilização responsiva e moderna
- **JavaScript**: Interatividade e comunicação com API
- **CSS Crítico Inline**: Otimização de performance

### Backend
- **Python 3**: Linguagem da API
- **psycopg2**: Conexão com PostgreSQL
- **Vercel Serverless Functions**: Hospedagem da API

### Banco de Dados
- **Supabase (PostgreSQL)**: Armazenamento de feedbacks

### Hospedagem & Deploy
- **Vercel**: Deploy automático via GitHub
- **GitHub**: Controle de versão

##  Estrutura do Projeto

```
├── api/
│   └── feedback.py          # API serverless para feedbacks
├── public/
│   ├── CSS/
│   │   └── style.css        # Estilos do site
│   ├── Imagens/             # Imagens e ícones
│   ├── index.html           # Página inicial
│   ├── museu.html           # Página do museu
│   ├── biblioteca.html      # Página da biblioteca
│   ├── arquivo.html         # Página do arquivo
│   ├── manifest.json        # PWA manifest
│   ├── robots.txt           # SEO
│   └── sitemap.xml          # SEO
├── requirements.txt         # Dependências Python
├── vercel.json             # Configuração Vercel
└── README.md               # Documentação
```

##  Fluxo de Funcionamento do Sistema de Feedback

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

##  Variáveis de Ambiente

Para o funcionamento correto, é necessário configurar no Vercel:

- `DATABASE_URL`: String de conexão com o Supabase
  - Formato: `postgresql://postgres.[PROJECT-REF]:[PASSWORD]@[HOST].pooler.supabase.com:6543/postgres`

##  Como Visualizar os Feedbacks

### Opção 1: Supabase Dashboard
1. Acesse [supabase.com](https://supabase.com)
2. Entre no projeto
3. Clique em "Table Editor"
4. Selecione a tabela "feedback"

### Opção 2: SQL Editor
1. No Supabase, vá em "SQL Editor"
2. Execute: `SELECT * FROM feedback ORDER BY created_at DESC;`

##  Deploy

O site está configurado para deploy automático:
1. Push para o repositório GitHub
2. Vercel detecta as mudanças
3. Build e deploy automático
4. Site atualizado em produção

##  Otimizações Implementadas

### Performance
-  CSS crítico inline
-  Preconnect para fontes e recursos externos
-  Preload de recursos críticos
-  Headers de cache otimizados
-  Lazy loading de iframe (Google Maps)
-  Min-height para evitar CLS

### SEO
-  Meta tags completas em todas as páginas
-  Dados estruturados JSON-LD
-  robots.txt e sitemap.xml
-  Meta descriptions únicas
-  Open Graph tags

### Acessibilidade
-  ARIA labels e roles
-  Skip links
-  Alt text descritivo
-  Estrutura HTML5 semântica
-  Contraste adequado

### Segurança
-  rel="noopener noreferrer" em links externos
-  SSL obrigatório no banco de dados
-  Validação de dados no backend

### PWA
-  manifest.json
-  theme-color
-  Favicon

##  Resultados

- **SEO**: 100/100
- **Acessibilidade**: 100/100
- **Melhores Práticas**: 100/100
- **Performance**: Otimizada

##  Desenvolvimento Local

```bash
# Clone o repositório
git clone [URL_DO_REPOSITORIO]

# Instale as dependências Python
pip install -r requirements.txt

# Configure a variável de ambiente
# Crie arquivo .env com:
DATABASE_URL=postgresql://...

# Rode localmente com Vercel CLI
npm i -g vercel
vercel dev
```

##  Observações Técnicas

- API usa SSL obrigatório para conexão segura
- Formulário envia dados em formato URL-encoded
- CORS habilitado para requisições do frontend
- Tabela criada automaticamente na primeira execução
- Validação de campos no backend
- Cache configurado para assets estáticos
- Fontes carregadas de forma assíncrona

##  Próximos Passos

- [ ] Otimizar imagens (reduzir de 3.3MB para ~500KB)
- [ ] Implementar Service Worker para PWA completo
- [ ] Adicionar página de administração de feedbacks
- [ ] Implementar sistema de busca no acervo

##  Contato

**Fundação Cultural Helmy Wendt Mayer**
-  (47) 3622-0609
-  Rua Vidal Ramos, 632 - Centro, Canoinhas/SC
-  https://fchwm.vercel.app
