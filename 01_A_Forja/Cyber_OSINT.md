---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_OSINT
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Open Source Intelligence (OSINT) é a técnica de reconhecimento passivo focada em coletar e correlacionar informações sobre um alvo, sistema ou organização através de fontes públicas e abertas, operando sem realizar nenhuma interação direta com a infraestrutura da vítima.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de enviar pacotes suspeitos contra um [[Rede_Firewall]], o analista (ou atacante) extrai dados de registros públicos de [[Rede_DNS|DNS]], varreduras do [[Ferramenta_Shodan|Shodan]], repositórios esquecidos no [[Ferramenta_GitHub|GitHub]], redes sociais de funcionários e [[Dados_Metadados|metadados]] de PDFs públicos da empresa.
* **O Problema que Causa:** Para o atacante, resolve o problema da detecção precoce. O reconhecimento ativo dispara o alarme do [[Cyber_IDS]]. O OSINT mapeia a superfície de ataque no mais absoluto silêncio.
*   **Visão Sênior (Vulnerabilidades/Escala):** O volume de lixo digital é o gargalo. Profissionais juniores acumulam terabytes de dados irrelevantes. OSINT sênior não é sobre extrair dados, é sobre inteligência decisória. A vulnerabilidade aqui é organizacional: as empresas "sangram" informações confidenciais constantemente na internet sem perceber, tornando-se o próprio vetor do ataque.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_OSINT]] é o **espião sentado no café do outro lado da rua com um binóculo**. Ele não toca no vidro do banco para ver se o alarme toca, ele apenas anota o horário em que o carro-forte chega, pesquisa a marca do cadeado na internet e descobre o nome do gerente lendo o crachá de longe. Quando a invasão real ocorre, ela é rápida e cirúrgica, pois a planta do prédio já foi montada através de fofocas públicas e fotos vazadas.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O [[Google_Dorking]] é a técnica primária de OSINT. É o abuso de operadores avançados do motor de busca para achar arquivos indexados acidentalmente.
Exemplo de Dork para achar planilhas de senhas ou bancos de dados SQL expostos publicamente:
```text
# Encontra arquivos SQL contendo a palavra "password" indexados pelo Google
filetype:sql "password" | "pass" site:empresa-alvo.com
````

5. História do Conteúdo

Criado pelas agências de inteligência governamentais e militares durante a Segunda Guerra Mundial e a Guerra Fria. Muito antes dos computadores, as agências descobriram que ler e analisar os jornais locais e as transmissões de rádio abertas do país inimigo revelava 80% das estratégias militares deles, sem a necessidade de enviar espiões armados.