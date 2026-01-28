import socket

# Cria o socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP da máquina do servidor
# '' significa: qualquer interface de rede
HOST = '192.168.0.112'
PORTA = 5000

servidor.bind((HOST, PORTA))
servidor.listen(1)

print("✅ Servidor ligado. Aguardando conexão...")

conexao, endereco = servidor.accept()
print(f" Conectado com {endereco}")


while True:
    dados = conexao.recv(1024)

    if not dados:
        print(" Cliente desconectou.")
        break

    mensagem = dados.decode()
    print("Cliente:", mensagem)

    resposta = input(" Resposta do servidor: ")
    conexao.send(resposta.encode())

conexao.close()
servidor.close()