---
tags:
  - tipo/conceito
  - contexto/dev/front
  - afinidade/alta
  - status/3_incubadora
---

### Front_JSON

#### 1. O Axioma (A Definição Rígida)
**O que é:** JavaScript Object Notation (JSON) é um formato de intercâmbio de dados de texto plano, universalmente legível e de baixo peso, estruturado nativamente em pares de chave-valor e listas.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Ele serializa objetos complexos em strings, sendo completamente agnóstico de linguagem. Qualquer backend (Java, Python, Go) consegue fazer o *parsing* dessa string para objetos nativos em memória.
- **O Problema que Resolve:** Aniquilou a verbosidade extrema e o peso burocrático do [[DB_XML]], permitindo o surgimento de aplicações web e mobile velozes que consomem APIs em milissegundos.
- **Visão Sênior (Vulnerabilidades/Escala):** Como o JSON não possui validação de esquema nativa rígida, ele é o vetor perfeito para ataques de *Mass Assignment*. Se o backend não blindar a entrada com um [[Arquitetura_DTO]], o atacante pode injetar chaves extras não previstas (`"admin": true`) direto no banco de dados. Em escalas de Big Data, o custo de CPU para ler JSON em texto plano é ineficiente, exigindo formatos binários como Parquet ou Protobuf.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O JSON é como usar **Post-its** para passar informações em um escritório. É rápido, direto e sem burocracia: você escreve "Nome: João" e cola na mesa do colega. O [[DB_XML]], por outro lado, exige que essa mesma informação seja enviada dentro de um envelope timbrado, carimbado em cartório e com 3 páginas de jargões jurídicos para provar que o João é realmente o João.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O *payload* enxuto de um cliente trafegando na rede. Em arquiteturas modernas com Spring Boot, a biblioteca Jackson serializa a resposta para este formato nativamente:
```json
{
  "id": 1,
  "nome": "João",
  "email": "joao@byteshop.com",
  "ativo": true,
  "telefones": ["11999999999", "11888888888"]
}
````

5. História do Conteúdo

Popularizado por Douglas Crockford no início dos anos 2000. Na época, a comunicação assíncrona no navegador (AJAX) tentava usar XML, mas o processamento era tão pesado que travava as máquinas. Crockford percebeu que o navegador já sabia ler objetos JavaScript nativamente; ele simplesmente extraiu essa sintaxe e a declarou como um formato de dados universal, matando o monopólio do XML na web.