---
tags:
  - afinidade/media
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/cloud
---

### Cyber_CSPM

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Cloud Security Posture Management (CSPM) é uma tecnologia de monitoramento contínuo operando no plano de controle (Control Plane) da nuvem, desenhada exclusivamente para caçar, alertar e remediar de forma automática o maior vetor de falhas arquiteturais: os *Misconfigurations* (Erros de Configuração).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ele não entra na sua Máquina Virtual nem lê o seu banco de dados. Ele consome as APIs públicas do seu provedor (AWS, Azure, GCP) e compara o estado da sua infraestrutura contra frameworks matemáticos de sobrevivência (como [[Cyber_Framework_CIS_Controls]], [[Cyber_PCI_DSS]] e [[Cyber_ISO_27001]]).
*   **O Problema que Resolve:** O erro humano na escala virtual. Um engenheiro de DevOps cria um Bucket S3 ([[Cloud_AWS_S3]]) para guardar arquivos de teste, esquece de trancar a permissão pública e vai dormir. O CSPM identifica o desvio do padrão de segurança da empresa e tranca o bucket via API em 2 segundos, antes que o robô do invasor ([[Cyber_OSINT]]) o encontre.
*   **Visão Sênior (Vulnerabilidades/Escala):** A miopia de profundidade. O CSPM é cego para o "Plano de Dados". Ele atesta com 100% de certeza que a sua máquina Linux está com o firewall fechado e o disco criptografado. Contudo, se o código Java dentro da máquina tiver um [[Cyber_Ataque_SQL_Injection|SQLi]] letal ou um [[Cyber_Malware_Rootkit]] rodando na memória RAM, o CSPM não faz a menor ideia, relatando um falso status de "Verde/Seguro".

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_CSPM]] é o **Inspetor Predial da Prefeitura**. Ele passa na frente do seu prédio corporativo, verifica se a fachada está pintada, confere se as saídas de emergência estão no tamanho correto (normas da ISO) e se a porta principal tranca direito (O Plano de Controle da Nuvem). No entanto, o Inspetor Predial **não tem a chave para entrar nos quartos**. Se houver um laboratório de metanfetamina operando secretamente dentro do apartamento 402 (A carga de trabalho no Runtime), o Inspetor anotará na prancheta que "o prédio está perfeito".

#### 4. Pragmatismo Aplicado (Código e Implementação)
Soluções open-source como o *Prowler* ou *CloudQuery* executam o motor do CSPM na linha de comando para varrer a AWS do usuário em busca de configurações primitivas:
```bash
# Rodando uma auditoria massiva na conta AWS cruzando com os controles CIS
prowler aws --compliance cis_1.5_aws --region us-east-1 --output json
````

5. História do Conteúdo

Ascendeu entre 2015 e 2018 com os megavazamentos do "Capital One" e do "Equifax", onde hackers roubaram dezenas de milhões de CPFs e cartões de crédito não quebrando criptografia, mas explorando buckets de nuvem deixados pateticamente abertos para o público por desleixo. O mercado entendeu da pior forma que, no _Modelo de Responsabilidade Compartilhada_ ([[Cyber_Cloud_Security]]), a Amazon protege o cabo de força do Data Center, mas a burrice da configuração é de inteira responsabilidade do cliente, forçando a criação do CSPM para auditar os engenheiros.