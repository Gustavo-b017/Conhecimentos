---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/3_incubadora
---

### Arquitetura_Correlation_ID

#### 1. O Axioma (A Definição Rígida)
**O que é:** O *Correlation ID* (ID de Correlação) é um token alfanumérico único (geralmente um [[Conceito_UUID|UUID]]) gerado no instante em que a primeira requisição entra no ecossistema e que é compulsoriamente propagado pelos cabeçalhos de todos os saltos de rede e logs em uma arquitetura distribuída.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O usuário clica em "Comprar". O [[Cyber_Firewall_WAF]] gera o ID `550e8400-e29b`. Esse ID é repassado no *header* [[Rede_HTTP|HTTP]] para o [[Arquitetura_API_Gateway|API Gateway]] -> Serviço de Carrinho -> [[Ferramenta_Kafka|Kafka]] -> Serviço de Estoque. Cada vez que um desses sistemas emite um log ou uma mensagem de erro, eles escrevem o ID na frente do log.
- **O Problema que Resolve:** O "Caos Assíncrono" e os "Erros Cegos". Se o Serviço de Estoque lançar uma exceção de "Sem Saldo", sem um ID de correlação, é humanamente impossível descobrir qual dos 500 clientes que clicaram em "Comprar" no mesmo segundo causou o erro no final da fila.
- **Visão Sênior (Vulnerabilidades/Escala):** Injetar manualmente o Correlation ID em cada requisição *HTTP Client* do seu código polui a regra de negócio. Arquitetos utilizam padrões como o `MDC` (Mapped Diagnostic Context) no Java/SLF4J, ou delegam o rastreamento integralmente para ferramentas de Malha de Serviço ([[Arquitetura_Service_Mesh|Service Mesh]]) e observabilidade como o *OpenTelemetry* e o *Jaeger*.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Arquitetura_Correlation_ID]] é o **Número de Rastreio de um Pacote de Logística Internacional**. Quando a sua encomenda sai da China, ela ganha um código de barras. Ela vai passar por caminhões, navios, aviões e diferentes transportadoras terceirizadas no Brasil. Se o pacote for destruído num incêndio num galpão em Curitiba (Mensagem de Erro num Microsserviço), o fiscal não perde tempo; ele bate o leitor no código de barras que sobreviveu e sabe exatamente quem comprou o produto no dia 1 e qual rota a caixa fez até morrer.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação do Correlation ID num filtro de requisição inicial do Spring Boot para plugar no log estruturado:
```java
@Component
public class CorrelationIdFilter implements Filter {
    private static final String CORRELATION_ID_HEADER = "X-Correlation-Id";

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) {
        HttpServletRequest req = (HttpServletRequest) request;
        // Pega o ID que veio da rede, ou gera um novo se for a origem
        String correlationId = req.getHeader(CORRELATION_ID_HEADER);
        if (correlationId == null) {
            correlationId = UUID.randomUUID().toString();
        }
        // Coloca no contexto de log do Java (MDC)
        MDC.put("correlationId", correlationId);
        try {
            chain.doFilter(request, response);
        } finally {
            MDC.remove("correlationId"); // Higiene de thread
        }
    }
}
````

5. História do Conteúdo

A necessidade de correlação metódica nasceu da dor real na transição da arquitetura Monolítica para Microsserviços na última década. No Monolito, se ocorria um erro, bastava ler o único arquivo de log `.txt` gerado. Em sistemas modernos com 500 serviços independentes conectados por mensageria assíncrona, o tempo gasto tentando remontar a ordem causal de um erro sem um ID atrelado inviabilizava a depuração e levou a adoção de Rastreamento Distribuído (Distributed Tracing).