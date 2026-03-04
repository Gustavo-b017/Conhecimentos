---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_Streaming_Telemetry

#### 1. O Axioma (A Definição Rígida)
**O que é:** Streaming Telemetry (Telemetria Contínua) é o moderno paradigma de observabilidade onde os equipamentos de rede **empurram (push)** proativamente fluxos de dados vitais e estruturados em tempo real (milissegundos) para coletores centralizados, substituindo os antigos e lentos protocolos de requisição baseados em perguntas.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de um servidor perguntar ao switch "Como você está?", o engenheiro assina caminhos de dados (Sensor Paths) no switch usando modelos padronizados como o YANG. O equipamento passa a vomitar os dados de CPU, BGP e buffers continuamente via protocolos de alto desempenho (como gRPC ou NETCONF) direto para bancos de dados de séries temporais (TSDB).
*   **O Problema que Resolve:** Mata a lentidão e a cegueira do protocolo SNMP legado. O SNMP atuava sob o modelo de *Pull* (pergunta a cada 5 minutos). Se um micro-congestionamento (microburst) inundasse a fila do switch por 2 segundos e fizesse pacotes caírem, o SNMP nunca veria o evento, pois ele ocorreu entre os intervalos de leitura. A telemetria contínua vigia todos os segundos.
*   **Visão Sênior (Vulnerabilidades/Escala):** A telemetria contínua causa uma "Avalanche de Dados" (*Data Deluge*). Um Data Center de médio porte transmitindo métricas a cada segundo gera terabytes de logs diários. Se os servidores coletores e indexadores não forem arquitetados para ingestão massiva (usando Kafka, InfluxDB ou Prometheus), a plataforma de monitoramento será afogada pelo próprio tráfego da infraestrutura, exigindo ferramentas de IA para extrair sentido do ruído.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O protocolo SNMP antigo era um **Médico visitando o quarto do paciente de hora em hora** para checar a temperatura (Pull). Se o paciente tivesse uma parada cardíaca 5 minutos após a saída do médico e voltasse à vida sozinho, o sistema nunca saberia. O [[Rede_Streaming_Telemetry]] é ligar o paciente a um **Monitor Holter Contínuo na UTI** (Push). Cada mínimo batimento cardíaco é jorrado ininterruptamente para a tela da enfermaria; qualquer engasgo de milissegundos soa um alarme. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
A configuração de telemetria é declarativa no roteador. O comando diz ao equipamento qual dado capturar e para onde atirar em tempo contínuo (Exemplo IOS-XE):
```bash
telemetry ietf subscription 101
 encoding encode-kvb
 filter xpath /memory-ios-xe-oper:memory-statistics/memory-statistic
 stream yang-push
 update-policy periodic 100 # Empurre as estatísticas de memória a cada 100 centissegundos
 receiver ip address 10.1.1.50 57000 protocol grpc-tcp
````

5. História do Conteúdo

A tecnologia nasceu das dores puras das provedoras _Hyper-scale_ (Google, AWS, Meta). Quando a velocidade dos cabos saltou para 100G e 400G, a perda de pacotes por enfileiramento começou a ocorrer em janelas de nanossegundos. Eles descobriram que usar a CPU do switch para responder às pesquisas (Polling) do SNMP estava travando o equipamento. A solução foi mudar a arquitetura: criar um chip dedicado que apenas transmitisse a saúde do sistema numa via de mão única, sem esperar que alguém pedisse.