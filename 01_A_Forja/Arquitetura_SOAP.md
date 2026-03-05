---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/3_incubadora
---

### Arquitetura_SOAP

#### 1. O Axioma (A Definição Rígida)
**O que é:** O SOAP (Simple Object Access Protocol) é um protocolo rígido e padronizado pelo W3C para troca de mensagens estruturadas exclusivamente em **[[DB_XML|XML]]**, exigindo contratos estritos para garantir a comunicação padronizada entre sistemas corporativos heterogêneos.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Toda requisição e resposta é obrigatoriamente empacotada em um "Envelope" XML (contendo `Header` e `Body`). O formato exato que essa mensagem deve ter é ditado por um contrato inviolável chamado **WSDL** (Web Services Description Language), que atua como o manual de instruções técnico do serviço e permite a geração automática de código cliente.
- **O Problema que Resolve:** Em ecossistemas legados, garantiu interoperabilidade com segurança de nível militar através da família de padrões embutidos `WS-*` (como o `WS-Security` para criptografia ponta a ponta e tokens SAML), fornecendo ferramentas de auditoria e governança necessárias para o cumprimento matemático de **[[Gov_SLA|SLA]]** (Service Level Agreement).
- **Visão Sênior (Vulnerabilidades/Escala):** A verbosidade do **XML** gera um *overhead* de rede e processamento gigantesco e inescalável quando comparado à leveza do **[[Front_JSON|JSON]]** utilizado em arquiteturas [[Arquitetura_REST|REST]] modernas. Além disso, a arquitetura SOAP em larga escala é operada de forma dependente sobre um **[[Infra_Middleware|Middleware]]** orquestrador corporativo (como o ESB rodando Apache Camel), que concentra todo o tráfego e inevitavelmente se converte no mais letal ***[[Infra_SPOF|Single Point of Failure]]* (Ponto Único de Falha)** da topologia.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Consumir uma API [[Arquitetura_REST|REST]] baseada em **JSON** é como pedir um café rápido no balcão de uma lanchonete sem burocracia. Já o protocolo [[Arquitetura_SOAP]] é como despachar material radiativo internacionalmente: você não pode simplesmente enviar a caixa; é obrigatório preencher e registrar um formulário alfandegário de 50 páginas (o contrato **WSDL**), isolar os dados dentro de um cofre blindado estruturado (o Envelope **XML**) e selar fisicamente com carimbos governamentais (`WS-Security`). Todo esse peso burocrático não viaja direto para o destino, ele passa compulsoriamente por uma agência central alfandegária (o **middleware** ESB), que garante o **SLA** da entrega. A falha fatal ocorre no estrangulamento da rede: se a agência central parar ou sofrer pane, o comércio do país inteiro colapsa simultaneamente (*Single Point of Failure*).

#### 4. Pragmatismo Aplicado (Código e Implementação)
A brutal diferença de custo em banda de rede e processamento na Camada de Aplicação. O que em REST/JSON seria um pacote leve de `{"cpf": "12345678901"}`, no SOAP exige um *parsing* pesado roteado pelo middleware. Exemplo do *payload* trafegando na rede:

```xml
POST /BillingService HTTP/1.1
Host: api.exemplo.com
Content-Type: text/xml; charset=utf-8
SOAPAction: "urn:ConsultarFatura"

<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"
               xmlns:bil="http://exemplo.com/billing">
   <soap:Header>
       <!-- A segurança (SAML/X.509) e roteamento entram embutidos na própria mensagem -->
       <wsse:Security xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
           <wsse:UsernameToken>
               <wsse:Username>sistema_rh</wsse:Username>
               <wsse:Password>token_opaco_estrito</wsse:Password>
           </wsse:UsernameToken>
       </wsse:Security>
   </soap:Header>
   <soap:Body>
      <bil:ConsultarFaturaRequest>
         <bil:cpf>12345678901</bil:cpf>
         <bil:mes>2025-07</bil:mes>
      </bil:ConsultarFaturaRequest>
   </soap:Body>
</soap:Envelope>
````

5. História do Conteúdo

Concebido no final de 1998 (inicialmente com o apoio da Microsoft) para resolver um problema físico de rede. Tecnologias de chamadas remotas corporativas da época (como CORBA ou DCOM) operavam em formato binário e utilizavam portas dinâmicas, esbarrando implacavelmente no bloqueio dos firewalls perimetrais (Camada 4). O protocolo SOAP foi criado para usar o texto plano em XML encapsulado dentro da porta 80 (HTTP), servindo como um "Cavalo de Troia" lícito para atravessar os firewalls e conectar sistemas heterogêneos. Anos depois, sua burocracia forçou a indústria a migrar para a fluidez do REST.