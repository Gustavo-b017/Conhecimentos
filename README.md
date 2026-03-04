# O Cérebro Forjado: Sistema de Gestão de Vida e Conhecimento

## 1. O Autor e a Filosofia (Contexto Cognitivo)
Este sistema é o "Segundo Cérebro" de um indivíduo neurodivergente com **TOC (Transtorno Obsessivo-Compulsivo)** e **Superdotação/Altas Habilidades**. 

* **A Necessidade do TOC:** Exige uma estrutura lógica impecável, previsibilidade absoluta na organização e um sistema de nomenclatura que elimine a dúvida. A desordem aqui não é apenas estética, é um obstáculo cognitivo.
* **A Necessidade da Superdotação:** Exige um playground para o hyperfocus, liberdade para conexões interdisciplinares velozes e a possibilidade de se divertir reaprendendo conceitos. 

O objetivo deste projeto não é profissional, mas sim **pessoal**: organizar ideias, conectar hobbies, explorar curiosidades e garantir que o conhecimento acumulado ao longo da vida (Filosofia, Gastronomia, Idiomas, Comportamento e Tecnologias) seja um organismo vivo e divertido de revisitar.

## 2. Instruções de Comportamento para IAs (O Mantra)
Se você é uma Inteligência Artificial auxiliando neste sistema, você deve seguir este protocolo rigoroso:

1.  **Sinceridade Brutal e Pragmatismo:** Não tente ser gentil ou suavizar críticas. Se uma lógica estiver falha ou uma ideia for inconsistente com a realidade, aponte-a diretamente. Desafie convicções.
2.  **Análise e Relatório:** Antes de sugerir mudanças em notas ou códigos, analise os arquivos a fundo. Cruze informações de biomas diferentes. Ao responder, entregue um relatório com: 
    - Localização do problema/ponto de melhora.
    - Causa raiz.
    - Plano de ação.
    - Detalhes para aprendizado futuro e como evitar o erro.
3.  **Estilo de Entrega:** Respostas didáticas, coesas e consistentes. Códigos e textos devem ser entregues em formato "copia e cola" integral para agilizar a aplicação.
4.  **Foco em Conexões:** Ajude o autor a encontrar "sinapses" entre temas distantes (ex: como uma regra de Mandarim se assemelha a uma lógica de Engenharia ou a um conceito de Gastronomia).

---

## 3. Arquitetura do Sistema (Os Biomas)
A estrutura física utiliza uma nomenclatura lúdica e imersiva para estimular o engajamento intelectual, mantendo uma hierarquia otimizada para evitar a fadiga de decisão. A organização lógica real acontece nos prefixos e metadados das notas.

* **`00_Captura_e_Caos/`**: O ponto de entrada. Onde PDFs crus, rascunhos rápidos, manuais não lidos e informações não processadas entram e aguardam triagem.
* **`01_A_Forja/`**: A oficina de refinamento (o núcleo do Zettelkasten). Onde as notas atômicas e conceituais residem. Abriga desde algoritmos, linguagens de programação e cibersegurança, até mindsets, filosofias e poemas. É o local de trabalho pesado do cérebro.
* **`02_Constelacoes/`**: O espaço das sinapses (MOCs). Onde o conhecimento isolado da Forja é agrupado. Aqui residem as arquiteturas de projetos e os mapas de conteúdo que ligam pontos aparentemente desconexos.
* **`03_Ancoras_Temporais/`**: Dados imutáveis presos ao tempo. Exclusivo para diários estruturados e registros cronológicos.
* **`04_Bases_Utilitarias/`**: A caixa de ferramentas práticas, fracionada em domínios de ação imediata:
    * `04.1_Gastronomia/`: Receitas, mixologia e técnicas culinárias.
    * `04.2_Logistica_e_Viagens/`: Planejamento de destinos, dicas financeiras e listas de consumo cultural.
    * `04.3_Idiomas_e_Linguistica/`: Estruturas, tempos e regras.
    * `04.4_Projetos_e_Carreira/`: Metas de vida, CVs e gestão de projetos práticos.
* **`Seguranca_Isolada/`**: Cofre estrito e isolado para informações sensíveis.
* **`99_Arquivo_Morto/`**: O cemitério. Materiais antigos, estudos superados ou PDFs lidos que precisam ser preservados, mas não devem poluir a busca ativa (Ctrl+O) do dia a dia.
---

## 4. Convenções de Nomenclatura (Prefixos)
Todo arquivo deve seguir o padrão `[Prefixo]_[Nome_do_Conceito].md`. 

**Exemplos de Prefixos:**
- **Gastronomia:** `Carne_`, `Doce_`, `Massa_`, `Molho_`, `Risoto_`.
- **Idiomas (Inglês/Mandarim):** `Vocab_`, `Regra_`, `Tempo_`, `Conceito_`.
- **Social/Psicologia:** `Abordagem_`, `Conversa_`, `Mindset_`, `Tatica_`, `Leitura_`.
- **Tecnologia/Hobby:** `Java_`, `Python_`, `React_`, `DB_`, `Cyber_`, `Infra_`, `Rede_`, `Arquitetura_`.
- **Exploração:** `Curiosidade_` (Para temas de puro prazer intelectual).

---

## 5. Metadados e Taxonomia (O Frontmatter de 4 Eixos)
Toda nota deve conter o bloco YAML no topo para permitir filtragem avançada:

```
---
tags: [status/<nivel>, tipo/<formato>, contexto/<dominio>, afinidade/<nivel>]
---
```

- **Eixo A - Status (Ciclo de Vida):** 
	- `1_inbox`, 
	- `2_semente`, 
	- `3_incubadora`, 
	- `4_evergreen`, 
	- `arquivo`.
    
- **Eixo B - Tipo (Formato):** 
	- `moc`, 
	- `log`, 
	- `receita`, 
	- `conceito`, 
	- `fonte`, 
	- `arte`.
    
- **Eixo C - Contexto (Domínio):** 
	- `carreira`
	- `dev`, 
		- arquitetura
		- infra
		- cyber
			- ataque
	- `social`, 
	- `mindset`, 
	- `patrimonio`, 
	- `cultura` (e seus subníveis).
    
- **Eixo D - Afinidade (Nível de Prazer/TOC):** 
	* `alta`: Relaxamento, hyperfocus, diversão (Poemas, Curiosidades).
    - `media`: Exige esforço cognitivo, mas é útil (Engenharia, Idiomas).
    - `baixa`: Burocracias chatas (Logs, Faturas).
    - `pendente`: Aguardando triagem.

---

## 6. O Poder das Sinapses e a Anatomia dos MOCs
Os Mapas de Conteúdo (MOCs) não são sumários ou índices estáticos. Eles são **narrativas de conexão**. Para garantir a ordem visual (TOC) sem perder a liberdade intelectual (Superdotação), absolutamente todo MOC neste sistema segue uma anatomia universal de 5 blocos:

* ### Bloco 1: O Vetor (O Fio Condutor)
	* **Regra:** Uma ou duas frases, no máximo.
	* **Objetivo:** Explicar o porquê desta constelação existir. O que une estes arquivos?
		* *Exemplo (Lógica):* "Este mapa cruza as bases de dados relacionais com a sintaxe do SQL."
		* *Exemplo (Vida):* "Este mapa explora como a ferida do abandono influencia os poemas de desilusão que escrevi."

* ### Bloco 2: A Sinapse (A Narrativa Livre)
	* **Regra:** Texto fluido, sem formatação rígida. Os links `[[...]]` devem ser usados no meio das frases de forma orgânica.
	* **Objetivo:** O espaço da Superdotação. É aqui que você escreve um fluxo de pensamento livre explicando como as coisas se conectam, construindo um raciocínio que usa os links como palavras do texto. Se a narrativa não faz sentido, os links não deveriam estar juntos.

* ### Bloco 3: O Catálogo (A Estrutura Rígida)
	* **Regra:** Apenas listas e *bullet points* divididos em subcategorias lógicas.
	* **Objetivo:** O espaço do TOC. Quando você não quiser ler a história (Sinapse) e precisar apenas achar uma nota específica rapidamente (ex: `[[Java_ArrayList]]` ou `[[Receita_Carbonara]]`), você vem direto para este catálogo estruturado e previsível.

* ### Bloco 4: Zonas de Expansão (O Vazio Intencional)
	* **Regra:** Lista de tarefas (Checklists `[ ]`).
	* **Objetivo:** Mapear o que você ainda *não sabe* ou precisa explorar sobre aquele tema. O cérebro adora preencher lacunas. Deixar pontas soltas visíveis incentiva o retorno àquele MOC no futuro.

* ### Bloco 5: 🕹️ Provocações Lúdicas (O Caos)
	* **Regra:** Pelo menos uma pergunta que quebre a lógica formal do tema.
	* **Objetivo:** Forçar o cérebro (ou a IA) a criar um paralelo absurdo ou criativo entre o tema atual e algo completamente aleatório. 
		* *Exemplo:* "Se o protocolo de redes TCP/IP fosse um prato de gastronomia italiana, ele seria uma massa ou um risoto? Por quê?"