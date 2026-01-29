import socket
import subprocess
import threading
import time
import requests

TOKEN = "8104816754:AAG8nn_4pPIH1PVO93ygkeSBbUhtsqxWvtM"
URL = f"https://api.telegram.org/bot{TOKEN}"

HOST = '0.0.0.0'
PORTA = 5000

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen(5)

print("Servidor ligado. Aguardando conexões...")

# ================= COMANDOS =================

def obter_arp():
    resultado = subprocess.check_output("arp -a", shell=True)
    return resultado.decode("cp850", errors="ignore")

def obter_ipconfig():
    resultado = subprocess.check_output("ipconfig", shell=True)
    return resultado.decode("cp850", errors="ignore")

def executar_ping(destino):
    comando = ["ping", destino, "-n", "4"]
    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        encoding="cp850"
    )
    return resultado.stdout

def processar_comando(mensagem):
    if mensagem == "arp":
        return obter_arp()

    elif mensagem == "ipconfig":
        return obter_ipconfig()

    elif mensagem.startswith("ping "):
        destino = mensagem.split(" ", 1)[1]
        return executar_ping(destino)

    else:
        return "Comandos: arp | ipconfig | ping <ip> | sair"

# ================= BOT TELEGRAM =================

def bot_telegram():
    ultimo_update = None

    while True:
        params = {"timeout": 10}
        if ultimo_update:
            params["offset"] = ultimo_update + 1

        r = requests.get(URL + "/getUpdates", params=params)
        updates = r.json().get("result", [])

        for update in updates:
            ultimo_update = update["update_id"]
            msg = update.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            texto = msg.get("text", "").strip().lower()

            if not chat_id or not texto:
                continue

            if texto == "/start":
                resposta = (
                    "Bot conectado ao servidor.\n\n"
                    "Comandos:\n"
                    "arp\nipconfig\nping <ip>"
                )
            else:
                resposta = processar_comando(texto)

            requests.post(
                URL + "/sendMessage",
                data={"chat_id": chat_id, "text": resposta[:4000]}
            )

        time.sleep(1)

# 🔹 Inicia o bot
threading.Thread(target=bot_telegram, daemon=True).start()

# ================= SERVIDOR SOCKET =================

while True:
    conexao, endereco = servidor.accept()
    print(f"\nCliente conectado: {endereco}")

    while True:
        dados = conexao.recv(1024)

        if not dados:
            print("Cliente desconectou.")
            break

        mensagem = dados.decode().strip().lower()
        print("Cliente:", mensagem)

        if mensagem == "sair":
            conexao.send("Conexão encerrada.".encode())
            break

        resposta = processar_comando(mensagem)
        conexao.send(resposta.encode())

    conexao.close()
    print("Aguardando novo cliente...")
