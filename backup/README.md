# App de Entregas - Versão Frontend com Firebase

Este repositório contém uma versão front-end mínima que implementa autenticação (email/senha), CRUD de produtos e upload de imagens usando Firebase (Firestore + Storage). A ideia é hospedar estático (por exemplo, GitHub Pages).

Arquivos principais:
- `index.html` - página pública (já existente no projeto)
- `login.html` - página de login / registro
- `admin.html` - painel para adicionar/editar/excluir produtos
- `JS/app.js` - lógica cliente (Firebase v9 modular)
- `firebase-config.example.js` - exemplo de configuração do Firebase

Passo a passo para configurar e rodar localmente

1. Criar projeto no Firebase
   - Acesse https://console.firebase.google.com/ e crie um novo projeto.
   - No painel do projeto, clique em "Adicionar app" (Web) e copie as configurações (SDK config).

2. Criar arquivo de configuração local
   - Copie `firebase-config.example.js` para `firebase-config.js` na raiz do projeto.
   - Preencha as chaves com as informações do seu projeto Firebase.

3. Habilitar Firestore e Storage
   - No console do Firebase, ative Firestore (modo de teste para desenvolvimento) e Storage.
   - Regras iniciais (apenas para desenvolvimento):

Firestore (regras):
```
service cloud.firestore {
  match /databases/{database}/documents {
    match /{document=**} {
      allow read, write: if true; // temporário - só para dev
    }
  }
}
```

Storage (regras):
```
service firebase.storage {
  match /b/{bucket}/o {
    match /{allPaths=**} {
      allow read, write: if true; // temporário - só para dev
    }
  }
}
```

Atenção: essas regras deixam seu banco aberto. Ajuste antes de publicar.

4. Testar localmente
   - Você pode abrir os arquivos `.html` diretamente no navegador ou usar um servidor simples (recomendado):

Windows PowerShell:
```powershell
# se você tiver Python instalado
python -m http.server 8000; Start-Process http://localhost:8000
```

5. Publicar no GitHub Pages
   - Crie repositório no GitHub e faça push do projeto.
   - Nas configurações do repositório -> Pages, selecione a branch `main` e a pasta `/ (root)`.
   - Aguarde e acesse `https://<seu-usuario>.github.io/<seu-repo>`.

Notas e próximos passos
- Ajuste regras de segurança antes de publicar (restringir write para usuários autenticados).
- Se quiser mostrar localização de entregas no mapa, posso integrar Leaflet/Mapbox e salvar lat/lng junto ao produto/pedido.
- Posso também adicionar validação, paginação, e edição de produtos.

