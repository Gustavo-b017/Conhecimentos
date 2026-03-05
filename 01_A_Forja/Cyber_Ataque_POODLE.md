---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Cyber_Ataque_POODLE

#### 1. O Axioma (A Definição Rígida)
POODLE (Padding Oracle On Downgraded Legacy Encryption) é uma vulnerabilidade de rebaixamento fatal que explora o design falho de servidores na Camada de Apresentação (Camada 6 do [[Rede_Modelo_OSI|modelo OSI]]) para forçar o uso do obsoleto protocolo [[Rede_SSL|SSL 3.0]] e decifrar comunicações seguras.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Se a vítima e o servidor preferem o [[Rede_TLS]], mas ainda mantêm o suporte para [[Rede_SSL|SSL 3.0]] como "legado de segurança", o atacante interfere no *Handshake* ([[Cyber_Man_In_The_Middle|MITM]]). Ele bloqueia as tentativas de usar TLS, forçando ambas as partes a rebaixarem (Downgrade) a conexão para o fraco SSL 3.0. Depois, ele ataca a fraqueza no sistema de preenchimento (padding) do bloco de cifra (CBC), vazando bytes em texto claro (como cookies de sessão) através da observação dos erros matemáticos.
- **O Problema que Causa:** Assassina a Confidencialidade de dados em trânsito. Um atacante ganha o cookie de login do banco do alvo simplesmente forçando o erro e injetando requisições JavaScript na mesma rede (Wi-Fi).
- **Visão Sênior (Vulnerabilidades/Escala):** É uma falha pura de design de protocolo, não de programação. A única solução é amputar o paciente: o administrador precisa desabilitar o suporte ao SSL 3.0 em todos os servidores (o que, segundo o [[Cyber_PCI_DSS]], é exigência imediata de conformidade). Qualquer servidor corporativo hoje que ainda permita a conexão via SSL 3.0 reprova instantaneamente em frameworks de segurança.

#### 3. As Sinapses (Conexões Livres)
O [[Cyber_Ataque_POODLE]] é o equivalente a **forçar o exército a lutar de espadas**. O seu computador tem um tanque de guerra blindado ([[Rede_TLS|TLS 1.2]]), mas guarda uma espada enferrujada ([[Rede_SSL|SSL 3.0]]) no porão por "questões de compatibilidade" com aliados velhos. O atacante (em um ataque de [[Cyber_Man_In_The_Middle]]) corta a gasolina do tanque de guerra, e como o sistema é burro, ele automaticamente diz: "Ok, o tanque quebrou, vamos usar a espada". Assim que você saca a espada, o atacante a quebra em pedaços e rouba o seu colar (os cookies de acesso).

#### 4. Pragmatismo Aplicado (Código/Implementação)
Comando mandatório com `openssl` (citado em documentação tática de hardening) para auditar um servidor web e atestar se ele está vulnerável a este rebaixamento de conexão 4:
```bash
# Força o servidor a aceitar uma conversa morta em SSLv3. O resultado correto de segurança é a conexão ser sumariamente REJEITADA.
openssl s_client -connect www.site-da-empresa.com.br:443 -ssl3
````

5. História do Conteúdo

Descoberto por pesquisadores do Google em Outubro de 2014. O ataque foi o martelo final no prego do caixão do protocolo SSL. Enquanto a falha _Heartbleed_ (ocorrida meses antes) era um erro de código que podia ser atualizado (Patched), o POODLE era uma falha matemática intransponível de fundação do SSL 3.0, obrigando a internet global a transicionar agressivamente para o TLS.