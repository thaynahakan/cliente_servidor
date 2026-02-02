import time
import requests
import subprocess

# ===================== CONFIGURAÇÕES =====================

#BOT_TOKEN = "8104816754:AAG8nn_4pPIH1PVO93ygkeSBbUhtsqxWvtM"
#GEMINI_TOKEN = "AIzaSyDBnek53ZKae1wlYQhLwgQmxLTaPIt_NPY"

TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

SERVICE = {
    "host": "generativelanguage.googleapis.com",
    "endpoint" : "/v1beta/openai/chat/completions",
    "token": GEMINI_TOKEN  
}

# ===================== GEMINI =====================

SERVICE = { 
             "host": "generativelanguage.googleapis.com",
             "endpoint" : "/v1beta/openai/chat/completions",
             "token": GEMINI_TOKEN  
          }

headers = {
    "Authorization": "",
    "Content-Type": "application/json"
   }

payload =  {   "model" : "gemini-2.5-flash", 
               "messages"   : [ 
                  {"role": "system", "content": "Você é um assistente."},
                  {"role": "user", "content": ""} ],
               "temperature": 0.7,
               "max_tokens" : 10000
   }

def get_results (data):
   try: 
      response = data["choices"][0]["message"]["content"].strip()
   except Exception as e:
      print ("Erro na resposta do modelo ", e)
      response = ""
   
   return response
         
def ask_service (str_prompt: str) -> str:
   try:
      headers ["Authorization"] = f'Bearer {SERVICE["token"]}'
      payload["messages"][1]["content"] = str_prompt

      req_envio = requests.post("https://"+ 
                               SERVICE["host"]+
                               SERVICE["endpoint"], 
                               headers=headers, json=payload)
      req_envio.raise_for_status()
      data = req_envio.json()
      return get_results(data)
   except Exception as e:
      return f"\nERRO: {e}..."


# ===================== TELEGRAM =====================

def send_message(chat_id, text):
    requests.post(
        TELEGRAM_URL + "/sendMessage",
        json={"chat_id": chat_id, "text": text}
    )

def get_updates(update_id):
    response = requests.post(
        TELEGRAM_URL + "/getUpdates",
        json={"offset": update_id + 1}
    )
    return response.json()

# ===================== COMANDOS =====================

def get_routes():
    try:
        return subprocess.check_output("netstat -r", shell=True, text=True)
    except Exception:
        return "Erro ao obter tabela de rotas."

def get_ipv4():
    try:
        return subprocess.check_output("ipconfig", shell=True, text=True)
    except Exception:
        return "Erro ao obter IPv4."

def ping_host(host):
    try:
        return subprocess.check_output(f"ping {host}", shell=True, text=True)
    except Exception:
        return f"Erro ao executar ping em {host}."

# ===================== PROCESSAMENTO =====================
def help_message(user_name):
    return (
        f"Olá, {user_name}! \n\n"
        "Eu sou um bot de serviços. Você pode usar os seguintes comandos:\n\n"
        "/askai pergunta  -> Pergunte algo à IA\n"
        "/routes          -> Exibe a tabela de rotas da máquina\n"
        "/ipv4            -> Mostra os endereços IPv4 da máquina\n"
        "/ping endereco   -> Executa ping para um endereço\n\n"
    )

def process_message(chat_id, user_name, text):

    if text.startswith("/start") or text.startswith("/help"):
        send_message(chat_id, help_message(user_name))
        return
    
    elif text.startswith("/askai"):
        pergunta = text.replace("/askai", "").strip()
        if pergunta:
            resposta = ask_service(pergunta)
        else:
            resposta = "Uso correto: /askai pergunta"
        send_message(chat_id, resposta)

    elif text == "/routes":
        send_message(chat_id, get_routes())

    elif text == "/ipv4":
        send_message(chat_id, get_ipv4())

    elif text.startswith("/ping"):
        endereco = text.replace("/ping", "").strip()
        if endereco:
            send_message(chat_id, ping_host(endereco))
        else:
            send_message(chat_id, "Uso correto: /ping endereco")

    else:
        send_message(chat_id, f"Olá, {user_name}! Comando não reconhecido.")

# ===================== LOOP PRINCIPAL =====================

def main():
    update_id = 0

    while True:
        data = get_updates(update_id)

        if data.get("ok"):
            for item in data["result"]:
                update_id = item["update_id"]

                message = item.get("message")
                if not message:
                    continue

                chat_id = message["chat"]["id"]
                user_name = message["from"].get("first_name", "Usuário")
                text = message.get("text", "")

                process_message(chat_id, user_name, text)

        time.sleep(2)

# ===================== START =====================

if __name__ == "__main__":
    main()