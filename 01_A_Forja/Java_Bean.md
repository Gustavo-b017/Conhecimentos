---
tags:
  - tipo/conceito
  - contexto/dev/java
  - afinidade/media
  - status/3_incubadora
---

### Java_Bean

#### 1. O Axioma (A Definição Rígida)
**O que é:** Um Bean é qualquer objeto que seja instanciado, montado e gerenciado ativamente de ponta a ponta pelo [[Java_IoC|contêiner IoC]] do framework [[Java_SpringBoot|Spring]].

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Quando a aplicação sobe, o Spring varre o projeto procurando classes marcadas com anotações de "Stereotypes" (`@Component`, `@Service`, `@Repository`, [[Java_Rest_Controller|@Controller]]). Ele cria uma cópia dessas classes na memória RAM e as cataloga em sua tabela interna como Beans.
*   **O Problema que Resolve:** Evita que o desenvolvedor crie vazamentos de memória (Memory Leaks) e permite o reaproveitamento máximo de instâncias através da aplicação, abstraindo a gestão do ciclo de vida da linguagem.
*   **Visão Sênior (Vulnerabilidades/Escala):** O perigo invisível do Bean é o seu "Escopo" (Scope). Por padrão, todo Bean do Spring é *[[Design_Pattern_Singleton|Singleton]]* (existe apenas UMA única instância na memória para todos os usuários). Se um desenvolvedor júnior declarar uma variável de "estado" mutável (ex: `String ultimoCliente`) dentro de um Bean Singleton, quando dois clientes acessarem a API ao mesmo tempo, ocorrerá uma *Race Condition* letal, e um cliente sobrescreverá os dados do outro. Beans devem ser obrigatoriamente sem estado (`Stateless`).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Um [[Java_Bean]] é **o ator contratado sob demanda em um set de filmagens**. O Spring é o Diretor de Elenco. Se você marca uma classe com `@Component`, você diz ao diretor: "Contrate este cara". A partir desse momento, a vida dele pertence ao estúdio (O Contêiner). O diretor diz a ele a que horas acordar (Instanciação), em qual cena atuar (Injeção de Dependência) e, no fim das filmagens, o estúdio termina o contrato dele (`@PreDestroy` e Garbage Collection). 

#### 4. Pragmatismo Aplicado (Código e Implementação)
Além do escaneamento automático por `@Service`, o desenvolvedor pode forçar manualmente a criação de um Bean em uma classe de configuração (útil para bibliotecas externas que você não pode alterar o código):
```java
@Configuration
public class AppConfig {
    
    // O Spring executará este método e guardará o objeto retornado como um Bean
    @Bean
    public EmailGateway emailGateway() {
        return new EmailGateway("smtp.empresa.com");
    }
}
````

5. História do Conteúdo

Na arquitetura Java clássica dos anos 90, o termo "JavaBean" significava apenas uma classe burra que seguia a convenção de ter um construtor vazio, getters e setters. O Spring sequestrou a terminologia. No ecossistema moderno do Spring, a palavra "Bean" abandonou o seu sentido de encapsulamento raso e passou a definir exclusivamente "A unidade funcional viva sob a ditadura do Contêiner IoC".