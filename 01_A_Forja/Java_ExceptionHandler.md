---
tags:
  - tipo/conceito
  - contexto/dev/java
  - afinidade/alta
  - status/3_incubadora
---

### Java_ExceptionHandler

#### 1. O Axioma (A Definição Rígida)
**O que é:** O `@ExceptionHandler` (operando junto ao `@ControllerAdvice`) é o mecanismo do Spring Boot projetado para interceptar globalmente exceções não tratadas lançadas pelo núcleo da aplicação e formatá-las em um payload JSON semântico antes de atingirem o cliente.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Quando um `UsuarioNaoEncontradoException` é disparado na camada de `Service`, em vez do servidor quebrar e devolver um genérico e aterrorizante `500 Internal Server Error`, o `@ControllerAdvice` entra na frente, captura a exceção específica, monta um objeto `ErrorResponseDTO` e obriga a Camada de Apresentação a retornar o status correto (ex: `404 Not Found`).
- **O Problema que Resolve:** Elimina o uso caótico e espalhado de blocos `try/catch` vazados dentro dos `Controllers`. Padroniza o contrato de erro da API. Todos os erros da sua empresa terão o mesmo formato matemático (Data, Status, Mensagem, Caminho).
- **Visão Sênior (Vulnerabilidades/Escala):** O vazamento de *Stack Trace* é uma falha de segurança primária. Se o seu manipulador de exceções genéricas deixar o erro puro do banco de dados (ex: "Table 'usuarios' not found in SQL...") vazar no JSON de resposta, você acaba de fazer um favor a um invasor prestando reconhecimento gratuito (Information Disclosure) para um ataque de [[Cyber_Ataque_SQL_Injection]].

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Java_ExceptionHandler]] é a **Assessoria de Imprensa de uma corporação no meio de um escândalo**. Quando a fábrica explode por dentro (Ocorre a Exceção/Crash), os engenheiros gritam jargões e o caos se instaura. A Assessoria de Imprensa não deixa o diretor sujo de graxa dar entrevista direto ao público; ela intercepta o pânico, traduz o incidente para um comunicado oficial limpo, calmo e padronizado (O JSON de Erro), e o entrega aos jornais garantindo a manutenção da reputação do protocolo [[Rede_HTTP_Status]].

#### 4. Pragmatismo Aplicado (Código e Implementação)
A fundação de um manipulador global unificado (`ApiExceptionHandler.java` citado no esqueleto da Aula 6) formatando o caos:
```java
@ControllerAdvice
public class ApiExceptionHandler {

    // Quando o negócio gritar esta exceção, a classe atua
    @ExceptionHandler(RegraDeNegocioException.class)
    public ResponseEntity<StandardErrorDTO> handleRegraDeNegocio(RegraDeNegocioException ex, HttpServletRequest request) {
        StandardErrorDTO error = new StandardErrorDTO(
            Instant.now(),
            HttpStatus.UNPROCESSABLE_ENTITY.value(), // Status 422 preciso
            "Violação de Domínio",
            ex.getMessage(),
            request.getRequestURI()
        );
        return ResponseEntity.status(HttpStatus.UNPROCESSABLE_ENTITY).body(error);
    }
}
````

5. História do Conteúdo

Antes de anotações como `@ControllerAdvice` existirem (introduzidas no Spring 3.2), os desenvolvedores eram obrigados a poluir cada método de cada controlador com lógicas massivas e repetitivas de `try-catch`, ou a usar configurações rígidas baseadas em XML para rotear falhas para páginas HTML de erro. O conceito trouxe a interceptação transversal (AOP - Aspect-Oriented Programming) para a ponta dos dedos dos desenvolvedores REST.