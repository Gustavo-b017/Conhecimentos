---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/baixa
  - status/3_incubadora
---

### Cyber_Engenharia_Social_Hoax

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Hoax (Boato) é uma categoria de engenharia social focada em espalhar mensagens fraudulentas ou falsos alarmes — sem carregar código malicioso técnico — com o único intuito de gerar confusão, pânico e desperdício de tempo e recursos entre os usuários.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ocorre de forma analógica em mensagens em cadeia (WhatsApp, E-mail). Geralmente alerta a vítima sobre um vírus incurável ("Não abra o e-mail X, ele vai derreter seu HD") ou faz falsas exigências de caridade. Pede expressamente que a mensagem seja repassada a todos os contatos.
*   **O Problema que Causa:** O ataque causa sobrecarga operacional (Negação de Serviço Humana). A equipe do SOC e o Helpdesk de TI perdem centenas de horas atendendo ligações de funcionários em pânico com um "vírus letal" que sequer existe, enquanto uma invasão real pode estar acontecendo de forma silenciosa por trás das cortinas.
*   **Visão Sênior (Vulnerabilidades/Escala):** Embora subestimado por técnicos puristas por não ter código embutido, o Hoax explora a confiança. Em um formato mais perigoso (Scam/Phishing manual), o boato finge ser um aviso da TI dizendo: "Seu sistema está infectado. Exclua a pasta System32 imediatamente para se salvar". O próprio usuário destrói a máquina obedecendo a uma ordem falsa.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O Hoax é **o garoto puxando o alarme de incêndio da escola no meio da prova de matemática**. Não existe fogo real. Não há combustível ou ameaça térmica. Mas a ação sociológica gerada pela farsa causa a evacuação do prédio, a interrupção das operações de ensino e o deslocamento inútil dos bombeiros.

#### 4. Pragmatismo Aplicado (Código e Implementação)
*(Sendo um ataque estritamente sociológico em formato de texto não executável, não há código malicioso para mitigar no prompt). A contenção ocorre no nível de Educação Corporativa (Security Awareness) e bloqueio de palavras-chave no Gateway de E-mail.*
```text
# Exemplo clássico da anatomia do texto de um Hoax:
ASSUNTO: [URGENTE] NOVO VÍRUS DESTRUIDOR DETECTADO
Por favor, envie isso a TODOS OS SEUS CONTATOS.
Se você receber uma mensagem chamada "Dança do Urso", NÃO ABRA. É um vírus que apaga todas as senhas do banco e não é detectado por antivírus nenhum! A Microsoft confirmou! Repasse urgente!
````

5. História do Conteúdo

Existem desde o nascimento da internet discada, operando nas antigas listas de e-mails da AOL e fóruns Usenet. Antes da internet, os hoaxes existiam na forma de "Correntes de Cartas" enviadas pelo correio físico (prometendo sorte ou maldição financeira).