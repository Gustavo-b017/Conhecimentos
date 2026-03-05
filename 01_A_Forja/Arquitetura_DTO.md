---
tags:
  - tipo/conceito
  - contexto/dev/design
  - afinidade/alta
  - status/3_incubadora
---

### Design_DTO

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Data Transfer Object (DTO) é um padrão de design que dita o uso de objetos puros (POJOs), desprovidos de inteligência de negócio, usados exclusivamente para transportar blocos de dados de forma segura e rápida através de fronteiras de rede ou de camadas de aplicação.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de retornar a Entidade ([[Java_Entity]]) inteira do Banco de Dados para o usuário via [[Arquitetura_REST|API REST]], você mapeia apenas os campos necessários dessa Entidade para um DTO de Resposta (ex: esconde a senha, mostra o nome). No sentido inverso (Request), o DTO atua como uma barreira de entrada antes do dado cru chegar ao sistema.
*   **O Problema que Resolve:** Impede dois problemas letais corporativos:
    1.  *Over-fetching:* Trafegar dados demais pela rede (ex: retornar a foto inteira em base64 num endpoint de listagem de nomes).
    2.  *Mass Assignment:* Um atacante intercepta o [[Front_JSON|JSON]] do Frontend, insere o campo malicioso `"admin": true` no meio, e como a sua API recebe a Entidade direto no banco, ele sobrescreve a tabela interna ganhando acesso. O DTO barra campos não esperados.
*   **Visão Sênior (Vulnerabilidades/Escala):** A complexidade não está no objeto, está na "tradução". Converter 100 mil Entidades para 100 mil DTOs através de código manual com "getters" e "setters" cria gargalo de CPU. Bibliotecas de reflexão ou mapeamento automático (como o ModelMapper em Java) são estritamente necessárias para compilar esse mapeamento em tempo de build, economizando processamento e código sujo.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Design_DTO]] é a **Bandeja de Plástico da Refeição do Hospital**. O cozinheiro (Camada de Dados) faz a comida na panela de aço gigante (A [[Java_Entity|Entidade]] mapeada no Banco). Você não envia a panela inteira pelo corredor até o quarto do paciente (A Interface Web); a panela é pesada e perigosa (Over-fetching e Falta de Segurança). O enfermeiro (O [[Java_Rest_Controller|Controlador]]) extrai apenas a porção correta do purê da panela, a deposita em uma bandeja descartável de plástico leve (O DTO) e a entrega.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação explícita usando as anotações do framework Lombok no Java para evitar a escrita de getters/setters e a exposição da entidade.
```java
// O DTO blinda a aplicação: O JSON que entra ou sai NUNCA mostrará campos sigilosos
@Data
@AllArgsConstructor
public class ClienteResponseDTO {
    private Long id;
    private String nomeCompleto;
    private String email;
    // O campo 'senha' que existe na Entidade do Banco de Dados não existe aqui
}
````

5. História do Conteúdo

Surgiu e foi popularizado por Martin Fowler no seu livro "Padrões de Arquitetura de Aplicações Corporativas" (PEAA). Foi criado primariamente nos tempos antigos dos sistemas de processamento remoto como EJB (Enterprise JavaBeans), onde cruzar a fronteira de um servidor para outro em uma rede exigia recursos gigantescos. Agrupar dezenas de propriedades menores em um único objeto de transferência de bloco (o DTO) economizava ciclos preciosos de CPU em sistemas legados lentos.