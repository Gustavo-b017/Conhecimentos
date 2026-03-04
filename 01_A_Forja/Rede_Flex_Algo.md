---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_Flex_Algo

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Flexible Algorithm (Flex-Algo - RFC 9350) é a extensão para protocolos de roteamento interno (IGP - IS-IS/OSPF) que permite a criação de topologias lógicas independentes (fatias), calculando rotas baseadas em restrições personalizadas (como atraso, links criptografados) de forma totalmente distribuída.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de todos confiarem no Algoritmo 0 padrão (SPF Baseado em Custo), os operadores ativam sub-algoritmos (identificadores 128 a 255) nos roteadores. O Algoritmo 128 pode ser ordenado a "achar o menor atraso e excluir links de baixa largura de banda". O IGP calcula uma nova topologia exclusiva para esse Flex-Algo e vincula ela a um endereço *Locator* SRv6 exclusivo. 
*   **O Problema que Resolve:** No passado remoto, desviar tráfego usando Engenharia de Tráfego exigia políticas estáticas ou controladores centralizados (SDN PCE) hiper complexos. O Flex-Algo automatiza isso devolvendo a responsabilidade para o IGP e forjando o *Network Slicing*, crucial em 5G (ex: A cirurgia remota entra na fatia do Flex-Algo de latência; o YouTube entra na fatia de custo base).
*   **Visão Sênior (Vulnerabilidades/Escala):** A genialidade é a imunidade a falhas humanas e "self-healing" nativo. Como quem computa é o próprio protocolo link-state (IS-IS), se uma fibra óptica crucial para a fatia de "Baixa Latência" romper, o roteador reconverge e acha matematicamente um novo caminho, confinado puramente às restrições originais daquele Flex-Algo. Um túnel não cai, a fatia apenas se dobra para continuar viva.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Imagine o roteamento normal como o trânsito da cidade onde carros sempre pegam as ruas mais largas (**Métrica Padrão**). O Flex-Algo é ligar o aplicativo de GPS Waze em perfis distintos, criando realidades e mapas paralelos sobre a mesma [[Rede_Topologias]] física. Os carros da ambulância veem apenas o mapa "Evitar ruas com pedágios/Semáforos" (**Algo 128: Low Delay / Link-Affinity Exclude**), ignorando ruas largas se estas forem mais demoradas. Cada perfil navega pelo mesmo asfalto físico, obedecendo regras lógicas diametralmente exclusivas.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação em roteadores (ex: Junos) baseia-se em alterar a métrica do FAD (Flex-Algo Definition) e atrelar a um SRv6 Locator exclusivo para que os pacotes ganhem o carimbo de entrada daquela "fatia":
```bash
# Vendor: Juniper (Junos)
# Definindo o Flex-Algo 128 focado em Métrica de Delay e vinculando um Locator
set routing-options flex-algorithm 128 definition metric-type delay
set routing-options source-packet-routing srv6 locator loc-delay-128 2001:db8:b1:1::/64 algorithm 128
set protocols isis source-packet-routing flex-algorithm 128
````

_(Fonte do pragmatismo referenciado no Junos Day One__)._

5. História do Conteúdo

Surgiu do abismo arquitetural gerado pelas antenas 5G e as exigências da ITU-T sobre o URLLC (Ultra-Reliable Low-Latency Communications). Operadoras precisavam vender links fatiados e isolados para indústrias financeiras ou médicas, mas as velhas caixas de engenharia de tráfego centralizadas reagiam de forma muito lenta ou manual. A extensão matemática do Dijkstra dentro do coração mais confiável de redes (O OSPF/IS-IS) resolveu o isolamento lógico sem demandar novos hardwares