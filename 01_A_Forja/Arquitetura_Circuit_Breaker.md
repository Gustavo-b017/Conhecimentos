---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/4_evergreen
---

### Arquitetura_Circuit_Breaker
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Circuit Breaker (Disjuntor) é um padrão de design de resiliência que monitora chamadas entre [[Arquitetura_Microsservicos]] e corta proativamente a comunicação (abre o circuito) quando as falhas atingem um limite tolerável, evitando o colapso em cascata do sistema inteiro.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Opera como uma máquina de estados com três posições:
    *   **Fechado (Closed):** Tudo funciona. As requisições fluem.
    *   **Aberto (Open):** O serviço de destino deu *timeout* 5 vezes seguidas. O disjuntor "desarma". Todas as novas requisições falham instantaneamente sem nem tentar acessar o destino, poupando a CPU de quem chama.
    *   **Meio-Aberto (Half-Open):** Após um tempo (ex: 30 segundos), o disjuntor deixa passar *uma* requisição de teste. Se ela funcionar, ele fecha o circuito de volta; se falhar, ele abre de novo.
*   **O Problema que Resolve:** O inferno do Efeito Dominó. Se o Serviço de Estoque ficar lento (demorando 30 segundos para responder), o Serviço de Vendas que depende dele vai enfileirar chamadas. A memória RAM do Serviço de Vendas esgota e ele cai também, arrastando o [[Arquitetura_API_Gateway|Gateway]] e derrubando a empresa inteira por causa de um banco de dados lento.
*   **Visão Sênior (Vulnerabilidades/Escala):** A vulnerabilidade de um Circuit Breaker é a má calibração de *Timeouts*. Se o seu disjuntor desarma muito rápido, o sistema entra em pânico e degrada a experiência do usuário por causa de uma oscilação comum de rede. Além disso, quando o circuito abre, você precisa obrigatoriamente de uma *Fallback Function* (Plano B: devolver dados do [[Conceito_Cache|cache]] ou uma mensagem amigável), senão o erro 500 ([[Rede_HTTP_Status|Erro 500]]) continuará estourando na tela do cliente.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A [[Arquitetura_Circuit_Breaker]] é literalmente o **Disjuntor Elétrico da sua casa**. A TV, a geladeira e o chuveiro compartilham a mesma fiação. Se um raio atinge a rua, gerando uma sobrecarga letal, o disjuntor (o código) identifica a anomalia e "desarma" (corta a energia do quadro) instantaneamente. Você fica no escuro, mas a sua televisão de R$ 5.000 não queima. Na arquitetura de software, você prefere devolver um "Erro Temporário" rápido do que queimar a memória de todos os servidores.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação moderna no ecossistema Java ([[Java_SpringBoot|Spring Boot]]) costuma utilizar a biblioteca *Resilience4j*. A configuração não suja a regra de negócio, ela apenas "envelopa" o método de chamada HTTP:
```java
// O disjuntor vai abrir se a API do Banco falhar ou ficar lenta muitas vezes
@CircuitBreaker(name = "bancoExterno", fallbackMethod = "metodoPlanoB")
public [[Arquitetura_DTO|PagamentoDTO]] processarPagamento() {
    return restTemplate.getForObject("https://api.banco.com/pagar", [[Arquitetura_DTO|PagamentoDTO]].class);
}

// O Plano B executado instantaneamente enquanto o circuito está "Aberto"
public [[Arquitetura_DTO|PagamentoDTO]] metodoPlanoB(CallNotPermittedException ex) {
    return new [[Arquitetura_DTO|PagamentoDTO]]("Serviço indisponível. Seu dinheiro está seguro. Tente mais tarde.");
}
````

5. História do Conteúdo

Michael Nygard eternizou o termo no desenvolvimento de software em seu livro definitivo _Release It!_ (2007). Antes disso, engenheiros tratavam os erros da rede de forma ingênua usando apenas blocos "Try/Catch", tentando infinitamente forçar a barra contra servidores que já estavam agonizando e morrendo. O padrão provou que, em sistemas distribuídos sob a nuvem agressiva, aceitar a falha de forma graciosa é muito mais resiliente do que tentar combatê-la com força bruta.