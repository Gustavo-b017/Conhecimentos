---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/3_incubadora
---

### Arquitetura_REST

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Representational State Transfer (REST) é um estilo arquitetural para sistemas distribuídos concebido para usar puramente as diretrizes fundamentais da Web (verbo HTTP e URIs), manipulando recursos de forma fluida e essencialmente *Stateless* (sem estado).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Abandona o peso de ações diretas (RPC). O mundo é modelado como "Recursos" através de URIs simples (`/clientes/1`). O cliente executa semânticas padronizadas do protocolo [[Rede_HTTP]] (GET para ler, POST para criar, PUT para alterar) manipulando arquivos enxutos (Geralmente no formato JSON).
- **O Problema que Resolve:** Exterminou a verbosidade, o processamento e a burocracia exigida pelos contratos XML/SOAP. Permitiu a ascensão de aplicações mobile e SPA (Single Page Applications) que exigiam comunicação ultrarrápida e consumo mínimo de banda da internet móvel.
- **Visão Sênior (Vulnerabilidades/Escala):** A falta de um contrato duro compulsório de fábrica (como o WSDL) cria o "Inferno da Quebra de Integração". Se a API mudar de `nome` para `nomeCompleto` na surdina, o front-end "crasha" em produção. O padrão exige blindagem por documentações geradas ativamente como Swagger/OpenAPI e forte governança de versionamento (ex: `api/v1/clientes`).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se o SOA era a Receita Federal burocrática, o REST é a **Logística Rápida de um Fast Food Drive-Thru**. O cardápio de opções (As URIs) está impresso na parede externa. O cliente simplesmente grita um verbo padronizado: "GET no Combo 1". O atendente não anota a vida inteira do cliente (é Stateless). Ele apenas monta a caixa leve e padronizada (O JSON), devolve pela janela cobrando a ação com um "200 OK" (Código de Status) e atende o próximo em milissegundos.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O payload brutalmente limpo do nível de rede de uma requisição REST madura (Nível 2), contendo o semáforo de status HTTP explícito sem a embalagem inútil do Envelope SOAP:
```http
GET /alunos/1 HTTP/1.1
Accept: application/json

HTTP/1.1 200 OK
Content-Type: application/json

{
  "id": 1,
  "nome": "João",
  "status": "ATIVO"
}
````

5. História do Conteúdo

Criado por Roy Fielding na sua icônica tese de doutorado no ano 2000. Sendo um dos autores do protocolo HTTP original, ele provou que tentar sobrepor envelopes burocráticos artificiais (SOAP) por cima da Web era ineficiente. A indústria corporativa o ignorou por quase 10 anos, apenas capitulando e adotando o seu modelo minimalista quando a explosão dos iPhones (Apps móveis) exigiu que os backends fossem infinitamente mais rápidos.