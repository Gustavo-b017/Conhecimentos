---
tags:
  - afinidade/media
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/devsecops
---

### DevSecOps_SAST

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Static Application Security Testing (SAST) é a análise estrutural da "caixa-branca" que varre o código-fonte, bytecode ou binários em repouso durante a fase de build para identificar padrões de vulnerabilidades e credenciais vazadas antes mesmo do software ser compilado ou executado.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O motor de análise lê o código (ex: Java, Python) procurando por fluxos de dados perigosos ou funções de biblioteca conhecidas por serem frágeis. Se você usar `md5()` em vez de um hash forte, ou não parametrizar uma query SQL, ele grita na mesma hora.
*   **O Problema que Resolve:** O "Shift-Left" puro. Encontrar um erro de arquitetura quando o código ainda está na máquina do desenvolvedor custa dez vezes menos (tempo e dinheiro) do que descobrir essa mesma falha quando o sistema já está na nuvem e o atacante o encontrou.
*   **Visão Sênior (Vulnerabilidades/Escala):** A falha mortal do SAST é a "Fadiga de Falsos Positivos". Como ele analisa texto morto sem entender o contexto da execução [1], ele vai disparar um alerta crítico sobre um dado "inseguro" que, na vida real, passaria por uma sanitização na camada do [[Arquitetura_API_Gateway]] que ele não enxerga. Analistas seniores não tentam zerar os alertas do SAST; eles criam "Quality Gates" rígidos apenas para os riscos inquestionáveis (como senhas *hardcoded*).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[DevSecOps_SAST]] é o **Revisor Ortográfico e Gramatical de um Livro**. Ele escaneia a página e aponta erros óbvios: "Você escreveu essa palavra errado", "Você usou uma vírgula onde não devia". Ele é vital e incansável. Contudo, o revisor gramatical não sabe se a história do livro é boa ou se faz sentido na prática (Falta de Contexto). Ele apenas garante que, quando você for enviar a carta pelo [[Rede_HTTP]], ela não tenha erros crassos que permitam um [[Cyber_Ataque_SQL_Injection]] ou [[Cyber_Ataque_XSS]].

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação moderna obriga o SAST a rodar dentro da esteira [[Rede_NetDevOps_CICD]] do GitHub Actions ou GitLab CI. Um exemplo executando a ferramenta `Semgrep` ou `SonarQube` via linha de comando para quebrar a compilação (Fail the Build) se houver falhas críticas:
```bash
# Rodando o SAST no diretório atual e forçando erro (exit 1) se houver vulnerabilidade High
semgrep scan --config "p/default" --error --severity ERROR ./src/
````

5. História do Conteúdo

Surgiu no final dos anos 1990 e início dos anos 2000, liderado por empresas como a Fortify. Na época, a segurança consistia em contratar engenheiros caros para ler milhares de linhas de código em busca de erros, um processo doloroso e humano. A necessidade corporativa de lançar softwares mais rápidos transformou a leitura humana em analisadores léxicos automatizados. O SAST cimentou o conceito fundacional de que "Segurança começa na IDE do programador, não no [[Rede_Firewall]]".