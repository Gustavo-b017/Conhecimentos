---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/4_evergreen
---

### Arquitetura_Pub_Sub
#### 1. O Axioma (A Definição Rígida)
**O que é:** Publish/Subscribe (Pub/Sub) é um padrão de mensageria assíncrona onde os publicadores de mensagens (Publishers) não programam as mensagens para serem enviadas a receptores específicos; em vez disso, categorizam as mensagens em classes (Tópicos), sem saberem se existem assinantes (Subscribers) escutando.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Baseado no conceito de "Desacoplamento Espacial e Temporal" orquestrado por um *Message Broker* (como Kafka, RabbitMQ ou AWS SNS). O Serviço A (Vendas) cria um pedido e simplesmente atira no Broker a mensagem: "Pedido #123 Criado". Ele não fica esperando resposta. O Serviço B (Estoque) e o Serviço C (Envio de E-mail) assinam esse evento e reagem no seu próprio tempo de processamento.
*   **O Problema que Resolve:** Mata a fragilidade síncrona do [[Arquitetura_REST]]. Se a Venda fizesse um `POST` via REST direto no Estoque, e o Estoque estivesse fora do ar, o cliente na ponta receberia "Erro 500: Falha na Compra". Com Pub/Sub, se o Estoque cair, a mensagem fica segura na fila do Broker. Quando o Estoque religar horas depois, ele lê a fila atrasada e tira a diferença.
*   **Visão Sênior (Vulnerabilidades/Escala):** Arquiteturas baseadas em eventos introduzem a *Consistência Eventual* (o dado vai estar correto em todos os bancos, eventualmente, mas não no mesmo milissegundo). Isso gera pânico no time de negócios ("Vendi, mas não atualizou a tela!"). Outro risco letal é a falha no consumo de eventos: se a mensagem falhar múltiplas vezes, o sistema exige uma [[Arquitetura_Dead_Letter_Queue]] configurada, ou o Broker perderá a mensagem (Data Loss) ou entrará em loop eterno travando a fila (Poison Pill).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Arquitetura_Pub_Sub]] é literalmente o modelo de uma **Estação de Rádio (AM/FM)**. O radialista (Publisher) fala no microfone e joga o sinal no ar (Tópico no Broker). Ele não sabe os nomes de quem está ouvindo, não sabe onde moram, nem se têm 5 ou 50.000 aparelhos ligados (Desacoplamento Espacial). Os motoristas em seus carros (Subscribers) sintonizam na frequência 99.9 e consomem a música. Se o rádio do seu carro queimar (Serviço cai), a estação continua transmitindo normalmente sem se abalar.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação não ocorre na camada de rede (como no [[Rede_TCP]]), mas na camada de software integrada a um *broker*. Exemplo de lógica num serviço Node.js atuando como Publisher (Atirando a mensagem para o universo no protocolo AMQP do RabbitMQ):
```javascript
const amqp = require('amqplib');

async function notificarCompra(pedido) {
    const connection = await amqp.connect('amqp://broker_interno');
    const channel = await connection.createChannel();
    
    const topico = 'eventos.vendas.pedido_criado';
    
    // O sistema não exige confirmação se o Estoque recebeu, ele apenas emite.
    channel.publish(topico, '', Buffer.from(JSON.stringify(pedido)));
    console.log("Venda finalizada. O resto do sistema que lute para atualizar os dados.");
}
````

5. História do Conteúdo

Embora o termo e a lógica existam em discussões da Ciência da Computação desde meados de 1987 (nos anais do ACM Symposium), a aplicação violenta dessa arquitetura ganhou força comercial na transição da virada do milênio, liderada por agências de notícias e bolsas de valores (como a Reuters) que precisavam enviar as cotações financeiras que sofriam mutações a cada segundo para centenas de milhares de terminais diferentes no planeta simultaneamente. Fazer chamadas síncronas uma a uma de um servidor central teria derretido o hardware instantaneamente.