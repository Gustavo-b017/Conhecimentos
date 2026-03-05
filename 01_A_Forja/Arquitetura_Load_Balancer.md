---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/4_evergreen
---

### Arquitetura_Load_Balancer
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Load Balancer (Balanceador de Carga) é um componente arquitetural de rede (hardware ou software) que distribui de forma eficiente o tráfego de entrada através de um pool de múltiplos servidores *backend*, garantindo escalabilidade e evitando a sobrecarga de um único nó.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O cliente manda a requisição para o IP público do Load Balancer. Ele usa algoritmos (como *Round Robin* - um para cada, de forma circular; ou *Least Connections* - mandar para o servidor menos ocupado no momento) para decidir para qual réplica do [[Arquitetura_Microsservicos|Microsserviços]] encaminhar o pacote. Ele checa constantemente a saúde dos servidores (*Health Checks*).
*   **O Problema que Resolve:** Aniquila o gargalo de processamento. Um único servidor tem limite físico de CPU/RAM. Se 100.000 usuários tentarem acessá-lo, ele cai. O Load Balancer permite adicionar 50 servidores fracos e baratos lado a lado, operando como uma única máquina superpoderosa para quem está de fora.
*   **Visão Sênior (Vulnerabilidades/Escala):** Se configurado de forma singela, o próprio Load Balancer vira o *[[Infra_SPOF|Single Point of Failure]]* (Ponto Único de Falha). Se ele queimar, as 50 máquinas atrás dele ficam perfeitamente saudáveis, mas invisíveis e inacessíveis para o mundo. Além disso, lidar com requisições que exigem "estado" (Sessões armazenadas no disco local de um servidor) quebra quando o Load Balancer manda o usuário para o Servidor B após ele ter feito login no Servidor A (exigindo soluções como "Sticky Sessions" ou cache distribuído via [[Conceito_Cache|Redis]]).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O Load Balancer é o **Gerente de Fila do Caixa de um Banco lotado**. O cliente não escolhe para qual caixa ir. O Gerente fica na frente das faixas e observa: "O Caixa 1 está demorando. O Caixa 2 acabou de ficar livre". Ele direciona o próximo cliente para o Caixa 2 (*Algoritmo de Least Connections*). Se o Caixa 3 tiver um colapso nervoso e for para o hospital (Falha no *Health Check*), o gerente imediatamente para de enviar clientes para aquele guichê, mantendo a operação do banco fluindo sem que os clientes do lado de fora percebam o caos (similar ao [[Arquitetura_API_Gateway|API Gateway]]).

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação de software Load Balancer mais famosa do mundo baseia-se no bloco `upstream` do [[Ferramenta_Nginx|Nginx]], roteando o tráfego para três portas internas via Round Robin simples:
```nginx
upstream meubackend {
    server 127.0.0.1:3001;
    server 127.0.0.1:3002;
    server 127.0.0.1:3003;
}
server {
    listen 80;
    location / {
        proxy_pass http://meubackend;
    }
}
````

5. História do Conteúdo

Surgiu na década de 1990 para salvar os gigantes da Web 1.0. Sistemas que rodavam grandes diretórios e motores de busca antigos estavam sendo bombardeados de tráfego e os melhores mainframes da IBM não aguentavam a carga. Engenheiros introduziram a "comutação de camada 4" para jogar os pacotes em dezenas de servidores Unix baratos empilhados, inventando o balanceamento de carga que formaria a fundação dos Data Centers modernos do Google e AWS.