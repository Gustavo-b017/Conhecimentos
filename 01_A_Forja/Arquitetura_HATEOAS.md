---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/media
  - status/3_incubadora
---

### Arquitetura_HATEOAS

#### 1. O Axioma (A Definição Rígida)
**O que é:** O *Hypermedia As The Engine Of Application State* (HATEOAS) representa o nível máximo e mais refinado (Nível 3) de maturidade arquitetural do design [[Arquitetura_REST|REST]], onde a resposta da [[Arquitetura_API|API]] injeta ativamente os links das próximas ações válidas que o cliente pode realizar com aquele recurso.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O frontend não precisa "hardcodar" (cravar no código) as URLs ou adivinhar a regra de negócio. Se ele dá um `GET` num recurso, o servidor retorna o dado + um bloco [[Front_JSON|JSON]] chamado `_links` (padrão HAL) informando que o cliente está autorizado, naquele estado, a acessar as rotas de `editar` ou `excluir`.
- **O Problema que Resolve:** Desacopla o Frontend do Backend. Se a URL de cancelamento mudar amanhã, o Frontend não quebra, pois ele apenas clica no botão fornecido dinamicamente na chave `href` vinda do servidor na hora da consulta.
- **Visão Sênior (Vulnerabilidades/Escala):** É amplamente aclamado na academia e brutalmente ignorado no mercado sênior de alta escala. O motivo? Custo de CPU. Calcular dinamicamente quais links o usuário X tem permissão de enxergar sobre o recurso Y para cada requisição que chega aumenta drasticamente a latência e o payload trafegado. Por isso, a grande maioria do mercado trava no "Nível 2" e usa cache agressivo.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O HATEOAS é o design de **um Jogo de Videogame Moderno com Interface Dinâmica**. Quando você (o cliente) entra em uma sala, você não precisa ler um manual PDF gigante (o [[Ferramenta_Swagger|Swagger]]/OpenAPI) para saber o que fazer. Se você olha para a porta, aparece na tela "Aperte X para abrir" (O Link HATEOAS fornecido pelo servidor). Se a porta estiver trancada pelo servidor, a opção do botão simplesmente não é enviada para a sua tela e você nem tem a chance de tentar uma ação que retornaria falha.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O padrão de saída utilizando a especificação estrita de *Hypertext Application Language* (HAL) para guiar o cliente:
```json
{
  "id": 1,
  "nome": "Joao",
  "status": "CADASTRADO",
  "_links": {
    "self":      { "href": "http://api.byteshop.com/alunos/1" },
    "editar":    { "href": "http://api.byteshop.com/alunos/1", "method": "PUT" },
    "excluir":   { "href": "http://api.byteshop.com/alunos/1", "method": "DELETE" }
  }
}
````

5. História do Conteúdo

Em 2008, o engenheiro Leonard Richardson olhou para a bagunça do mercado que dizia "fazer REST" e desenhou o _Richardson Maturity Model_ (RMM) como uma escada didática. Nível 0 era SOAP fantasiado; Nível 1 usava URIs; Nível 2 respeitava os Verbos e Status (O atual padrão mundial). O Nível 3, o HATEOAS, foi cunhado por Roy Fielding como a verdadeira definição matemática de REST. Ironicamente, a utopia de Roy se tornou "complexa demais" para startups modernas focadas puramente na entrega rápida de telas via React/Next.js.