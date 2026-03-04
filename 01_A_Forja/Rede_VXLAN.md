---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Rede_VXLAN
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Virtual Extensible LAN (VXLAN) é um protocolo de tunelamento avançado de Data Center que encapsula quadros de Camada 2 (MAC) dentro de pacotes UDP da Camada 3 (IP), criando redes locais virtuais gigantescas por cima de qualquer infraestrutura roteada.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ele pega a "VLAN" antiga e a embrulha. Usa identificadores de 24 bits (VNID), permitindo a existência de até 16 milhões de redes isoladas (contra o limite pífio de 4.096 da VLAN normal). O tráfego L2 é roteado pela malha L3 sem que a infraestrutura subjacente precise saber dos MACs dos servidores originais.
*   **O Problema que Resolve:** O pesadelo da nuvem e da virtualização (AWS/Azure). Em um Data Center moderno com arquitetura [[Rede_Arquitetura_Data_Center]] (Spine-Leaf), você tem milhões de Máquinas Virtuais (VMs). O VXLAN permite que uma VM no rack A (São Paulo) converse com uma VM no rack B (Rio de Janeiro) achando que ambas estão conectadas no mesmíssimo switch físico, sem o limite matemático do padrão 802.1Q da [[Rede_VLAN]] clássica.
*   **Visão Sênior (Vulnerabilidades/Escala):** Adiciona peso (Overhead) de cerca de 50 bytes no cabeçalho do pacote. Isso exige obrigatoriamente que toda a rede do Data Center seja reconfigurada para suportar *Jumbo Frames* (aumentar o MTU da rede para mais de 1500 bytes), do contrário, os roteadores fragmentarão os pacotes de forma tão agressiva que o processador do servidor derreterá.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se a [[Rede_VLAN]] tradicional é **levantar uma parede de vidro dentro de um escritório fechado**, a [[Rede_VXLAN]] é construir um **Portal de Teletransporte** entre dois prédios em estados diferentes. Quando você atravessa o portal mágico, a física do espaço é dobrada: você está no Rio de Janeiro, mas para todos os efeitos elétricos e lógicos da sua placa de rede, você jura que está na mesma sala em São Paulo.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Usado massivamente em infraestruturas como código e redes baseadas em Linux (SDN). Exemplo rudimentar de criação de um túnel VXLAN no terminal Linux:
```bash
# Cria uma interface virtual vxlan10 mapeando o tráfego da porta UDP 4789 para um IP remoto
ip link add vxlan10 type vxlan id 10 remote 10.0.0.5 dstport 4789 dev eth0
ip link set up dev vxlan10
````

5. História do Conteúdo

Criado ao redor de 2011 através de uma união improvável entre gigantes inimigas (Cisco, VMware e Red Hat). A computação em nuvem estava estagnada: as fazendas de servidores haviam crescido tanto que os roteadores e switches clássicos simplesmente não tinham mais memória RAM física para guardar as tabelas de milhões de placas de rede virtuais (MAC Addresses). O VXLAN salvou a nuvem ao esconder esses milhões de MACs dentro do roteamento IP tradicional.