---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---
# Rede_Subnetting
## 1. O Axioma (A Definição Rígida)
> **O que é:** Subnetting é a técnica cirúrgica de fatiar uma grande rede lógica de [[Rede_IP]] em pedaços menores, isolados e eficientes, manipulando os bits da Máscara de Sub-rede para definir exatamente onde termina o endereço da "Rede" e onde começa o endereço do "Host".

## 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de usar classes fixas engessadas (A, B, C), usamos a notação **CIDR** (Classless Inter-Domain Routing), representada por uma barra (ex: `/24`). O número após a barra indica quantos bits da esquerda para a direita estão "travados" para identificar a Rede. O restante dos bits sobra para os dispositivos locais.
*   **O Problema que Resolve:** O desperdício criminoso de IPs e o excesso de ruído na rede. Se uma empresa com 50 computadores ganhasse uma Classe B inteira (65.534 IPs), dezenas de milhares de endereços ficariam inutilizados. Além disso, o Subnetting diminui o "Domínio de Broadcast": menos máquinas gritando ao mesmo tempo no ouvido das outras. Frequentemente mapeado 1:1 com [[Rede_VLAN]]s.
*   **Visão Sênior (Vulnerabilidades/Escala):** O cálculo manual de VLSM (Variable Length Subnet Masking) é altamente propenso a falhas humanas. Um erro matemático no fatiamento resulta em sobreposição de IPs (Overlapping), fazendo com que pacotes entrem em *loop* infinito ou nunca cheguem ao destino. Requer documentação obsessiva.

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
Fazer Subnetting é atuar como o **Síndico de um Loteamento Gigante**. A operadora te entrega um terreno enorme chamado `192.168.0.0` (O [[Rede_IP]]). Se você deixar tudo aberto, vira uma praça caótica. Usando a Máscara de Sub-rede, você levanta muros físicos lógicos, criando o "Condomínio RH", o "Condomínio TI" e o "Condomínio Visitantes". Dispositivos em sub-redes diferentes **não** conseguem conversar diretamente pelo switch local; eles são obrigados a passar pela alfândega do [[Rede_Hardware]] (Roteador), onde o [[Rede_Firewall]] pode inspecioná-los..

## 4. Pragmatismo Aplicado (Código e Implementação)
A matemática que todo engenheiro de redes tem que saber de cabeça. A regra de ouro para descobrir quantas máquinas cabem em uma sub-rede é a fórmula: `2^(32 - CIDR) - 2`.

Exemplo de fatiamento padrão do mercado (CIDR `/24`):
*   Total de bits do IPv4: 32.
*   Bits usados pela Rede: 24 (A máscara `255.255.255.0` trava os 3 primeiros octetos).
*   Bits que sobram para os Hosts: 8 (32 - 24).
*   Cálculo: `2^8 = 256` IPs totais [9].
*   Tiramos 2 IPs obrigatórios (o primeiro `X.X.X.0` identifica a Rede, o último `X.X.X.255` é o Broadcast para gritar com todos) [10].
*   **Resultado:** 254 IPs usáveis reais para o [[Rede_DHCP]] distribuir para as máquinas.

## 5. História do Conteúdo
No início da internet, os endereços IP eram divididos estritamente em Classes (A, B e C).Era um sistema burguês: ou você era uma universidade gigante e recebia 16 milhões de IPs (Classe A), ou você era uma pequena empresa e recebia 254 (Classe C). Não havia meio termo. Quando a internet estourou nos anos 90, os engenheiros entraram em pânico percebendo que os endereços IPv4 acabariam em poucos anos. O CIDR (RFC 1519) foi introduzido às pressas em 1993, quebrando a rigidez das classes e permitindo fatiar redes em qualquer tamanho arbitrário. Foi a salvação logística que manteve a internet de pé até hoje.