import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORTA = 5000            # Porta do servidor

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.connect((HOST, PORTA))

print("✅ Conectado ao servidor!")

while True:
    mensagem = input(" coloque sua mensagem de vitória: ")

    if mensagem.lower() == "sair":
        break

    cliente.send(mensagem.encode())
    resposta = cliente.recv(1024).decode()
    print(" Servidor:", resposta)

cliente.close()