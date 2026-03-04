---
tags:
  - tipo/conceito
  - contexto/dev/java
  - afinidade/alta
  - status/3_incubadora
---

### Java_RestController

#### 1. O Axioma (A Definição Rígida)
**O que é:** A anotação `@RestController` é uma especialização do framework Spring que marca a classe como o ponto de entrada de requisições web, forçando matematicamente que todos os métodos retornem os dados serializados diretamente no corpo da resposta (geralmente em JSON), em vez de renderizar páginas HTML.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** É uma anotação de conveniência que aglutina `@Controller` e `@ResponseBody`. Quando uma requisição HTTP bate na URI definida (via `@RequestMapping`), o Spring delega a chamada ao método correto e usa uma biblioteca (como o Jackson) para transformar o objeto Java retornado (`ResponseEntity`) em uma string JSON antes de mandá-lo pela rede.
*   **O Problema que Resolve:** No passado, backends precisavam injetar dados em templates HTML na unha (JSP/Thymeleaf). O `@RestController` foca exclusivamente no tráfego de dados puros, permitindo que a mesma API sirva perfeitamente a um aplicativo de celular, um site em React ou um relógio inteligente.
*   **Visão Sênior (Vulnerabilidades/Escala):** O maior erro arquitetural de desenvolvedores júniores é a criação de "Fat Controllers" (Controladores obesos). O Controller **não deve** conter regra de negócio (if/else), **não deve** calcular preços e **não deve** acessar o banco de dados. A única função dele é receber o JSON, acionar a camada de `Service` e devolver a resposta. Colocar lógica no Controller destrói a testabilidade e fere o princípio SRP do [[Arquitetura_SOLID]].

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Java_RestController]] é o **Maitre (Recepcionista) de um restaurante 5 estrelas**. Ele fica na porta (a URI). Quando você chega e faz o pedido (Requisição HTTP), o Maitre não vai para a cozinha picar cebola. Se ele for picar cebola (Regra de Negócio), a fila na porta vai acumular e o restaurante quebra. O Maitre apenas anota o seu pedido em um papel padrão (O JSON), entrega ao Chef (O Service), pega a bandeja pronta (O DTO) e entrega para você com um sorriso (Status 200 OK).

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação enxuta de um controlador que apenas orquestra o tráfego e respeita a semântica, sem conhecer as entranhas do negócio:
```java
@RestController
@RequestMapping("/api/v1/produtos")
public class ProdutoController {

    private final ProdutoService service;

    public ProdutoController(ProdutoService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<ProdutoResponseDTO> criar(@RequestBody ProdutoRequestDTO request) {
        // O Controller não calcula nada, apenas repassa ao Service
        ProdutoResponseDTO resposta = service.salvarNovoProduto(request);
        // O Spring serializa automaticamente o DTO para JSON e retorna o código 201
        return ResponseEntity.status(HttpStatus.CREATED).body(resposta);
    }
}
````

5. História do Conteúdo

Adicionado na versão 4.0 do Spring Framework (2013). Foi a resposta vital da linguagem Java à explosão das "Single Page Applications" (SPAs) fomentadas por frameworks JavaScript como Angular e React. A web deixou de pedir páginas prontas ao servidor e passou a pedir apenas os "dados puros" para montar a tela no lado do cliente. O `@RestController` automatizou essa extração.