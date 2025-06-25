# 💬 Online Chat Socket Redes (Chat-On TCP - Adaptado)

Este projeto implementa um sistema de **chat em tempo real** utilizando **sockets TCP** com a linguagem **Python**. O sistema permite que múltiplos clientes se conectem a um servidor central e troquem mensagens de forma síncrona via terminal. 

Usuários com o apelido `"admin"` possuem permissões especiais, podendo expulsar (`/kick`) ou banir (`/ban`) outros participantes da conversa.

---

## 🎓 Projeto da disciplina de Redes de Computadores

**Curso:** Engenharia de Software – IFSP  
**Disciplina:** Redes de Computadores 1  
**Ano:** 2025  
**Integrantes:**
- João Pedro Piccino Marafiotti  
- Mauricio Duarte

---

## 📄 Documentação

📘 O arquivo PDF completo com:
- Descrição da aplicação
- Explicação do funcionamento cliente/servidor
- Detalhamento da comunicação por sockets
- Manual de instalação e uso

Está disponível aqui no repositório com o nome:

👉 **`Trabalho Redes de Computadores - Joao e Mauricio.pdf`**

---

## 🎥 Demonstração em vídeo

📺 Assista ao vídeo com:
- Apresentação do PDF
- Explicação do manual do usuario
- Explicação do código-fonte
- Demonstração da execução
- Casos de uso reais com comandos `/kick` e `/ban`

🔗 [Clique aqui para assistir no YouTube](https://www.youtube.com/watch?v=lPhOWroEquQ)  
📹 **Título:** *Video Socket Redes de Computadores - Joao e Mauricio*

---

## 🚀 Como executar o sistema

### ✔️ Requisitos
- Python 3.8 ou superior

### 🖥️ 1. Iniciar o servidor
```bash
python Server.py
```

### 👤 2. Iniciar um cliente
```bash
python Client.py
```

### ✍️ 3. Instruções de uso
- Escolha um servidor salvo (ex: `localhost`)
- Digite um apelido
- Para permissões de admin, use apelido `admin` e senha `adminpass`
- Comandos disponíveis para admin:
  - `/kick nome` – expulsa um usuário
  - `/ban nome` – bane um usuário permanentemente

---

## 📂 Arquivos principais

| Arquivo         | Descrição                                   |
|-----------------|---------------------------------------------|
| `Server.py`     | Código do servidor TCP                      |
| `Client.py`     | Código do cliente com interface via terminal|
| `servers.json`  | Servidores salvos com IP e porta            |
| `bans.txt`      | Lista de apelidos banidos                   |
| `README.md`     | Este manual                                 |
| `Trabalho Redes de Computadores - Joao e Mauricio.pdf` | Documento completo da atividade |

---

## 🛠️ Base do Projeto

Este projeto foi adaptado e traduzido a partir de:  
🔗 https://github.com/IamLucif3r/Chat-On

Todos os créditos pelo código original pertencem ao autor.
