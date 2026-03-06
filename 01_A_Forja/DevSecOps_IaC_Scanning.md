---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/devsecops
---
### DevSecOps_IaC_Scanning

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Scanner de Infraestrutura como Código (IaC Scanning) é um controle preventivo estático (SAST focado em nuvem) que varre manifestos declarativos (Terraform, Kubernetes, CloudFormation) no ciclo de vida de integração antes que servidores inseguros ou expostos sejam criados no provedor público.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Quando o engenheiro envia (Commit) o código `main.tf` para criar uma [[Rede_VPC]] ou um [[Cloud_AWS_S3]] no repositório, o scanner intercepta o arquivo e o avalia contra as normas rígidas (como CIS Benchmarks e PCI-DSS). Se o código diz: "Abrir a Porta SSH 22 para 0.0.0.0/0", a ferramenta falha o pipeline e bloqueia a criação na nuvem instantaneamente.
*   **O Problema que Resolve:** Mata o *Misconfiguration* na origem. O maior risco na nuvem não é invasão complexa, é o erro humano do administrador. O scanner atua como o "Corretor Ortográfico Arquitetural", reduzindo em até 84% o volume caótico de alertas em tempo de execução que inundariam o [[Cyber_CSPM]] da organização mais tarde. Ele materializa o conceito brutal de "Security by Design".
*   **Visão Sênior (Vulnerabilidades/Escala):** O desafio colossal desta abordagem é o Contexto Geopolítico e Técnico. O scanner olha um código criando um Bucket S3 sem criptografia e grita. Porém, aquele bucket pode ser apenas para hospedar as imagens públicas de marketing do site, onde a criptografia não importa. Lidar com Falsos Positivos e forjar o *Policy-as-Code* (Políticas como Código, como o Rego no OPA) requer maturidade em arquitetura, senão o time de infraestrutura vai desativar o scanner para poder trabalhar.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O monitoramento clássico (CSPM) atua como o **Inspetor da Prefeitura que fiscaliza e multa um prédio pronto** por estar com a fundação torta (o que força a sua demolição e causa prejuízo). O [[DevSecOps_IaC_Scanning]] é o **Engenheiro Chefe que avalia o Desenho Arquitetônico no Papel (AutoCAD)**. Ele olha as medidas da estrutura da sua planta baixa e diz: "Se você colocar esse pilar aqui, o prédio vai cair. Corrija o desenho agora antes que eu mande cimento pra lá". O erro morre na folha de papel.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Ferramentas de código aberto como o `checkov` e o `tfsec` rodam sem dor e de maneira cirúrgica no terminal ou nas Actions do GitHub. Analisando um projeto de Terraform:
```bash
# Executando análise implacável nas definições de infraestrutura contra falhas conhecidas
checkov -d ./infra-aws/ --quiet --compact
````

_Saída esperada caso tente rodar algo tóxico:_ `FAILED: CKV_AWS_24: "Ensure no security groups allow ingress from 0.0.0.0:0 to port 22"`.

5. História do Conteúdo

Ascendeu violentamente durante os últimos cinco anos com a solidificação da [[Cyber_Immutable_Infrastructure]] encabeçada pela HashiCorp (Terraform). Quando as corporações abandonaram a prática amadora de "clicar em botões no console da AWS" para "provisionar servidores descrevendo o estado desejado em texto", a Segurança percebeu uma janela de ouro: a oportunidade inédita de ler a intenção da rede em linguagem plana e detê-la milissegundos antes que ela se transformasse em silício.