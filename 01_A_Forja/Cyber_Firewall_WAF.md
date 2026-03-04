---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Firewall_WAF
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Web Application Firewall (WAF) é um filtro de perímetro hiperfocado e projetado especificamente para proteger aplicações web, monitorando, inspecionando e aniquilando tráfego HTTP/HTTPS malicioso.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente dos firewalls de rede que lidam com portas e IPs, o WAF atua exclusivamente na Camada 7 (Aplicação). Ele intercepta o tráfego HTTP antes de chegar ao servidor web, dissecando parâmetros, cabeçalhos, cookies e formulários em busca de padrões de ataques catalogados (como SQL Injection, Cross-Site Scripting - XSS, e ataques do [[Ferramenta_OWASP_ZAP|OWASP Top 10]]).
*   **O Problema que Resolve:** Firewalls como o [[Cyber_Firewall_NGFW]] não entendem a lógica de código de um site web. Se o invasor enviar um código SQL malicioso via porta 443 (HTTPS permitida), o NGFW deixa passar. O WAF entende a linguagem da web e barra o payload tóxico.
*   **Visão Sênior (Vulnerabilidades/Escala):** O WAF é um inferno operacional para ser calibrado. Em modo rígido, bloqueia usuários legítimos (falsos-positivos) e quebra aplicações de negócio. Em modo frouxo, torna-se inútil. Além disso, hackers seniores fazem *Bypass de WAF* codificando o ataque (ex: *Double URL Encoding* ou injeções fragmentadas) para que a assinatura do WAF não reconheça a ameaça.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se o firewall de rede é a polícia de fronteira, o [[Cyber_Firewall_WAF]] é o **Revisor de Código Postal** do correio. Ele não se importa de que caminhão a carta chegou (Camada 3) ou qual o tamanho da caixa (Camada 4). Ele só se importa com a carta escrita no idioma HTTP. Ele tira o papel do envelope, lê a frase e, se encontrar gírias de golpistas ou palavras codificadas pedindo a senha do banco do destinatário (SQL Injection), ele incinera a carta antes que o usuário final possa lê-la.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O *ModSecurity* é o WAF open-source mais famoso do mundo (frequentemente acoplado ao [[Ferramenta_Nginx|Nginx]]). Um exemplo de regra pragmática onde o WAF bloqueia qualquer requisição HTTP que tente injetar o comando clássico `1=1` (usado para explodir bancos de dados em SQLi):
```text
# Exemplo de regra SecRule do ModSecurity para detectar SQL Injection no parâmetro ARGS
SecRule ARGS "(?i)(?:\b(alter|create|delete|drop|exec(ute){0,1}|insert|merge|select|update|union|all)\b.*\b(from|into|table|database)\b)" \
"id:1000,phase:2,deny,status:403,msg:'Bloqueio WAF: Tentativa de SQL Injection detectada'"
````

5. História do Conteúdo

Nos anos 1990, os firewalls de pacote e _Stateful_ resolviam invasões de infraestrutura, mas então surgiu a World Wide Web (www) comercial. Os sites pararam de ser apenas leitura de texto e passaram a processar compras, formulários e cadastros. O alvo do atacante migrou do sistema operacional para a aplicação em si. O WAF foi forjado no início dos anos 2000 como uma exigência emergencial (impulsionada por normativas como o [[Cyber_PCI_DSS|PCI-DSS]]) para defender sites mal programados que não validavam as entradas de texto dos usuários.