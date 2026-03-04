````
---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Infra_SPOF

#### 1. O Axioma (A Definição Rígida)
**O que é:** O *Single Point of Failure* (Ponto Único de Falha) é um erro arquitetural estrutural caracterizado por qualquer hardware, software ou link de rede cuja paralisação individual arrasta inevitavelmente todo o ecossistema corporativo para a inoperância.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Manifesta-se em topologias de gargalo. Se 500 microsserviços ágeis e independentes precisarem ler dados em um único banco de dados central Oracle, esse banco de dados é o SPOF.
- **O Problema que (Não) Resolve:** O design que contém SPOFs é atraente apenas por motivos financeiros a curto prazo: é muito mais barato manter um único servidor potente do que três servidores médios sincronizados.
- **Visão Sênior (Mitigação/Escala):** A engenharia madura aniquila o SPOF através da replicação matemática (Padrão N+1 ou 2N+1). Para sistemas de missão crítica, a infraestrutura deve ser espelhada em "Zonas de Disponibilidade" físicas diferentes para garantir que, se um data center incendiar, o balanceador de carga vire a chave para o data center B em milissegundos.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O SPOF é o **único gerador elétrico de uma UTI em um hospital de traumas**. Você pode ter 50 dos melhores cirurgiões do mundo (Sistemas modernos) operando nas melhores salas esterilizadas (Containers Isolados). Mas se existe apenas uma linha de energia conectando o hospital à rua, basta uma tempestade derrubar um único poste para matar todos os pacientes simultaneamente no meio das cirurgias.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A eliminação do SPOF declarada na infraestrutura (via Docker Compose). Um banco de dados Redis nunca roda sozinho em produção; ele exige réplicas para assumir a carga imediatamente se o *Master* queimar:
```yaml
services:
  redis-master:
    image: redis:alpine
    ports: ["6379"]
  
  redis-slave-1: # Eliminação do SPOF (Redundância N+1)
    image: redis:alpine
    command: redis-server --replicaof redis-master 6379

  redis-slave-2: # Resiliência Extrema (Redundância 2N+1)
    image: redis:alpine
    command: redis-server --replicaof redis-master 6379
````

5. História do Conteúdo

O conceito de "design para a falha" foi imposto pela aviação militar e exploração espacial na década de 1960 (NASA). O módulo lunar da Apollo possuía o conceito de _Triple Modular Redundancy_, onde 3 computadores executavam o cálculo simultaneamente para garantir que um transistor queimado pela radiação espacial não matasse a tripulação com um erro de trajetória. A TI moderna apenas importou a paranoia militar para proteger transações de cartão de crédito.