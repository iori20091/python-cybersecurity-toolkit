# Cybersecurity Automation Toolkit — Test Report

## 1. Objetivo

Validar o funcionamento dos módulos desenvolvidos para o Cybersecurity Automation Toolkit.

O objetivo dos testes é verificar se cada ferramenta executa corretamente sua função dentro de um ambiente de laboratório local.

---

# 2. Ambiente

| Item | Informação |
|---|---|
| Sistema operacional | Windows |
| Linguagem | Python 3 |
| Ambiente | Laboratório local |
| Interface | PowerShell / VS Code |
| Virtual Environment | `.venv` |

---

# 3. Testes Realizados

### 3.1 TCP Port Scanner

Foi utilizado o endereço de loopback:

```text
127.0.0.1