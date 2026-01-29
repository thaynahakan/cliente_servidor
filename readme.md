# Projeto de Estudo – Bot Telegram com Arquitetura Cliente/Servidor

Este projeto tem como objetivo estudar a comunicação cliente/servidor em Python,
integrada a um bot do Telegram, permitindo a execução remota de comandos de rede
no sistema operacional.

---

## 🚀 Como Rodar o Projeto

1. Inicie o servidor:
```bash
python servidor.py

Em outro terminal (ou outro computador da rede), inicie o cliente:

python cliente.py
```

(Opcional) Inicie o bot no Telegram após configurar o TOKEN.

🧪 Comandos Disponíveis

No cliente TCP ou no Telegram:

arp → Exibe a tabela ARP

ipconfig → Exibe as configurações de rede

ping <ip ou domínio> → Testa conectividade

sair → Encerra a conexão do cliente TCP

Exemplos:
```bash
arp
ipconfig
ping 8.8.8.8
ping google.com
```

🧩 Tecnologias Utilizadas

socket → Comunicação entre cliente e servidor

subprocess → Execução de comandos do sistema operacional

threading → Execução paralela (Servidor + Bot Telegram)

time → Controle de pausas e intervalos

requests → Comunicação com a API do Telegram

flowchart TD
    A[Início do Sistema] --> B[Servidor Python]
    B --> C[Cria Socket TCP :5000]
    B --> D[Inicia Bot Telegram em Thread]

    C --> E[Aguardando Cliente TCP]
    D --> F[Aguardando Mensagens Telegram]

    E --> G[Recebe Comando]
    F --> G

    G --> H{processar_comando}

    H -->|arp| I[Executa arp -a]
    H -->|ipconfig| J[Executa ipconfig]
    H -->|ping ip| K[Executa ping <ip>]

    I --> L[Resposta em Texto]
    J --> L
    K --> L

    L --> M[Envia Resposta ao Cliente TCP]
    L --> N[Envia Resposta ao Telegram]

    M --> E
    N --> F