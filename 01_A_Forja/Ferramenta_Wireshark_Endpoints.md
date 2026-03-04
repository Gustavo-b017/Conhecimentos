---
tags:
  - tipo/ferramenta
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Ferramenta_Wireshark_Endpoints

#### 1. O Axioma (A Definição Rígida)
**O que é:** O painel de Endpoints é a interface do Wireshark que lista as estatísticas individuais de cada endereço de hardware (MAC) ou rede (IPv4/IPv6, TCP/UDP) que emitiu ou recebeu dados durante uma sessão.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ele extrai uma lista limpa de todos os "nós" da rede. Mostra de forma isolada quantos pacotes foram transmitidos (Tx) e quantos foram recebidos (Rx) por cada IP específico.
*   **O Problema que Resolve:** Isola o "Paciente Zero". Quando a rede cai devido a um [[Cyber_Ataque_DDoS]] interno ou a um [[Cyber_Malware_Worm]], o painel de Endpoints aponta imediatamente qual IP da máquina local está disparando 50 mil conexões por segundo de forma alucinada.
*   **Visão Sênior (Vulnerabilidades/Escala):** A genialidade aqui está na identificação de Botnets e C2 (Command & Control). Se você organizar a lista pela coluna de Endpoints Remotos (IPv4) baseada na menor quantidade de pacotes (ex: IPs que só mandaram 2 pacotes esporádicos o dia todo), você localiza os sinais de "Beaconing" (Sinal de vida) que malwares enviam para servidores na Rússia ou China, que normalmente passariam despercebidos no oceano de tráfego legítimo.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A aba de Endpoints atua como o **Rastreador de Presenças na Catraca de uma Festa VIP**. Não importa o quão cheia a festa esteja ou quantas conversas cruzadas estejam acontecendo no salão. A catraca registrou perfeitamente quantas vezes o convidado de "Identidade X" entrou e saiu, permitindo localizar rapidamente quem é o encrenqueiro do evento.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Utilização para caçar anomalias isolando o atacante de maior fluxo:
```text
# Menu Path:
Statistics -> Endpoints -> Aba IPv4
# Dica de campo: Clique na coluna "Tx Bytes" para ordenar em forma decrescente e encontrar a máquina que está exfiltrando (fazendo upload de) informações sigilosas.
````

5. História do Conteúdo

Técnicas de isolamento de terminais eram usadas por administradores do Unix escrevendo comandos complexos de `awk` e `grep` em cima de arquivos gerados por `tcpdump`. A interface unificada de Endpoints do Wireshark democratizou a perícia digital forense, permitindo o isolamento do criminoso com apenas dois cliques de mouse.