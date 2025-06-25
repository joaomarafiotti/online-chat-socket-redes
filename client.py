import socket
import threading
import json
import os

# Função para entrar em um servidor existente salvo em servers.json
def entrar_no_servidor():
    os.system('cls||clear')
    with open('servers.json') as f:
        data = json.load(f)
    print('Servidores disponíveis: ', end="")
    for servidor in data:
        print(servidor, end=" ")
    
    nome_servidor = input("\nDigite o nome do servidor para entrar: ")
    global nickname
    global password
    nickname = input("Escolha seu apelido: ")
    if nickname == 'admin':
        password = input("Digite a senha do administrador: ")

    ip = data[nome_servidor]["ip"]
    port = data[nome_servidor]["port"]
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))

# Função para adicionar um novo servidor no arquivo servers.json
def adicionar_servidor():
    os.system('cls||clear')
    nome = input("Digite um nome para o servidor: ")
    ip = input("Digite o endereço IP do servidor: ")
    porta = int(input("Digite a porta do servidor: "))

    with open('servers.json', 'r') as f:
        data = json.load(f)
    with open('servers.json', 'w') as f:
        data[nome] = {"ip": ip, "port": porta}
        json.dump(data, f, indent=4)

# Menu principal: permite escolher entre entrar ou adicionar servidor
while True:
    os.system('cls||clear')
    opcao = input("(1) Entrar em servidor\n(2) Adicionar servidor\n")
    if opcao == '1':
        entrar_no_servidor()
        break
    elif opcao == '2':
        adicionar_servidor()

stop_thread = False

# Função que escuta mensagens vindas do servidor
def receber():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            mensagem = client.recv(1024).decode('utf-8')
            if mensagem == 'NICK':
                client.send(nickname.encode('utf-8'))
                proxima_mensagem = client.recv(1024).decode('utf-8')
                if proxima_mensagem == 'PASS':
                    client.send(password.encode('utf-8'))
                    if client.recv(1024).decode('utf-8') == 'ACESSO_NEGADO':
                        print("Acesso negado! Senha incorreta.")
                        stop_thread = True
                elif proxima_mensagem == 'BAN':
                    print('Você foi banido e não pode entrar.')
                    client.close()
                    stop_thread = True
            else:
                print(mensagem)
        except socket.error:
            print('Erro de conexão com o servidor.')
            client.close()
            break

# Função que envia mensagens para o servidor
def escrever():
    while True:
        if stop_thread:
            break
        mensagem = f'{nickname}: {input("")}'
        if mensagem[len(nickname) + 2:].startswith('/'):
            if nickname == 'admin':
                if mensagem[len(nickname) + 2:].startswith('/kick'):
                    client.send(f'KICK {mensagem[len(nickname) + 2 + 6:]}'.encode('utf-8'))
                elif mensagem[len(nickname) + 2:].startswith('/ban'):
                    client.send(f'BAN {mensagem[len(nickname) + 2 + 5:]}'.encode('utf-8'))
            else:
                print("Apenas o administrador pode usar comandos!")
        else:
            client.send(mensagem.encode('utf-8'))

# Inicia as duas threads: uma para receber e outra para enviar mensagens
thread_receber = threading.Thread(target=receber)
thread_receber.start()
thread_escrever = threading.Thread(target=escrever)
thread_escrever.start()
