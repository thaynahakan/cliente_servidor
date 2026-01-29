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

flowchart TB
    A[Início do Sistema]

    subgraph Servidor
        B[Servidor Python]
        C[Socket TCP :5000]
        D[Bot Telegram]
        E[processar_comando]
    end

    subgraph Entradas
        F[Cliente TCP]
        G[Usuário Telegram]
    end

    subgraph Comandos
        H[arp -a]
        I[ipconfig]
        J[ping &lt;ip&gt;]
    end

    subgraph Saídas
        K[Resposta em Texto]
        L[Terminal do Cliente]
        M[Chat do Telegram]
    end

    A --> B
    B --> C
    B --> D

    F --> C
    G --> D

    C --> E
    D --> E

    E --> H
    E --> I
    E --> J

    H --> K
    I --> K
    J --> K

    K --> L
    K --> M
