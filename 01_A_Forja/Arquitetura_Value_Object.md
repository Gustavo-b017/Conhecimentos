---
tags:
  - tipo/conceito
  - contexto/dev/design
  - afinidade/alta
  - status/3_incubadora
---

### Design_Value_Object

#### 1. O Axioma (A Definição Rígida)
**O que é:** Um Value Object (Objeto de Valor) é um bloco de dados sem identidade formal e intrinsecamente imutável, usado para tipar fortemente atributos de negócio que devem obedecer a lógicas de validação internas antes de existirem no sistema.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de tipar o e-mail de um cliente como uma genérica `String email`, o arquiteto cria a classe formal `Email`. Na instanciação dessa classe, a regra de negócio checa a expressão regular (Regex). Se a formatação do e-mail for inválida, o próprio objeto aciona uma exceção e impede a criação. Como são imutáveis, para mudar um VO, você o descarta e cria outro novo.
*   **O Problema que Resolve:** Aniquila o padrão primitivo do "Primitive Obsession" (Obsessão Primitiva). Impede que dados logicamente corrompidos (um CPF com letras, um preço negativo) circulem ou existam na memória RAM do seu backend.
*   **Visão Sênior (Vulnerabilidades/Escala):** A fraqueza operacional é a alocação de lixo em memória (Garbage Collection). Como o objeto é imutável (você não pode dar "setNovoNome"), caso haja um loop atualizando milhares de valores de forma contínua, você estará destruindo e recriando milhares de objetos na RAM, o que ativará o coletor de lixo da linguagem (Garbage Collector), gerando pequenas travas de performance na execução.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A diferença entre a Entidade de domínio e um [[Design_Value_Object]] é a **Diferença entre a Monalisa de Da Vinci e uma Nota de 100 Reais**. A Monalisa é uma Entidade: só existe uma, ela tem um código único (ID). Se alguém pichar o rosto dela, o valor sofre mutação, mas ela continua sendo aquele quadro específico. Já a nota de 100 reais é um Objeto de Valor: não me importa o número de série dela, se eu der 100 reais ao caixa e ele me devolver outra nota diferente de 100 reais do caixa dele, o valor é absolutamente o mesmo e a igualdade estrutural está garantida, além de eu não poder mudar o valor dessa nota a caneta (imutabilidade).

#### 4. Pragmatismo Aplicado (Código e Implementação)
A fundação de um VO implementado para o [[Java_SpringDataJPA|Spring Data JPA]] via `@Embeddable` agrupa as validações que o banco não suporta estruturalmente, para ser "embutido" posteriormente na Entidade principal:
```java
@Embeddable
public class DocumentoCPF {
    @Column(name = "cpf", length = 11, nullable = false)
    private String valor;

    // O construtor é o único lugar de injeção e garante a Imutabilidade
    public DocumentoCPF(String valor) {
        if (valor == null || valor.length() != 11) {
            throw new IllegalArgumentException("CPF violado na raiz lógica");
        }
        this.valor = valor;
    }
    
    // Construtor vazio fechado exigido por bibliotecas ORM (Hibernate)
    protected DocumentoCPF() {} 
}
````

5. História do Conteúdo

A distinção estrita entre "Entidades" (que rastreamos) e "Objetos de Valor" (que apenas nos interessam pelo que são) foi popularizada na Bíblia do desenvolvimento complexo: o livro _Domain-Driven Design (DDD)_ de Eric Evans, no ano de 2003. Ele mudou a forma como os engenheiros mapeavam o mundo real para dentro da classe de um computador, impedindo que programadores usassem tipos rasos construídos de fábrica (como String ou Float) para dados comerciais estritamente exigentes (Dinheiro, Placa de Carro, Geofencing).