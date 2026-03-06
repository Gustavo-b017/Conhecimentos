---
tags:
  - afinidade/media
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/cloud
---

### Cyber_CIEM

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Cloud Infrastructure Entitlement Management (CIEM) é o mecanismo de auditoria microscópica focado exclusivamente em rastrear, calcular e aniquilar riscos de identidades (IAM) superprivilegiadas e acessos não utilizados concedidos a humanos e máquinas em ambientes multicloud.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O CIEM ingere continuamente milhões de logs de auditoria (como o AWS CloudTrail) para gerar a "Net Effective Permission" (Permissão Efetiva Real). Ele não olha apenas o que está no papel, ele compara a matemática. Ele diz: "A conta do servidor Jenkins tem permissão teórica para acessar 10.000 recursos, mas nos últimos 90 dias ele só acessou 3 recursos". E então o CIEM oferece o código exato para castrar o poder dessa conta de 10.000 para os exatos 3.
*   **O Problema que Resolve:** O letal fenômeno do *Permission Creep* (Acúmulo de Permissões Crônicas) aliado à explosão das "Identidades Não Humanas" (NHIs). Na nuvem, existem 50 máquinas e APIs conversando sozinhas para cada 1 funcionário humano. Controlar essa teia com o antigo [[Cyber_IAM]] baseado em Active Directory é cego e impraticável.
*   **Visão Sênior (Vulnerabilidades/Escala):** O atrito cultural do *Right-sizing* (cortar excessos). Se o CIEM remover uma permissão inativa de forma cega (Auto-remediação), e um mês depois a empresa precisar rodar o fechamento fiscal anual que usava aquela permissão órfã, a corporação sofre apagão de negócio. Retirar poder de desenvolvedores baseando-se apenas em telemetria passada sem entendimento contextual é a forma mais rápida de ser odiado e banido do ecossistema da empresa.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_CIEM]] atua como um **Mestre de Armas recolhendo crachás de acesso universal**. No início de um projeto, por preguiça, o gerente entrega o "Crachá Mestre" (Permissão FullAdmin `* : *`) para o encanador que vai consertar apenas um ralo no 3º andar. O CIEM fica vigiando o encanador pelas câmeras o mês inteiro. Ele conclui: "Você nunca subiu no 10º andar nem foi ao cofre no subsolo". Imediatamente, ele desativa o crachá mestre e entrega um crachá de plástico que só permite, fisicamente e matematicamente, que o encanador abra a porta do banheiro do 3º andar, trancando a movimentação lateral caso ele seja um impostor.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O pavor da cibersegurança que o CIEM caça impiedosamente: A política JSON com coringa genérico injetada em contas de serviço, que permite o temido [[Cyber_Privilege_Escalation]]:
```json
// Política Lixo/Preguiçosa clássica que o CIEM exige que seja assassinada.
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}
````

5. História do Conteúdo

Criado recentemente, perto de 2020, para suprir uma brecha monstruosa que os desenvolvedores do CSPM inicial deixaram passar. A nuvem pública da AWS tem mais de 10.000 permissões individuais diferentes no seu modelo IAM. A complexidade matemática dessa rede de acessos cruzados (Roles herdando Policies que anulam Grupos) ultrapassou a capacidade cognitiva do cérebro humano. O mercado teve que forjar um motor especializado apenas para ler arquivos de texto intermináveis e garantir o Princípio do Menor Privilégio.