---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/media
  - status/4_evergreen
---

### Arquitetura_API_Gateway
#### 1. O Axioma (A Definição Rígida)
**O que é:** O API Gateway é um servidor de gerenciamento de tráfego (Layer 7) que atua como o único ponto de entrada (Single Point of Entry) para as requisições de clientes, roteando-as para os microsserviços internos corretos e consolidando lógicas transversais.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez do aplicativo mobile do usuário tentar adivinhar o [[Rede_IP]] e a porta de 20 [[Arquitetura_Microsservicos]] diferentes espalhados pela nuvem, o aplicativo chama apenas um endereço: `api.empresa.com/v1/compras`. O Gateway intercepta a chamada HTTP, verifica o token do [[Cyber_IAM]], traduz a rota e encaminha para o servidor interno escondido na [[Rede_LAN]] que processa as compras.
*   **O Problema que Resolve:** Anula o acoplamento do cliente com a topologia do backend e centraliza *cross-cutting concerns* (Segurança, Rate Limiting, SSL Termination, Logs). Sem ele, cada um dos 50 microsserviços da empresa teria que programar a própria validação de JWT e sua própria segurança [[Rede_HTTPS|HTTPS]].
*   **Visão Sênior (Vulnerabilidades/Escala):** Se configurado de forma burra, o API Gateway herda o exato mesmo problema do antigo [[Arquitetura_ESB]]: vira um Ponto Único de Falha (SPOF) e um gargalo de performance brutal. A Regra de Ouro é: *"Gateways devem ser burros quanto ao negócio e inteligentes quanto ao roteamento"*. Nunca coloque lógica de "se o cliente for VIP, dê desconto" dentro do Gateway. Para evitar o gargalo para diferentes plataformas, utiliza-se a variação **BFF (Backend for Frontend)**, criando um Gateway para o Mobile e outro para a Web.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Arquitetura_API_Gateway]] atua como a **Recepcionista Blindada de um Prédio Corporativo**. Você (o Cliente Web) entra no saguão e não pode simplesmente sair andando pelos corredores tentando achar a sala do contador. Você fala apenas com a Recepcionista. Ela checa sua identidade, te entrega o crachá e liga para o ramal interno, redirecionando você para o elevador exato. Se o contador mudar da sala 402 para a 501 amanhã (Mudança de IP interno do serviço), você não precisa saber; a Recepcionista atualiza a rota no caderno dela de forma transparente.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O mercado é dominado por Gateways maduros e ultrarrápidos escritos em C ou Go, como Kong, [[Ferramenta_Nginx|Nginx]] ou AWS API Gateway. Exemplo declarativo da anatomia de uma rota (Kong YAML) barrando acesso de clientes que passam do limite (Rate Limiting) antes de onerar a aplicação:
```yaml
routes:
  - name: rota_pagamentos
    paths:
      - /api/v1/pagamentos
    service: microsservico_pagamentos_interno
plugins:
  - name: rate-limiting
    config:
      minute: 60  # Protege o serviço interno contra DDoS de Camada 7
      policy: local
````

5. História do Conteúdo

A ascensão do API Gateway foi a resposta direta à "Ressaca dos Microsserviços" na década de 2010. Quando as empresas fatiaram seus sistemas, os desenvolvedores de Front-end começaram a sofrer colapsos nervosos tentando rastrear 300 APIs diferentes para renderizar uma única tela. Eles precisavam de uma "fachada" unificada (Facade Pattern) que empacotasse a desordem do back-end em uma interface civilizada e segura, consolidando-se como o padrão de design número 1 para bordas de sistemas distribuídos modernos.