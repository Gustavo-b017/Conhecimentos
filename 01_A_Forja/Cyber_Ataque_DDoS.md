---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/alta
  - status/4_evergreen
---

### Cyber_Ataque_DDoS
#### 1. O Axioma (A Definição Rígida)
**O que é:** O *Distributed Denial of Service* (DDoS) é um ataque cibernético que visa tornar um serviço, rede ou servidor indisponível para o tráfego legítimo, sobrecarregando os recursos da vítima com uma inundação massiva de dados falsos de múltiplas origens.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O ataque opera em diferentes camadas. Pode atacar a Camada 4 com *SYN Floods* para esgotar a memória de portas abertas em um servidor (half-open attack). Também pode abusar da falta de estado do [[Rede_UDP]] na Camada 3/4, forjando o IP da vítima e pedindo dados para servidores externos (como DNS ou NTP), que enviam respostas gigantescas de volta para a vítima (Ataque de Amplificação e Reflexão).
*   **O Problema que Causa:** Fere fatalmente o pilar da Disponibilidade da Tríade de Segurança (CID), causando indisponibilidade de serviços web e prejuízos financeiros massivos.
*   **Visão Sênior (Vulnerabilidades/Escala):** Atacantes modernos raramente usam as próprias máquinas; eles controlam *Botnets* gigantescas compostas por dispositivos de IoT infectados (como a botnet Mirai) para gerar tráfego. A mitigação local via firewall corporativo é inútil contra ataques volumétricos; exige-se a filtragem e dispersão na nuvem com provedores como a Cloudflare.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_Ataque_DDoS]] de amplificação é o **trote telefônico com pedido de pizza**. O atacante liga para 5.000 pizzarias fingindo ser você, e pede as maiores pizzas do cardápio para o seu endereço. Alguns minutos depois, 5.000 entregadores chegam à sua rua simultaneamente, bloqueando completamente o trânsito e impedindo que você saia ou entre em casa.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Ataques baseados em esgotamento de TCP (*SYN Flood*) são rastreáveis via `Wireshark` procurando a ausência do pacote *ACK* final ou via terminal no Linux visualizando soquetes presos na fase de recebimento:
```bash
netstat -n -p | grep SYN_RECV
````

5. História do Conteúdo

Cresceu rapidamente com a explosão comercial da internet nos anos 90, evoluindo de simples interrupções feitas por "script kiddies" para o uso como arma geopolítica e ferramenta de extorsão (_Ransom DDoS_) visando derrubar instituições financeiras e infraestruturas críticas em todo o mundo.