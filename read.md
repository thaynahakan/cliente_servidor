Projeto de estudo Pessoal de bot-telegram cliente/servidor

Como Rodar?

Abrir o servidor
python servidor.py

Abrir o cliente
python cliente.py

Testar comandos
arp
ipconfig
ping 8.8.8.8 ou google.com

socket	Comunicação entre cliente e servidor
subprocess	Executar comandos do sistema
threading	Rodar tarefas em paralelo
time	Controlar pausas e intervalos
requests	Falar com a API do Telegram

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
