---
tags:
  - tipo/conceito
  - contexto/dev/dados
  - afinidade/media
  - status/3_incubadora
---

### Dados_XML

#### 1. O Axioma (A Definição Rígida)
**O que é:** eXtensible Markup Language (XML) é uma metalinguagem de marcação estrita baseada em árvores hierárquicas, projetada para armazenar e transportar dados de forma formalmente validável através de esquemas matemáticos (XSD).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Utiliza tags de abertura e fechamento (ex: `<cliente>...</cliente>`) para encapsular dados. Suporta metadados complexos dentro da própria tag (atributos) e exige um *parser* validado para não quebrar a compilação.
- **O Problema que Resolve:** No passado, cada sistema fechado gravava arquivos de um jeito proprietário (binários ou posições fixas de texto). O XML forjou uma "pedra de roseta" universal legível por humanos e máquinas, sendo a fundação que permitiu a existência das integrações [[Arquitetura_SOAP]].
- **Visão Sênior (Vulnerabilidades/Escala):** A proporção de lixo estrutural (*overhead*) em relação ao dado real devora a largura de banda. Além disso, parsers XML são historicamente vulneráveis à injeção de [[Ferramenta_OWASP_ZAP|XXE]] (*XML External Entity*), onde o atacante usa entidades recursivas (Billion Laughs Attack) para expandir o XML na memória RAM até o servidor colapsar por exaustão.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O XML atua como a **Burocracia Alfandegária Internacional**. Você não pode simplesmente despachar uma caixa de ferramentas. Cada ferramenta deve estar em uma sub-caixa separada, rotulada, com um manifesto carimbado descrevendo o peso, o fabricante e a liga metálica, tudo dentro de uma caixa maior com selo do governo. Garante integridade absoluta na entrega, mas a lentidão do processo mata o comércio ágil, motivo pelo qual a internet migrou para o [[Front_JSON|JSON]].

#### 4. Pragmatismo Aplicado (Código e Implementação)
O peso estrutural exigido para enviar os mesmos dados que um [[Front_JSON|JSON]] simples. Note o uso de *namespaces* para validação do esquema de dados:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<ns:cliente xmlns:ns="http://byteshop.com/schemas">
    <ns:id>1</ns:id>
    <ns:nome>João</ns:nome>
    <ns:email>joao@byteshop.com</ns:email>
    <ns:ativo>true</ns:ativo>
    <ns:telefones>
        <ns:telefone>11999999999</ns:telefone>
    </ns:telefones>
</ns:cliente>
````

5. História do Conteúdo

Padronizado pelo [[Org_W3C|W3C]] em 1998, surgiu da necessidade de extrair o poder do [[Lang_SGML|SGML]] (uma linguagem de marcação colossal e militar da década de 80) e torná-lo utilizável via Web. Durante toda a década de 2000, o XML foi o "Santo Graal" das integrações, até ser esmagado pela cultura de velocidade exigida pelos aplicativos mobile.