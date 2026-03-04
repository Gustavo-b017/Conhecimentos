---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Ataque_DDoS_SYN_Flood
#### 1. O Axioma (A Definição Rígida)
**O que é:** Um ataque de Negação de Serviço Distribuído (DDoS) no qual o atacante inunda o alvo com falsas requisições de sincronização TCP, explorando o design do protocolo para esgotar a memória do servidor antes que a conexão seja estabelecida.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O atacante envia uma avalanche de pacotes com a flag SYN ativada. O servidor alvo responde com SYN-ACK e reserva recursos (RAM) para a conexão, aguardando o ACK final do cliente. Como o atacante forjou o IP de origem ou simplesmente ignora a resposta, o ACK nunca chega. O servidor fica com milhares de conexões presas no estado "half-open" (semi-abertas).
*   **O Problema que Causa:** O esgotamento rápido da tabela de conexões do sistema operacional. Quando o limite é atingido, o servidor para de responder a usuários legítimos, ferindo o princípio da Disponibilidade da [[Cyber_Triade_CID]].
*   **Visão Sênior (Vulnerabilidades/Escala):** O ataque prova que o [[Rede_TCP_3_Way_Handshake]] possui uma vulnerabilidade de design nativa. A mitigação moderna não pode ser feita apenas fechando portas; ela exige a implementação em nível de Kernel ou [[Rede_Firewall]] de *SYN Cookies* (onde o servidor responde ao SYN-ACK usando uma assinatura matemática sem alocar memória até que o ACK retorne).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_Ataque_DDoS_SYN_Flood]] opera idêntico a um **trote telefônico coordenado em uma pizzaria**. O atacante liga, pede a pizza (SYN) e dá um endereço falso. O atendente anota o pedido, aloca o ingrediente e o motoqueiro (SYN-ACK), e fica esperando a entrega ser confirmada. Multiplique isso por 10 mil ligações por segundo. A pizzaria entra em colapso logístico, o forno fica travado, e quando um cliente legítimo tenta pedir comida, a linha dá ocupado.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O ataque pode ser testado em laboratório (ou em auditorias de penetração) utilizando o `netwox`, gerando milhares de conexões fantasmas que podem ser visualizadas travando o alvo.
```bash
# Executa a ferramenta netwox (módulo 76) para disparar o ataque SYN Flood contra o IP e porta (ex: telnet na porta 23)
netwox 76 -i 192.168.204.136 -p 23
````

5. História do Conteúdo

Detectado em larga escala na década de 1990 (notoriamente no ataque contra o provedor Panix em 1996), este foi o ataque que forçou a comunidade global de infraestrutura a perceber que o TCP/IP foi criado para ambientes de confiança mútua e era militarmente inadequado para a internet comercial pública sem a criação de escudos ativos.