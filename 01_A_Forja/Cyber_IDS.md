---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Cyber_IDS
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Intrusion Detection System (IDS) é um vigilante passivo de rede que espelha e analisa continuamente o tráfego interno em busca de assinaturas conhecidas de malwares ou anomalias comportamentais, gerando alertas sem interromper o fluxo de dados.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ele opera "out-of-band" (fora da linha principal de tráfego). O [[Rede_Switch|switch]] de rede copia todo o tráfego (via porta SPAN/Mirror) e entrega ao IDS. Ele compara os pacotes com um banco de dados de assinaturas (como um antivírus de rede) ou analisa desvios de tráfego baseados em heurística (ex: um PC do RH que de repente começa a escanear IPs do banco de dados).
*   **O Problema que Resolve:** O [[Rede_Firewall|Firewall]] não enxerga movimentação lateral (uma máquina da [[Rede_LAN|LAN]] atacando outra máquina da LAN). O IDS resolve o problema da "cegueira interna", dando visibilidade sobre o que acontece dentro do perímetro.
*   **Visão Sênior (Vulnerabilidades/Escala):** A maior falha do IDS é a **Fadiga de Alerta**. Como ele é passivo, ele não bloqueia nada; ele apenas grita. Se mal calibrado, gera dezenas de milhares de alertas (falsos positivos) por dia, fazendo com que a equipe de segurança passe a ignorar o painel de logs, permitindo que um ataque real passe despercebido. Além disso, é inútil contra tráfego criptografado se não houver um sistema de quebra de SSL.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_IDS]] é como o **Sistema de Câmeras de Segurança e Alarme Sonoro de um banco**. Ele observa o saguão e, se alguém sacar uma arma, ele dispara a sirene e avisa a central. Mas **ele não tem a capacidade física de impedir o assalto** (não trava portas, não atira, diferente do [[Cyber_IPS]]). Se o criminoso for rápido o suficiente e a polícia demorar, o dano será concretizado. Na TI, o alarme vai para a tela de uma plataforma de monitoramento contínuo ([[Cyber_Monitoramento_Continuo|SIEM]]) para que um analista humano tome a decisão.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O *Snort* é o IDS de código aberto mais consagrado do mundo. Um exemplo da anatomia de uma regra pragmática do Snort criada para alertar (e não bloquear) uma tentativa de acesso remoto indevido ao servidor de banco de dados via Telnet:
```text
# Regra do Snort: Alerta para tráfego TCP externo tentando atingir a porta 23 da LAN ([[Rede_Telnet|Telnet]])
alert tcp $EXTERNAL_NET any -> $HOME_NET 23 (msg:"ALERTA: Tentativa de acesso Telnet detectada"; sid:1000001; rev:1;)
````

5. História do Conteúdo

Criado no final dos anos 1980 (com projetos como o _Intrusion Detection Expert System - IDES_), o IDS surgiu porque o mundo acadêmico percebeu que firewalls isolavam o "fora", mas não auditavam o "dentro". A premissa era criar um sistema especialista baseado em regras lógicas para identificar usuários legítimos que se transformavam em ameaças internas (insider threats) abusando de seus privilégios na rede local.