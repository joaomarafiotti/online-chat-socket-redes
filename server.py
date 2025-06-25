import threading
import socket

# Definição do IP e porta do servidor (localhost = 127.0.0.1)
host = "127.0.0.1"
port = 5555  # Porta escolhida para conexões

# Cria o socket TCP do servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))  # Associa o IP e porta ao servidor
server.listen()  # Coloca o servidor em modo de escuta

# Listas para armazenar os clientes conectados e seus apelidos
clients = []
nicknames = []

# Função para enviar uma mensagem para todos os clientes conectados
def broadcast(message):
    for client in clients:
        client.send(message)

# Função para lidar com mensagens recebidas de um cliente específico
def handle(client):
    while True:
        try:
            msg = client.recv(1024)

            if msg.decode('utf-8').startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    nome_para_remover = msg.decode('utf-8')[5:]
                    kick_user(nome_para_remover)
                else:
                    client.send('Comando negado!'.encode('utf-8'))

            elif msg.decode('utf-8').startswith('BAN'):
                if nicknames[clients.index(client)] == 'admin':
                    nome_para_banir = msg.decode('utf-8')[4:]
                    kick_user(nome_para_banir)
                    with open('bans.txt', 'a') as f:
                        f.write(f'{nome_para_banir}\n')
                    print(f'{nome_para_banir} foi banido pelo administrador.')
                else:
                    client.send('Comando negado!'.encode('utf-8'))

            else:
                broadcast(msg)  # Envia a mensagem recebida para todos

        except socket.error:
            if client in clients:
                index = clients.index(client)
                clients.remove(client)
                client.close()
                apelido = nicknames[index]
                broadcast(f'{apelido} saiu do chat.'.encode('utf-8'))
                nicknames.remove(apelido)
                break

# Função principal que aceita novas conexões
def receive():
    while True:
        client, address = server.accept()
        print(f"Conectado com {str(address)}")

        client.send('NICK'.encode('utf-8'))  # Solicita o apelido do cliente
        nickname = client.recv(1024).decode('utf-8')

        with open('bans.txt', 'r') as f:
            bans = f.readlines()

        if nickname + '\n' in bans:
            client.send('BAN'.encode('utf-8'))
            client.close()
            continue

        if nickname == 'admin':
            client.send('PASS'.encode('utf-8'))
            password = client.recv(1024).decode('utf-8')
            if password != 'adminpass':
                client.send('ACESSO_NEGADO'.encode('utf-8'))
                client.close()
                continue

        nicknames.append(nickname)
        clients.append(client)

        print(f'O apelido do cliente é {nickname}')
        broadcast(f'{nickname} entrou no chat!'.encode('utf-8'))
        client.send('Conectado ao servidor!'.encode('utf-8'))

        # Cria uma thread para lidar com esse cliente
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Função para expulsar um cliente do chat
def kick_user(name):
    if name in nicknames:
        index = nicknames.index(name)
        client_to_kick = clients[index]
        clients.remove(client_to_kick)
        client_to_kick.send('Você foi expulso do chat!'.encode('utf-8'))
        client_to_kick.close()
        nicknames.remove(name)
        broadcast(f'{name} foi expulso do chat.'.encode('utf-8'))

# Inicia o servidor
print('Servidor iniciado. Aguardando conexões...')
receive()