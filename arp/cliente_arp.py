import socket


HOST = '192.168.0.112'  #para escutar em todas as interfaces
#HOST = '127.0.0.1'   # mesmo PC
PORTA = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORTA))

print(" Conectado ao servidor!")
print("Digite 'arp' para ver IPs e MACs.")
print("Digite 'sair' para encerrar.\n")

while True:
    try:
        mensagem = input("Quer solicitar o arp? ").strip()

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
        print("------------------------")
        print(resposta.decode(errors="ignore"))

    except ConnectionResetError:
        print(" Conexão perdida com o servidor.")
        break

    except Exception as erro:
        print(f" Ocorreu um erro: {erro}")
        break

cliente.close()
print(" Finalizou o fluxo.")
