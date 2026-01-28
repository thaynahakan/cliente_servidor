import socket
import subprocess

#HOST = '127.0.0.1' # mesmo PC
#HOST = '192.168.0.112'  # IP do servidor na rede local
HOST = '0.0.0.0'
PORTA = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen(5)

print(" Servidor ligado. Aguardando conexões...")

def obter_arp():
    try:
        resultado = subprocess.check_output("arp -a", shell=True)
        return resultado.decode("cp850", errors="ignore")
    except Exception as e:
        return f"Erro ao obter ARP: {e}"

while True:  #  servidor nunca para
    conexao, endereco = servidor.accept()
    print(f"\n🔗 Novo cliente conectado: {endereco}")

    while True:  #  conversa com o cliente
        try:
            dados = conexao.recv(1024)

            if not dados:
                print("❌ Cliente desconectou.")
                break

            mensagem = dados.decode().strip().lower()
            print("📩 Cliente:", mensagem)

            if mensagem == "arp":
                resposta = obter_arp()

            elif mensagem == "sair":
                print(" Cliente saiu.")
                conexao.send("Conexão encerrada.".encode())
                break   # sai só da conversa, não do servidor

            else:
                resposta = "Comando inválido. Use: arp ou sair."

            conexao.send(resposta.encode())

        except Exception as erro:
            print(" Erro com cliente:", erro)
            break

    conexao.close()
    print(" Aguardando novo cliente...")

# servidor.close()  # só se você quiser desligar o servidor manualmente
