---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Cyber_DLP

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Data Loss Prevention (DLP) é uma estratégia e tecnologia de software projetada para detectar potenciais violações de dados, monitorar exfiltrações e impedir que informações sensíveis sejam enviadas, copiadas ou destruídas por usuários não autorizados

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O DLP inspeciona ativamente o conteúdo dos arquivos nas três fases da informação: Dados em Uso (monitorando a máquina do usuário), Dados em Trânsito (inspecionando anexos de e-mail e tráfego de rede) e Dados em Repouso (varrendo bancos de dados e servidores em nuvem). Ele usa Expressões Regulares (Regex) e análise léxica para procurar padrões como CPFs, números de cartão de crédito ou marcas d'água de documentos confidenciais, bloqueando a transferência caso as regras não sejam cumpridas.
*   **O Problema que Resolve:** Resolve a prevenção de fraude e a Ameaça Interna (*Insider Threat*) exigida em sala de aula. Mesmo que o usuário seja legítimo e possua credenciais do [[Cyber_IAM]], o DLP impede que ele copie o banco de dados inteiro da empresa para um Pendrive antes de se demitir para ir trabalhar na concorrência.
*   **Visão Sênior (Vulnerabilidades/Escala):** A implementação de DLP é um inferno de "falsos positivos" que irrita a diretoria e atrasa negócios legítimos. Além disso, o DLP tem uma vulnerabilidade puramente analógica insuperável: a câmera do celular. O software impede você de copiar o texto, mandar o arquivo por e-mail ou usar um pendrive, mas ele não consegue impedir o funcionário de pegar o seu smartphone pessoal, apontar para o monitor e tirar 50 fotos da planilha confidencial.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_DLP]] é o **Detector de Metais e a Revista na porta de saída de uma mina de diamantes**. O [[Rede_Firewall]] foca intensamente em ver quem está *entrando* na mina (os bandidos externos). O DLP foca exclusivamente em quem está *saindo* da mina (os próprios funcionários). Ele não se importa se o funcionário tem um crachá válido; se o scanner apitar detectando que há um diamante no bolso dele (um número de cartão de crédito no anexo do e-mail), a catraca trava e a gerência é notificada.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O núcleo algorítmico da maioria dos sistemas DLP (como o Microsoft Purview ou Symantec) reside na leitura de padrões. Se você quisesse criar um DLP básico via terminal Linux para achar arquivos na rede contendo o formato do CPF brasileiro (XXX.XXX.XXX-XX) escondidos antes de um funcionário tentar enviá-los, você faria:
```bash
# Usa Expressão Regular (Regex) para varrer os documentos da pasta do usuário procurando a assinatura matemática de um CPF:
grep -E -r -o '[3-11]{3}\.[3-11]{3}\.[3-11]{3}-[3-11]{2}' /home/usuario/documentos/
````

5. História do Conteúdo

Tornou-se mandatório e vital para corporações após o início da década de 2010, impulsionado agressivamente pelo surgimento das severas leis globais de proteção de dados (como a GDPR na Europa e a LGPD no Brasil). De repente, as empresas poderiam ser multadas em milhões de dólares se vazassem CPFs. O mercado migrou do simples "bloqueio de hackers externos" para o controle obsessivo de "para quem os meus funcionários estão mandando esses e-mails".