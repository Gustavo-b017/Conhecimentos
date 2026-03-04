---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_QoS_Avancado

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Quality of Service (QoS) Avançado consolida os algoritmos cirúrgicos de enfileiramento Lógico (como LLQ e CBWFQ) combinados a arquiteturas físicas profundas de hardware de datacenters modernos (como VOQ - Virtual Output Queues) para mitigar o congestionamento e garantir latência matemática determinística.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **A Arquitetura Física - VOQ (Virtual Output Queues):** Em switches arcaicos (CIOQ), se a Porta 1 congestionar, todos os pacotes nas filas de entrada ficam engarrafados, mesmo pacotes que iam para a Porta 2 (o infame Head-of-Line Blocking - HOLB). A VOQ destrói o HOLB criando filas isoladas *na entrada* (Ingress PFE) dedicadas matematicamente a cada porta de *saída* (Egress) do datacenter. O pacote só atravessa o *Fabric* (a placa-mãe) quando a porta de destino envia uma permissão explícita (Grant/Token) afirmando ter espaço na memória, não desperdiçando banda interna.
*   **O Algoritmo Lógico - CBWFQ (Class-Based Weighted Fair Queuing):** Garante limites mínimos de largura de banda baseados em "Pesos". Se você alocou 20% para a classe "Web", ela recebe esses 20% durante a guerra do congestionamento, mas não tem exclusividade de *saída rápida* frente aos outros pacotes.
*   **O Algoritmo de Missão Crítica - LLQ (Low Latency Queuing):** O estado da arte do QoS tradicional. Pega a estrutura do CBWFQ e insere nela uma "Fila de Prioridade Estrita" (Strict Priority). Dados como VoIP ou URLLC (5G) são despachados à frente de absolutamente tudo, cortando a latência pela raiz.
*   **Visão Sênior (Vulnerabilidades/Escala):** O LLQ é uma arma letal para o resto da rede. Se a fila prioritária (Voz/Missão Crítica) sofrer uma inundação repentina, o hardware despachará apenas essa fila e **causará inanição (*Starvation*) letal** em todos os outros serviços da empresa. A mitigação obrigatória é implementar um *Policer* atrelado à fila LLQ: "Você tem prioridade absoluta de passar na frente de todos, *desde que* não ultrapasse o limite rígido de X kbps. Passou disso, é sumariamente descartado (Drop)".

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Imagine uma festa de fim de ano massiva.
*   O **CBWFQ** é a **Divisão Justa de Garçons**. As mesas normais ganham seus chopps com base no valor da mesa, mas todos esperam sua vez.
*   O **LLQ** é a **Sirene do Paramédico**. O paramédico (VoIP) entra primeiro na festa, jogando os garçons e os clientes normais para fora do caminho. O problema: se você deixar entrar 1.000 paramédicos sem freio (*Policer*), a festa acaba (Starvation da rede).
*   A **VOQ** é o **Aplicativo de Controle de Estacionamento**. Antigamente (Sem VOQ), os carros iam até a frente da boate para tentar estacionar; se a garagem estivesse cheia, eles trancavam a rua inteira, impedindo os moradores do bairro de passarem (HOLB). Com a VOQ, o carro só sai da garagem da sua casa (*Ingress Port*) se a garagem da boate (*Egress Port*) avisar pelo app: "Tenho uma vaga reservada, pode vir". A avenida principal (*Switch Fabric*) nunca sofre congestionamento cego.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A sintaxe de linha de comando exigida em um roteador de arquitetura Cisco (IOS/XE) via MQC (Modular QoS CLI) provando a diferença entre garantia justa (Bandwidth - CBWFQ) e monopólio rápido (Priority - LLQ):

```bash
! Define quem é quem no tráfego
class-map match-all VOIP-TRAFFIC
 match dscp ef
class-map match-all BACKUP-TRAFFIC
 match protocol ftp

! A Política implacável
policy-map ENTERPRISE_QOS
 class VOIP-TRAFFIC
  ! Aqui reside o LLQ: Fila prioritária com teto rígido de 100 Megabits (Policer natural)
  priority 100000 
 class BACKUP-TRAFFIC
  ! Aqui reside o CBWFQ: Garantia justa em % de banda sem prioridade na fila de saída
  bandwidth percent 20 

! Aplicação na interface
interface GigabitEthernet0/1
 service-policy output ENTERPRISE_QOS
````

5. História do Conteúdo

Historicamente, o QoS primitivo consistia em Filas FIFO (First-In, First-Out), onde os pacotes agiam de forma selvagem: a requisição de download de um vídeo de 40GB do servidor entrava na frente da ligação do CEO (VoIP) simplesmente por ter chegado 1 milissegundo antes, derrubando a voz dele. Com a invenção da telefonia digital nos anos 90, o LLQ foi forjado como um trator de prioridades e resolveu a latência. Na virada de 2010, quando os Datacenters e processamentos de Inteligência Artificial exigiram um _Throughput_ monstruoso de _Terabits_, os engenheiros constataram que filas simples de saída não acompanhavam a física, criando a infraestrutura VOQ fora dos chips tradicionais para absorver os gargalos do RoCE v2 (RDMA over Converged Ethernet).