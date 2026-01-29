import socket


HOST = '192.168.0.112'  #para escutar em todas as interfaces
#HOST = '127.0.0.1'   # mesmo PC
PORTA = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORTA))

print(" Conectado ao servidor!")
print("Comandos: arp | ipconfig | ping <ip> | sair")

while True:
    try:
        mensagem = input("O que você deseja solicitar? arp | ipconfig | ping <ip> | sair ").strip()

        if not mensagem:
            continue

        if mensagem.lower() == "sair":
            print("Desconectando do servidor...")
            cliente.send("sair".encode())
            break

        cliente.send(mensagem.encode())

        resposta = cliente.recv(65535)

        if not resposta:
            print("Servidor encerrou a conexão.")
            break

        print("\n Resposta do servidor:")
        print(resposta.decode(errors="ignore"))

    except ConnectionResetError:
        print(" Conexão perdida com o servidor.")
        break

    except Exception as erro:
        print(f" Ocorreu um erro: {erro}")
        break

cliente.close()
print(" Finalizou o fluxo.")
