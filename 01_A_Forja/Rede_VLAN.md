---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---
### Rede_VLAN
#### 1. O Axioma (A Definição Rígida)
**O que é:** A Virtual Local Area Network (VLAN) é uma tecnologia de particionamento lógico na Camada 2 (Enlace) que divide uma única rede física em múltiplos domínios de broadcast isolados, criando a ilusão de que dispositivos estão conectados a switches diferentes.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Emprega o padrão IEEE 802.1Q para injetar uma "Tag" (etiqueta) no cabeçalho dos quadros (*Frames*) Ethernet. Switches gerenciáveis leem essa Tag e garantem que os dados de uma VLAN (ex: VLAN 10) jamais vazem para portas pertencentes a outra (ex: VLAN 20).
*   **O Problema que Resolve:** Se todos os dispositivos de um prédio ficassem na mesma rede física padrão, o tráfego de "gritos" na rede (*broadcast*) causaria lentidão crônica e falhas graves de segurança (o RH enxergaria os servidores da Engenharia). A VLAN resolve isso via software, evitando o custo proibitivo de comprar switches físicos separados para cada departamento.
*   **Visão Sênior (Vulnerabilidades/Escala):** VLANs separam tráfego, mas **não criptografam** os dados. Elas sofrem riscos de *VLAN Hopping*, um ataque onde um invasor forja Tags duplas para "pular" as restrições lógicas do switch e acessar redes restritas. Além disso, se duas VLANs precisam se comunicar, o tráfego é obrigado a subir para a Camada 3 e passar pela inspeção rigorosa de um Roteador ou Layer-3 Switch (Inter-VLAN Routing).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Uma VLAN é o equivalente arquitetônico de dividir um grande galpão de escritório (*Open-Space*) com paredes de vidro acústico. A equipe de Vendas (VLAN 10) e a de TI (VLAN 20) compartilham o mesmo teto, o mesmo piso e a mesma infraestrutura elétrica (o Switch Físico), mas uma equipe não consegue ouvir o que a outra fala por causa da parede acústica (Domínio de Broadcast isolado). Para a TI entregar um documento para Vendas, eles precisam sair da sala, passar pela recepção (o Roteador / Gateway) e pedir autorização do segurança, que pode ser o [[Rede_Firewall]]. A VLAN interage diretamente com o [[Rede_Subnetting]], onde a boa prática dita que cada VLAN isolada deve possuir a sua própria sub-rede lógica de IP dedicada.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O pão com manteiga de qualquer Engenheiro de Redes ao configurar portas físicas em switches Cisco para designar isolamento:

```bash
# Entrar em modo de configuração e criar a parede lógica
Switch(config)# vlan 10
Switch(config-vlan)# name Diretoria

# Informar que a porta física X pertence APENAS àquela parede lógica
Switch(config)# interface gigabitEthernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
````

5. História do Conteúdo

No início dos anos 90, os cabos eram caros e mover um funcionário de departamento exigia que o técnico fosse até o armário do servidor e trocasse fisicamente os cabos de porta (um pesadelo logístico). W. David Sincoskie, um engenheiro de redes, concebeu a ideia da VLAN justamente para solucionar essa dor operacional: "E se a gente pudesse mudar a rede de um funcionário apenas digitando um comando de software no switch, sem ter que tocar em cabos físicos?". O que nasceu por preguiça logística, tornou-se hoje o padrão-ouro inegociável de segmentação e higiene cibernética.