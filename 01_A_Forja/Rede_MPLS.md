---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

### Rede_MPLS
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Multiprotocol Label Switching (MPLS) é uma técnica de roteamento corporativo de alto desempenho que direciona dados de um nó a outro baseando-se em rótulos curtos de caminho (Labels) em vez de longos endereços IP, operando logicamente entre as Camadas 2 e 3.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O roteador de borda (Provider Edge - PE) recebe o pacote do cliente, anexa um cabeçalho de 32 bits (o *Label*) e o joga na nuvem da operadora. Os roteadores internos da operadora (Provider - P) não abrem a Camada 3 para ler o [[Rede_IP]] de destino; eles apenas olham o número do rótulo e repassam o pacote na velocidade da luz.
*   **O Problema que Resolve:** A lentidão extrema dos roteadores dos anos 90. Naquela época, processar e ler o IP completo de cada pacote consumia muita CPU. O rótulo transformou roteadores complexos em "Switches super-rápidos". Também cria VPNs lógicas de altíssima segurança sem precisar de criptografia (L3VPN).
*   **Visão Sênior (Vulnerabilidades/Escala):** O MPLS é caríssimo e inflexível. Ele exige links físicos dedicados e dependência estrita do provedor de telecomunicações (Vendor Lock-in). Nos dias de hoje, empresas estão abandonando ativamente o custo abusivo do MPLS em favor do [[Rede_SD_WAN]], que usa internet comum barata somada a criptografia.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O Roteamento IP Tradicional é **dirigir um carro lendo as placas de cada cidade**: a cada cruzamento, você para, lê o mapa, calcula a rota e segue em frente (Lentidão). O MPLS é **despachar sua carga através de um Sistema de Trens Expressos**. O pacote é colocado no trem e recebe um bilhete impresso na janela (O Rótulo/Label). Os controladores dos trilhos não querem saber qual o destino final da carga, eles só olham a cor do bilhete e acionam as alavancas dos trilhos em milissegundos.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Para debugar se o tráfego está cruzando a malha da operadora de telecom através de rótulos MPLS em vez de IPs puros, o engenheiro checa a tabela de encaminhamento rápido (LFIB) no roteador:
```bash
# Verificando a Tabela de Rótulos de um equipamento Cisco
show mpls forwarding-table
# Output:
# Local Label  Outgoing Label  Prefix           Next Hop
# 1045         2048            192.168.1.0/24   10.1.1.2
````

5. História do Conteúdo

Nascido no final dos anos 1990 pela IETF, o MPLS foi criado porque a "Internet estava devagar demais". Hardware de silício era caro, e processar a Camada 3 do modelo OSI era um inferno matemático. Ironicamente, hoje o hardware tornou-se infinitamente rápido e barato, anulando a premissa de velocidade do MPLS. No entanto, ele se recusou a morrer porque provou ser a melhor ferramenta já criada para prover túneis privados e Qualidade de Serviço ([[Rede_QoS]]) com garantias de contrato rigorosas para grandes bancos.