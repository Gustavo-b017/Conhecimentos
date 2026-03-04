---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/alta
  - status/3_incubadora
---

### Arquitetura_Clean

#### 1. O Axioma (A Definição Rígida)
**O que é:** A Arquitetura Limpa (Clean Architecture) é um modelo de design estrutural focado na Separação de Interesses (Separation of Concerns), dividindo o software em camadas concêntricas independentes onde o núcleo das regras de negócio não sabe absolutamente nada sobre o mundo externo.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** É governada por uma lei inviolável: a *Regra de Dependência*, que dita que as dependências do código-fonte devem apontar exclusivamente para o centro. No núcleo estão as *Entidades* (regras puras) e *Casos de Uso* (orquestração). Nas bordas externas ficam a Interface de Usuário (Web) e a Persistência (Banco de Dados), tratadas como meros "detalhes" periféricos.
*   **O Problema que Resolve:** Elimina o acoplamento tecnológico destrutivo. Se a sua empresa decidir trocar o banco de dados da Oracle por MongoDB, ou o framework Spring por Quarkus, o núcleo de negócio permanece intacto e funcional, pois ele independe de agências externas.
*   **Visão Sênior (Vulnerabilidades/Escala):** A Arquitetura Limpa sofre de *Over-engineering* (excesso de engenharia) precoce. Exige a criação de dezenas de interfaces, mapeadores e DTOs para que a informação consiga atravessar as fronteiras sem quebrar a Regra de Dependência. Aplicar isso em um microserviço de CRUD simples destrói a produtividade do time e consome orçamento desnecessário.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A [[Arquitetura_Clean]] é o design rigoroso de um **Laboratório de Biossegurança Nível 4 (BSL-4)**. A pesquisa vital (O Núcleo/Entidades) fica no centro geográfico do prédio, isolada do mundo externo. Se um terremoto destruir a portaria (Mudança de Framework) ou se faltar água na rua (Queda do Banco de Dados), as portas de vácuo das camadas intermediárias trancam o laboratório central para que a amostra principal não seja contaminada.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A aplicação tática da regra de dependência. O *Caso de Uso* interno (Service) não pode invocar o Banco de Dados diretamente (isso apontaria a dependência para fora). Ele depende de uma Abstração (Interface).
```java
// Núcleo (Não conhece o Spring Data JPA ou SQL)
public interface UsuarioRepository {
    void salvar(Usuario usuario);
}

// Camada Interna (Caso de Uso)
public class CadastrarUsuarioUseCase {
    private final UsuarioRepository repository;
    // A implementação concreta será injetada aqui de fora para dentro (Inversão)
    public CadastrarUsuarioUseCase(UsuarioRepository repository) {
        this.repository = repository;
    }
}
````

5. História do Conteúdo

Criada por Robert C. Martin (Uncle Bob) em 2012, a Arquitetura Limpa não inventou a roda. Ela foi um esforço para unificar matematicamente dezenas de modelos de arquiteturas defensivas criados no início dos anos 2000 (como a _Hexagonal Architecture_ de Alistair Cockburn e a _Onion Architecture_ de Jeffrey Palermo), provendo um diagrama único e uma regra universal para guiar a imunidade do negócio em sistemas de missão crítica corporativos.