---
tags:
  - afinidade/media
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/devsecops
---

### DevSecOps_Secrets_Scanning

#### 1. O Axioma (A Definição Rígida)
**O que é:** O *Secrets Scanning* é um motor de análise automatizada, frequentemente integrado às esteiras de CI/CD, projetado para vasculhar o código-fonte e o histórico do repositório em busca de credenciais vazadas, tokens de API e chaves criptográficas *hardcoded* antes que atinjam a produção.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Utiliza expressões regulares (Regex) e algoritmos de alta entropia para ler cada linha de código, *commit* ou arquivo de configuração em busca de padrões estruturais (ex: o formato exato de uma chave `AKIA...` da AWS ou um token JWT).
*   **O Problema que Resolve:** O maior e mais estúpido vetor de invasão da nuvem corporativa: o erro humano. Desenvolvedores costumam cravar senhas no código para testar a aplicação na própria máquina e, por desatenção, enviam essa bomba para o [[Ferramenta_GitHub]]. O scanner barra a submissão e quebra o *build*.
*   **Visão Sênior (Vulnerabilidades/Escala):** Operar o *scanner* apenas na nuvem (via GitHub Actions) já é tarde demais, pois o *commit* já foi registrado no histórico do Git e robôs de invasores ([[Cyber_OSINT]]) varrem repositórios públicos em milissegundos. A arquitetura sênior impõe o *scanning* local na máquina do desenvolvedor (via *pre-commit hooks*) impedindo fisicamente que a senha saia do laptop. Sofre cronicamente de fadiga por Falsos Positivos ao esbarrar em hashes inofensivos ou variáveis de ambiente falsas em testes de QA.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[DevSecOps_Secrets_Scanning]] é a **Revista de Bolsos na porta da Casa da Moeda**. O desenvolvedor fabricou o dinheiro perfeitamente (o código do software) e vai embora para casa. O segurança na catraca não avalia se o dinheiro foi bem impresso (o [[DevSecOps_SAST]] faz isso), ele apalpa o bolso do operário apenas para garantir que a **Chave Matriz do Cofre** não está saindo do prédio escondida na meia dele. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação open-source bruta usando o `trufflehog` ou `git-secrets` para travar o repositório se uma chave for encontrada:
```bash
# Rodando o TruffleHog para varrer todo o histórico do repositório em busca de segredos de alta entropia e chaves verificadas de provedores em nuvem
trufflehog git file:///home/dev/projeto_secreto --fail
````

5. História do Conteúdo

A prática explodiu na segunda metade da década de 2010. Com a adoção massiva do GitHub, criminosos criaram exércitos de _bots_ que ficavam permanentemente conectados às APIs do repositório público, apenas aguardando programadores cometerem erros. Se um desenvolvedor subisse uma chave da AWS acidentalmente, em 4 segundos a conta dele na nuvem era sequestrada e 100 servidores eram criados para minerar criptomoedas, gerando contas de US$ 50.000 da noite para o dia. A automação forçou a segurança a tratar segredos como lixo tóxico detectável.