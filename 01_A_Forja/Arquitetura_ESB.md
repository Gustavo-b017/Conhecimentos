---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/3_incubadora
---

### Arquitetura_ESB

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Enterprise Service Bus (ESB) é o middleware centralizador da [[Arquitetura_SOA]]que intercepta todas as mensagens trocadas na rede corporativa para realizar roteamento lógico, orquestração, tradução de protocolos e imposição de segurança.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O consumidor (Ex: Aplicativo Mobile) nunca chama o provedor de serviço (Ex: Banco de Dados de Produtos) diretamente. Ele chama o ESB. O ESB lê a mensagem, valida o cabeçalho criptográfico ([[Cyber_IAM]]), traduz a mensagem de [[Front_JSON|JSON]] para [[DB_XML|XML]] (se o destino for um sistema legado) e despacha a requisição para o servidor correto.
- **O Problema que Resolve:** Remove a complexidade de rede e segurança de dentro do código da aplicação. O desenvolvedor do frontend não precisa saber onde o servidor de produtos está ou qual protocolo ele usa; o ESB atua como um tradutor universal mágico.
- **Visão Sênior (Vulnerabilidades/Escala):** O ESB é o mais letal *[[Infra_SPOF|Single Point of Failure]]* (Ponto Único de Falha) da engenharia clássica. Como *todo* o tráfego da empresa passa por dentro deste único barramento de software, se o ESB travar por falta de memória ou erro de CPU, a empresa inteira (RH, Vendas, Estoque) sai do ar instantaneamente. Mantê-lo exige times dedicados e hardwares monstruosos.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se a rede [[Rede_Modelo_TCPIP]] é a malha de estradas, o [[Arquitetura_ESB]] é uma **Única Rotatória Gigante no centro de Nova York** por onde absolutamente todos os carros, ambulâncias e caminhões de lixo da cidade são obrigados a passar para chegar em qualquer bairro. No centro da rotatória fica um policial (A lógica do ESB) que para cada carro, confere o documento e diz para qual saída ele deve ir. A orquestração é linda no papel, mas no horário de pico, a rotatória causa um congestionamento catastrófico.

#### 4. Pragmatismo Aplicado (Código e Implementação)
No ESB, o código de negócio (If/Else) é arrancado do Java e injetado nas ferramentas do Middleware (como Apache Camel ou IBM Integration Bus). Exemplo de roteamento lógico de um ESB escrito em XML (Route Builder):
```xml
<!-- Se a requisição vier do App Mobile, roteia para o Servidor Moderno, 
     se for do Backoffice antigo, roteia para o Mainframe Legado -->
<route id="roteamento-vendas">
    <from uri="http:0.0.0.0:8080/api/vendas" />
    <choice>
        <when>
            <simple>${header.origem} == 'MOBILE'</simple>
            <to uri="http://servidor-moderno:8081/vendas" />
        </when>
        <otherwise>
            <to uri="jms:queue:mainframe_legado" />
        </otherwise>
    </choice>
</route>
````

5. História do Conteúdo

O conceito de ESB não nasceu de uma teoria acadêmica limpa, mas do desespero corporativo dos anos 2000. As empresas haviam comprado a ideia do SOA, mas perceberam que conectar 500 serviços diferentes exigiria que os desenvolvedores programassem a lógica de roteamento em cada um deles repetidamente. A indústria de software empacotou o padrão EAI (Enterprise Application Integration) em um único super-servidor de prateleira e chamou de ESB. Ironicamente, sua complexidade estranguladora forçou a indústria anos depois a abraçar a descentralização radical dos [[Arquitetura_Microsservicos|Microsserviços]] e do [[Arquitetura_REST]].