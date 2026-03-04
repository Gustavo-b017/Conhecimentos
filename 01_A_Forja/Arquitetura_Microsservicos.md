---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/4_evergreen
---

### Arquitetura_Microsservicos
#### 1. O Axioma (A Definição Rígida)
**O que é:** Microsserviços é um estilo arquitetural que estrutura uma aplicação como uma coleção de pequenos serviços fracamente acoplados, altamente testáveis, modelados em torno de domínios de negócio e independentemente implantáveis.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O monolito (um único código gigante rodando em um servidor com um único banco de dados) é fatiado. O serviço de "Estoque" vira um projeto separado, com seu próprio banco de dados, que se comunica com o serviço de "Pagamento" exclusivamente via chamadas de rede (como [[Arquitetura_REST]] ou mensageria).
*   **O Problema que Resolve:** Agilidade e Escalabilidade de times. Em um monolito, 50 desenvolvedores trabalhando no mesmo código geram conflitos constantes, e o deploy demora horas. Com microsserviços, o time de Pagamentos faz deploy do seu código 10 vezes ao dia em sua linguagem preferida (ex: Go), sem medo de quebrar a tela de Login que é mantida por outro time em outra linguagem (ex: Node.js).
*   **Visão Sênior (Vulnerabilidades/Escala):** A complexidade não desaparece, ela apenas sai do código e vai para a infraestrutura. Você troca as chamadas de função locais pela letal latência de rede. Ocorre o pesadelo das "Transações Distribuídas": se o serviço de Pagamento aprova, mas a rede cai e o serviço de Estoque não recebe a baixa, o banco de dados fica corrompido (exigindo padrões complexos como *[[Arquitetura_Saga|Saga Pattern]]*). Monitorar bugs em 50 servidores separados exige obrigatoriamente a injeção do [[Arquitetura_Correlation_ID]].

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O Monolito é um **Hipermercado Gigante**: você acha tudo no mesmo lugar, mas se a fiação elétrica central fechar curto, a loja inteira fica às escuras e para de faturar. Os [[Arquitetura_Microsservicos]] formam uma **Rua de Comércio Local**: você tem a padaria, o açougue e a farmácia como negócios independentes. Se a padaria pegar fogo (Serviço fora do ar), o açougue continua vendendo carne normalmente. O cliente precisa andar pela rua para comprar nos três (Custo de Rede), mas a resiliência do bairro como um todo é indestrutível. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
A separação brutal de microsserviços se reflete diretamente na infraestrutura como código (IaC). No `docker-compose.yml` da empresa, eles sobem e caem de forma isolada:
```yaml
services:
  servico-carrinho:
    image: empresa/carrinho-node:latest
    ports: ["3000:3000"]
    depends_on: [ db-redis-carrinho ] # Banco exclusivo dele
  
  servico-faturamento:
    image: empresa/faturamento-java:latest
    ports: ["8080:8080"]
    depends_on: [ db-postgres-faturamento ] # Banco exclusivo dele
````

5. História do Conteúdo

Cunhado informalmente por arquitetos de software em um workshop em Veneza em 2011, o termo explodiu quando gigantes nativas da nuvem, como Netflix e Amazon, abriram seus laboratórios e mostraram como haviam superado o peso burocrático da [[Arquitetura_SOA]]. A Amazon (sob as ordens do infame mandato de API de Jeff Bezos) descobriu que a única forma de escalar a engenharia para milhares de desenvolvedores era forçar cada equipe a ser dona do seu próprio serviço do banco de dados à interface, comunicando-se apenas por redes