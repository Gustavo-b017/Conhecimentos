---
tags:
  - tipo/conceito
  - contexto/gov/gestao
  - afinidade/media
  - status/3_incubadora
---

### Gov_SLA

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Service Level Agreement (SLA) é um contrato matemático e juridicamente vinculativo que estipula o padrão inegociável de disponibilidade (*uptime*), latência e confiabilidade que um serviço de tecnologia deve entregar.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Baseia-se em métricas brutas. O provedor assina que entregará "99,99% de disponibilidade no mês". Se o monitoramento provar que o sistema caiu mais tempo que o permitido, gatilhos de multas financeiras ou devolução de créditos (Service Credits) são ativados.
- **O Problema que Resolve:** Elimina a subjetividade entre a TI e os acionistas. "O sistema está lento" não é uma métrica. O SLA força a engenharia a provisionar a infraestrutura exata para sustentar o contrato, nem mais, nem menos.
- **Visão Sênior (Vulnerabilidades/Escala):** A armadilha financeira do SLA são os "Nove Noves". Garantir 99,9% permite ~43 minutos de queda por mês. Garantir 99,999% (5 noves) permite apenas 26 segundos de queda. Passar de 3 para 5 noves não custa o dobro, custa 100 vezes mais, obrigando a adoção de data centers espelhados geograficamente ([[Rede_Redundancia]]) e a eliminação de qualquer [[Infra_SPOF]].

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O SLA é o **"Entregamos sua pizza em 30 minutos ou ela sai de graça"**. Não é uma promessa de marketing, é uma balança de risco atrelada a uma penalidade financeira real. Se a pizzaria (A Cloud) assina isso, o arquiteto deles é obrigado a comprar motos mais rápidas (ferramentas de [[Ferramenta_Nginx|Load Balancing]]) e ter cozinheiros extras ([[Rede_Redundancia]]). Se o motoboy chegar em 31 minutos, a multa é executada sem negociação.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O SLA de negócio dita a arquitetura do código. Se o contrato exige que a API responda em 500ms, injetamos padrões de *Timeout* e *[[Arquitetura_Circuit_Breaker|Circuit Breaker]]* no código Java para cortar a conexão no limite, evitando a violação do acordo:
```java
// O Fallback atua para não estourar o SLA de 500ms
@CircuitBreaker(name = "servicoPagamento", fallbackMethod = "pagamentoOffline")
@TimeLimiter(name = "servicoPagamento", fallbackMethod = "pagamentoOffline")
public CompletableFuture<String> processarTransacao() {
    return CompletableFuture.supplyAsync(pagamentoLegado::chamarBanco);
}
````

5. História do Conteúdo

Originou-se no setor de telecomunicações nas décadas passadas. As operadoras que instalavam links físicos caríssimos entre prédios (Leased Lines) precisavam garantir às empresas que o cabo não ficaria mudo. Quando a computação migrou para a nuvem pública (AWS, Azure), o SLA tornou-se o único documento que faz um banco confiar em rodar seus dados num computador que pertence a um terceiro.