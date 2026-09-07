# Cybersecurity Automation Toolkit

<p align="center">
  <img src="assets/banner.svg" alt="Cybersecurity Automation Toolkit">
</p>

<p align="center">
  <strong>Toolkit em Python para automação de tarefas básicas de cibersegurança.</strong>
</p>

---

## Sobre o Projeto

O **Cybersecurity Automation Toolkit** é um projeto educacional desenvolvido em Python com o objetivo de demonstrar como scripts podem ser utilizados para automatizar tarefas comuns relacionadas à segurança da informação.

O projeto reúne diferentes ferramentas em um único toolkit, permitindo realizar:

-  Identificação de portas TCP abertas
-  Cálculo e validação de hashes SHA-256
-  Análise básica de força de senhas
-  Análise de logs de autenticação
-  Execução das ferramentas através de um menu interativo

O projeto foi desenvolvido para **ambientes de laboratório e sistemas autorizados**.

---

## Objetivos

Este projeto foi desenvolvido para praticar:

- Python aplicado à cibersegurança
- Automação de tarefas de segurança
- Manipulação de arquivos
- Análise de logs
- Redes e sockets
- Criptografia e hashes
- Expressões regulares
- Argumentos de linha de comando
- Organização de projetos Python
- Git e GitHub

---

## Tecnologias Utilizadas

| Tecnologia | Utilização |
|---|---|
| Python 3 | Desenvolvimento dos scripts |
| Socket | Comunicação TCP e port scanning |
| Hashlib | Cálculo de SHA-256 |
| Argparse | Interface de linha de comando |
| Regex | Identificação de padrões em logs e senhas |
| Counter | Contagem de eventos e IPs |
| Subprocess | Integração dos módulos |
| Git | Controle de versão |
| GitHub | Hospedagem do projeto |

---

# Funcionalidades

## 1. TCP Port Scanner

Realiza uma verificação de portas TCP em um determinado host.

Exemplo:

```bash
python scripts/port_scanner.py 127.0.0.1 --start 1 --end 100