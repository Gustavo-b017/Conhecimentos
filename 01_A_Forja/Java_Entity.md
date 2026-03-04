---
tags:
  - tipo/conceito
  - contexto/dev/java
  - afinidade/alta
  - status/3_incubadora
---

### Java_Entity

#### 1. O Axioma (A Definição Rígida)
**O que é:** Uma Entidade (`@Entity`) é uma classe de domínio Java leve (POJO) cujos atributos são mapeados cirurgicamente para refletir a estrutura de colunas e linhas de uma tabela em um banco de dados relacional.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Através de anotações metadadas. `@Entity` avisa que a classe é gerenciada pelo banco. `@Table` define o nome do destino. `@Id` define a Chave Primária (PK) obrigatória, e `@GeneratedValue` automatiza a contagem do ID (Auto-Incremento).
*   **O Problema que Resolve:** Permite que dados que vivem de forma abstrata na memória do servidor ganhem estado físico e duradouro no disco (Persistência), sem a necessidade de converter cada variável manualmente para o formato SQL antes de enviá-los ao banco.
*   **Visão Sênior (Vulnerabilidades/Escala):** O crime arquitetural mais comum e letal nas empresas é usar a [[Java_Entity]] como o objeto de transporte na web. Se o programador expõe a Entidade direto no `Controller` HTTP em vez de isolá-la atrás de um [[Arquitetura_DTO]], ele abre a porta para um *Mass Assignment Attack*. O hacker intercepta o JSON, adiciona a chave secreta `"admin": true`, e o JPA salva o atributo injetado direto na tabela do banco, dando acesso total ao invasor. Entidades não cruzam a fronteira da rede; elas vivem trancadas no cofre.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Uma [[Java_Entity]] é a **Forma de Silicone para assar bolos**. A forma de silicone dita a estrutura rígida, o tamanho e a capacidade (O Schema da Tabela). Você pode preparar a massa crua (A Lógica Orientada a Objetos) como quiser, mas quando você despeja a massa dentro da forma e a coloca no forno (O comando `.save()` do banco de dados), a massa perde a flexibilidade e é eternizada no exato formato matemático desenhado pela Forma.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O mapeamento blindado de uma tabela, incorporando um [[Arquitetura_Value_Object]] (`@Embedded`) para não poluir a entidade com regras miúdas:
```java
@Entity
@Table(name = "clientes")
public class Cliente {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // O Banco gera o ID
    private Long id;

    @Column(nullable = false, length = 100) // Regra rígida do SQL
    private String nome;

    @Embedded // Agrega uma classe imutável (Value Object) para dentro desta tabela
    private Email email;

    // A especificação JPA exige, obrigatoriamente, um construtor vazio protegido.
    protected Cliente() {}
}
````

5. História do Conteúdo

Antes do Java 5 introduzir o recurso de "Anotações" em 2004, descrever como um objeto viraria uma tabela envolvia redigir aterradores e intermináveis arquivos XML (`hibernate.cfg.xml`). Um erro de digitação de uma letra no arquivo XML quebrava o sistema sem que o compilador avisasse. A anotação `@Entity` trouxe a configuração visual para perto do campo exato a que ela se refere, matando a configuração externa em texto morto.