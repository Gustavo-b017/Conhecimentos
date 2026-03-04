---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Rede_Segment_Routing_SRv6

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Segment Routing over IPv6 (SRv6) é uma arquitetura de roteamento na origem (Source Routing) que codifica instruções de caminho explícitas (SIDs de 128 bits) diretamente dentro do cabeçalho do pacote IPv6 nativo, eliminando a necessidade de protocolos legados de sinalização e preservação de estado, como LDP e RSVP-TE.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez da rede decidir o caminho a cada salto, o Roteador de Entrada (Headend) injeta um "Segment Routing Header" (SRH) no pacote com uma lista ordenada de segmentos (SIDs) a serem visitados. Cada SID possui um *Locator* (para roteamento até o nó) e uma *Function* (ação local a ser executada ao chegar lá, como encaminhar a uma VRF específica).
*   **O Problema que Resolve:** Escalabilidade e simplicidade extrema. Roteadores intermediários (trânsito) não precisam mais manter tabelas monstruosas de memória para cada túnel ou cliente; eles apenas roteiam o pacote IPv6 normalmente, pois toda a "inteligência" de roteamento viaja embutida no próprio pacote.
*   **Visão Sênior (Vulnerabilidades/Escala):** O SRv6 Clássico esmaga o desempenho do hardware. Como cada SID ocupa 16 bytes (128 bits), um túnel complexo de 10 saltos injeta um overhead massivo de 160 bytes no cabeçalho. Isso não apenas causa risco de fragmentação e queda de *MTU*, como obriga o *silício (ASIC)* dos roteadores legados a realizar múltiplas leituras pesadas de memória para processar a pilha de SIDs, estrangulando o *throughput* (PPS - Packets Per Second).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O SRv6 funciona exatamente como entregar a um entregador de transportadora **um caderno de instruções exatas de ruas para virar na origem (Source Routing)**, em vez de depender que em cada esquina haja um guarda de trânsito que precisa lembrar para onde cada pacote do mundo está indo (LDP/RSVP-TE). A inteligência e o estado são movidos do centro da cidade (o meio da rede) para o armazém de despacho (roteador de borda). 

#### 4. Pragmatismo Aplicado (Código e Implementação)
A fundação do SRv6 requer a alocação de um bloco IPv6 local e a ativação explícita sob a interface e o protocolo IS-IS, criando um Locator para que o domínio possa "ver" o roteador. Em equipamentos baseados no Cisco IOS-XR:
```bash
# Aloca o Locator e ativa na topologia IS-IS (IPv6 Data Plane nativo)
segment-routing
 srv6
  locators
   locator MAIN
    prefix 2001:db8:a1:1::/64
!
router isis 1
 address-family ipv6 unicast
  segment-routing srv6
   locator MAIN
````

5. História do Conteúdo

Padronizado primariamente pela IETF via SPRING WG (RFC 8402 e RFC 8986) na metade da década de 2010. Nasceu da constatação da falência arquitetural do MPLS em nuvens gigantes. Enquanto o SR-MPLS foi um degrau transitório aceitável para aproveitar o hardware antigo ("brownfield"), o SRv6 foi concebido como a utopia do estado "greenfield": convergir Datacenters baseados em contêineres e Service Providers globais num único Data Plane IPv6 unificado, fluído e programável.