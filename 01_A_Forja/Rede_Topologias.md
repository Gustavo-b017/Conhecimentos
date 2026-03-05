---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

# Rede_Topologias
## 1. O Axioma (A Definição Rígida)
> **O que é:** Topologia de rede é o mapa estrutural, físico ou lógico, que dita exatamente como os nós (dispositivos) e os links (cabos/ondas) estão interconectados para a transmissão de dados.

## 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Barramento (Bus):** Todos os computadores ligados em um único cabo linear. Se o cabo corta no meio, a rede inteira morre. (Obsoleto, gerava colisões massivas).
*   **Estrela (Star):** O padrão absoluto das [[Rede_LAN]] modernas. Todos os PCs se conectam a um equipamento central (o [[Rede_Hardware]] Switch). Se um cabo de PC quebra, só ele cai.
*   **Malha (Mesh):** Cada nó se conecta a múltiplos ou todos os outros nós. Altíssima redundância. A própria Internet ([[Rede_WAN]]) é uma topologia de malha gigante.
*   **O Problema que Resolve:** Sem um design estruturado, o tráfego de dados elétricos causaria interferência mútua constante. A topologia define o fluxo, o custo de cabeamento e o grau de resiliência.
*   **Visão Sênior (Vulnerabilidades/Escala):** A topologia em Estrela introduz um Ponto Único de Falha (SPOF - *Single Point of Failure*). Se o Switch central queimar, os 500 computadores ao redor dele ficam cegos. A mitigação arquitetural exige redundância física (dois switches centrais em *stack* operando juntos).

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
Topologias são puramente **Planejamento Urbano**. A topologia de Barramento é uma estrada de mão única onde todos os carros precisam parar se houver um acidente. A topologia em Estrela é uma Rotatória Gigante (o Switch): todo o trânsito flui para o centro e é distribuído para a saída correta. É nessa rotatória que serviços vitais como o [[Rede_SLAAC]] (para endereços IPv6) ou DHCP são distribuídos. Se a rotatória trava, ninguém ganha endereço para circular.

A topologia em Malha (Mesh) é o sistema de vielas de um centro histórico europeu: se uma rua principal estiver fechada para obras, você vira à direita, pega três vielas menores e chega no destino de qualquer jeito. O [[Rede_Roteamento]] é o Waze que navega nessa malha.

## 4. Pragmatismo Aplicado (Código e Implementação)
A topologia não é um código que se digita, é uma arquitetura que se desenha (Geralmente usando softwares como Cisco Packet Tracer, Microsoft Visio ou Draw.io).
Na prática de uma casa (Topologia Híbrida - Estrela Estendida):
```text
(Internet) --- [Roteador Wi-Fi] 
                  /    |    \
              [PC]  [TV]  [Switch Secundário]
                             /       \
                        [PS5]      [Xbox]
````

5. História do Conteúdo

A evolução das topologias é a história de fugir do caos. Nos anos 70, com o início da Ethernet, a topologia de Barramento foi usada porque cabos coaxiais eram caros. Os PCs "mordiam" o cabo como vampiros para escutar o tráfego. Quando o silício barateou nos anos 90, construir Switches de alta performance tornou-se viável, e o mundo inteiro abandonou o barramento para adotar a topologia em Estrela, trocando a economia de cabos pela estabilidade mental de não ter a rede caindo todo dia.