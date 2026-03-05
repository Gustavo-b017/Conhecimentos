---
tags:
  - tipo/conceito
  - contexto/dev/design
  - afinidade/alta
  - status/3_incubadora
---

### Design_SOLID

#### 1. O Axioma (A Definição Rígida)
**O que é:** SOLID é o acrônimo mnemônico de cinco princípios fundamentais de design [[Java_OOP|orientado a objetos]] (SRP, OCP, LSP, ISP e DIP) que governam a organização do código para torná-lo tolerante a mudanças, testável e fácil de manter em larga escala.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Cada letra exige uma disciplina de software:
    *   *S (Responsabilidade Única):* O código só tem um motivo para mudar.
    *   *O (Aberto/Fechado):* Expande-se o código criando novas classes, sem alterar as velhas.
    *   *L (Substituição de Liskov):* Subclasses não podem trair a lógica da classe pai.
    *   *I (Segregação de Interface):* Interfaces gigantes devem ser quebradas em interfaces menores.
    *   *D (Inversão de Dependência):* Dependa de abstrações, não de implementações de concreto.
*   **O Problema que Resolve:** O SOLID aniquila a "programação espaguete" e o código frágil, onde arrumar o sistema de faturamento na linha 200 quebra misteriosamente a tela de login na linha 500 devido ao [[Arquitetura_Acoplamento|acoplamento]] oculto e alta dependência.
*   **Visão Sênior (Vulnerabilidades/Escala):** O dogma absoluto do SOLID fragmenta o software em centenas de arquivos minúsculos que não fazem quase nada sozinhos. A "Inversão de Dependência" cega torna o debug doloroso, pois você entra numa Interface na IDE e não sabe imediatamente qual das 5 classes concretas está rodando aquele método em tempo de execução. O sênior sabe quando ignorar um princípio em favor da performance.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O SOLID funciona como a padronização das **Tomadas Elétricas e Eletrodomésticos**. A Inversão de Dependência (DIP) garante que a fiação na parede (Núcleo) não seja soldada direto na geladeira. Existe um buraco padronizado (Abstração/Interface). Isso cumpre o princípio Aberto/Fechado (OCP), pois você pode desconectar a geladeira velha e plugar uma TV nova (extensão) sem quebrar e refazer a parede (modificação do código existente).

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação brutal do Princípio da Responsabilidade Única (SRP).
```java
// ANTI-PADRÃO (Responsabilidade dupla - fere o SRP)
public class Empregado {
    public void calcularPagamento() { ... } // Regra financeira
    public void salvarNoBanco() { ... }     // Regra de infraestrutura
}

// PADRÃO SÊNIOR (Isolamento de responsabilidades)
public class CalculadoraPagamento {
    public void calcular(Empregado e) { ... }
}
public class EmpregadoRepository {
    public void salvar(Empregado e) { ... }
}
````

5. História do Conteúdo

Os cinco princípios não nasceram de uma única vez. Foram ensinados de forma isolada por diferentes matemáticos e engenheiros de software nas décadas de 1980 e 1990 (como o LSP criado por Barbara Liskov em 1987). Robert C. Martin (Uncle Bob) reuniu esses conceitos em seu clássico artigo "Design Principles and Design Patterns" em 2000. Mais tarde, Michael Feathers percebeu que as iniciais dos princípios formavam a palavra S.O.L.I.D., criando o acrônimo mais poderoso da engenharia de software moderna.