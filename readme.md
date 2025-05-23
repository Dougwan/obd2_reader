---
# Emulador de Diagnóstico Veicular Simplificado

Este projeto tem como objetivo principal estabelecer a comunicação com um emulador ELM327 para monitorar dados básicos de um veículo, como rotação do motor (RPM), velocidade e consumo de combustível, utilizando Python. É um ponto de partida simples para quem deseja explorar o diagnóstico veicular sem a complexidade de um sistema de nível industrial.
---

## 🚀 Primeiros Passos

Siga estas instruções para configurar e rodar o projeto em seu ambiente local.

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em sua máquina.

### Configuração do Ambiente

É **altamente recomendável** usar um ambiente virtual para isolar as dependências do projeto.

1.  **Crie um ambiente virtual:**

    ```bash
    python3 -m venv venv
    ```

2.  **Ative o ambiente virtual:**

    - **No macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```
    - **No Windows (Command Prompt):**
      ```bash
      venv\Scripts\activate.bat
      ```
    - **No Windows (PowerShell):**
      `powershell
    .\venv\Scripts\Activate.ps1
    `
      Você saberá que o ambiente está ativo quando `(venv)` aparecer no início da linha de comando do seu terminal.

3.  **Instale as dependências:**

    Instale as dependências do projeto rodando `pip instal -r requirements.txt` na raiz do seu projeto.

---

## 🛠️ Como Usar

### 1. Iniciar o Emulador ELM327

Abra um **novo terminal** e, **com o ambiente virtual ativo**, inicie o emulador:

```bash
python -m elm
```

O emulador iniciará e informará qual porta serial virtual ele está utilizando (ex: `COM3` no Windows, ou `/dev/ttyUSB0` no Linux/macOS). **Anote essa porta**, pois você precisará dela no seu código Python.

### 2. Rodar o Código de Monitoramento Python

O código Python `main.py` se conectará ao emulador e lerá os dados.

1.  **Copie o `.env.example` para `.env`**:
    Substitua o valor de `OBD2_SERIAL_PORT` pela porta serial que o `ELM327-emulator` informou quando foi iniciado (ex: `'COM3'`, `'/dev/ttyUSB0'`).

    Substituia o valor de `OBD2_SERIAL_BAUDRATE` pelo baudrate da sua porta serial.

2.  **Abra um segundo terminal** (diferente do anterior que está rodando o emulador) e, **com o ambiente virtual ativo**, execute o script de monitoramento:

    ```bash
        python monitor_carro.py
    ```

Seu script Python deverá se conectar ao emulador, enviar os comandos ELM327 para ler os PIDs configurados e exibir os valores simulados para RPM, velocidade e consumo, além de calcular médias durante o período de leitura.

---

## 📄 Estrutura do Projeto

```
.
├── config/
│   └── settings.py           # Configurações do projeto, como porta serial e baudrate, utilizando dotenv para variáveis de ambiente.
├── obd2/
│   ├── interface.py        # Interface de comunicação com o dispositivo ELM327 via porta serial (envio e leitura de comandos).
│   ├── pids.py             # Definições de PIDs OBD2 com fórmulas de interpretação dos dados brutos.
│   └── at_commands.py      # Definições de comandos AT utilizados na inicialização da interface.
├── .env.example            # Arquivo de exemplo para configuração das variáveis de ambiente.
├── main.py                 # Script principal que inicializa a conexão com o ELM327 e executa a leitura dos dados OBD2.
├── requirements.txt        # Lista de dependências do projeto (ex: pyserial, python-dotenv).
└── README.md               # Documentação do projeto com instruções de uso, estrutura e exemplos.
```

---

## 💡 Próximos Passos (Ideias para Melhoria)

- **Visualização de Dados:** Integrar bibliotecas como `matplotlib` ou `Tkinter` para criar gráficos ou uma interface de usuário mais visual.
- **Armazenamento de Dados:** Salvar os dados lidos em um arquivo CSV, banco de dados SQLite, ou similar para análise posterior.
- **Outros PIDs:** Explorar e implementar a leitura de outros PIDs OBD-II relevantes.
- **Tratamento de Erros:** Adicionar tratamento de erros mais robusto.

---
