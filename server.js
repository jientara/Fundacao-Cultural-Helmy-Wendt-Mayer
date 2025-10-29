const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const path = require('path');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: true }));

// Serve static files from the root directory
app.use(express.static(path.join(__dirname)));

app.post('/feedback', (req, res) => {
    const { nome, email, mensagem } = req.body;
    const feedbackData = `Nome: ${nome}
Email: ${email}
Mensagem: ${mensagem}
------------------
`;

    fs.appendFile('feedback.txt', feedbackData, (err) => {
        if (err) {
            console.error(err);
            return res.status(500).send('Ocorreu um erro ao salvar o feedback.');
        }
        console.log('Feedback recebido e salvo com sucesso!');
        res.send('Feedback recebido com sucesso!');
    });
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
