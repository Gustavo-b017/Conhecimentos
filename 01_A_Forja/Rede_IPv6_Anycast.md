---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Rede_IPv6_Anycast
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Anycast é um método revolucionário de roteamento de rede (fortemente atrelado ao IPv6) onde um **único endereço IP destino é compartilhado por múltiplos servidores espalhados geograficamente**; a rede direciona o pacote automaticamente para a máquina topologicamente mais próxima.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez do modelo Unicast (1 IP = 1 Servidor físico exclusivo), empresas como a Cloudflare anunciam o mesmo endereço de IP (ex: `1.1.1.1` ou um bloco IPv6) a partir de 200 Data Centers pelo planeta via protocolo BGP. O roteador do provedor de internet do usuário sempre escolhe o caminho com o menor "custo" físico/lógico até esse IP.
*   **O Problema que Resolve:** Mata a latência global. Se um serviço está apenas em Nova York, o mundo inteiro sofre com a física do cabo submarino. Com o Anycast, o usuário no Brasil acessa a cópia do serviço que está em São Paulo, o da Europa acessa em Paris, ambos usando o mesmíssimo IP.
*   **Visão Sênior (Vulnerabilidades/Escala):** O pesadelo do Anycast é o tráfego [[Rede_TCP]] orientado a estado ([[Rede_Stateful]]). Se a topologia da internet balançar no meio de um download (um cabo é rompido no bairro), o pacote seguinte pode ser roteado para um servidor secundário Anycast diferente. Como esse segundo servidor não viu o *Handshake TCP*, ele reseta a conexão (RST). É por isso que Anycast é majoritariamente usado com protocolos sem estado, como o UDP ([[Rede_DNS]]).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O roteamento Anycast é idêntico ao serviço **190 da Polícia ou 192 do SAMU**. Se você ligar para 190 estando em São Paulo, cai na delegacia de São Paulo. Se você pegar um avião, for para Manaus e discar o mesmíssimo 190, a ligação cai na delegacia de Manaus. Um único número (IP), múltiplos postos de atendimento (Servidores) espalhados pelo mapa; o sistema telefônico (O Roteador BGP) garante que você seja atendido por quem está fisicamente mais perto de você.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Não se configura Anycast num terminal comum; ele é configurado nos anúncios de borda (BGP) dos ASN das operadoras. A forma de testar se um IP comercial utiliza Anycast é usar pings de máquinas em continentes diferentes e observar a latência milagrosa (ex: 5ms no mundo todo, quebrando as leis da física).
```bash
ping 1.1.1.1 # DNS da Cloudflare responderá com latência mínima não importa o país em que você esteja rodando o comando.
````

5. História do Conteúdo

Embora as definições tenham surgido em RFCs experimentais em 1993, foi apenas com o crescimento dos ataques massivos de [[Cyber_Ataque_DDoS]] na década de 2010 que a arquitetura explodiu. Descobriu-se que o Anycast atuava como um _Load Balancer_ natural e geográfico: se a Coreia do Norte disparasse um DDoS monumental contra um IP, os roteadores BGP enviariam o ataque apenas para o servidor da Coreia do Sul (o mais perto), deixando as cópias daquele mesmo IP na Europa e Américas perfeitamente ilesas.