---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_EtherChannel
#### 1. O Axioma (A Definição Rígida)
**O que é:** O EtherChannel (ou Link Aggregation) é uma tecnologia de infraestrutura que agrupa múltiplas portas Ethernet físicas em um único enlace lógico (Port-Channel), somando suas larguras de banda e provendo redundância automática.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Utiliza protocolos de negociação como o LACP (padrão aberto IEEE 802.3ad) ou o PAgP (proprietário da Cisco). Se você conectar quatro cabos de 1 Gigabit entre dois switches, o EtherChannel amarra os quatro, criando um "supercabo" lógico de 4 Gigabits.
*   **O Problema que Resolve:** Duas falhas sistêmicas: o Gargalo de Uplink e o bloqueio do [[Rede_STP]]. Pela regra do STP, se você ligar dois cabos entre dois switches, o STP bloqueia um deles para evitar loop, desperdiçando o cabo. O EtherChannel "engana" o STP, fazendo-o enxergar os quatro cabos físicos como apenas uma única porta lógica, mantendo todos ativos simultaneamente.
*   **Visão Sênior (Vulnerabilidades/Escala):** O maior mito da agregação de links é achar que um único download vai usar os 4 Gbps. O EtherChannel faz *balanceamento de carga por fluxo* (geralmente via hash de IP e MAC de origem/destino). Uma única transferência de arquivo de um PC para um Servidor vai usar sempre apenas 1 cabo (1 Gbps) do feixe, para evitar que os pacotes cheguem fora de ordem ao destino. A vantagem só é vista com *múltiplos* PCs acessando o servidor ao mesmo tempo.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Configurar um [[Rede_EtherChannel]] é **demolir os muros divisórios de 4 rodovias de pista única para construir uma super-rodovia de 4 faixas**. Se as rodovias fossem separadas, a polícia de trânsito (o STP) fecharia três delas para evitar que os carros ficassem andando em círculos no bairro. Ao juntá-las numa via larga expressa, 4 vezes mais caminhões podem transitar lado a lado, e se um buraco interditar a faixa 3 (Cabo rompido), o trânsito simplesmente flui pelas outras 3 faixas sem interromper a viagem de ninguém.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A sintaxe para agrupar as interfaces de hardware do switch e designar a negociação aberta (LACP):
```bash
# Seleciona as portas físicas
Switch(config)# interface range GigabitEthernet 0/1 - 2

# Força a formação do grupo lógico pedindo a negociação LACP (mode active)
Switch(config-if-range)# channel-group 1 mode active
````

5. História do Conteúdo

A tecnologia foi desenvolvida no início dos anos 90 pela Kalpana (uma empresa posteriormente comprada pela Cisco). O problema era financeiro: os switches centrais estavam recebendo mais tráfego dos computadores do que a porta principal (Uplink) aguentava. O custo para fabricar e comprar placas de rede 10 vezes mais rápidas (ex: passar de 10 Mbps para 100 Mbps) era proibitivo. O Link Aggregation permitiu que empresas escalassem sua banda empilhando cabos baratos que elas já possuíam, uma técnica tão eficiente que é a base dos Data Centers modernos até hoje.