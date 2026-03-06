---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/cloud
---

### Cyber_CNAPP

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Cloud-Native Application Protection Platform (CNAPP) é a super-arquitetura unificada que aglutina as disciplinas isoladas de segurança de nuvem ([[Cyber_CSPM]], [[Cyber_CWPP]], [[Cyber_CIEM]]) em um único motor de visibilidade e defesa, operando desde a concepção do código até a execução em produção.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de usar uma ferramenta para olhar a rede, outra para olhar o contêiner e outra para olhar o código, o CNAPP centraliza a telemetria. Ele lê o pipeline de CI/CD ([[Rede_NetDevOps_CICD]]), audita a postura da nuvem e monitora o Kernel do sistema operacional através de sensores unificados.
*   **O Problema que Resolve:** O abismo do contexto cego. O CNAPP realiza a **correlação de riscos**. Ele não emite um alerta burro dizendo "A porta 22 está aberta". Ele correlaciona os dados e diz: "A porta 22 está aberta (CSPM), levando a um contêiner rodando uma biblioteca com vulnerabilidade crítica (CWPP), e esse contêiner possui uma chave de administrador da AWS superprivilegiada (CIEM)".
*   **Visão Sênior (Vulnerabilidades/Escala):** A adoção de um CNAPP exige uma maturidade de engenharia colossal. O mercado sofre com o *vendor lock-in* (ficar preso a um gigante como Wiz ou Palo Alto Prisma). Além disso, a "visão total" gera um custo computacional e financeiro gigantesco se não houver uma governança de *shift-left* verdadeira; não adianta o CNAPP apontar 10.000 falhas se a equipe de DevSecOps não tiver braço para corrigir o código na raiz.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O mercado antigo de segurança era um **Hospital Fragmentado e Surdo**. O ortopedista (CSPM) olhava o osso, o cardiologista (CWPP) olhava o coração, e o neurologista (CIEM) olhava o cérebro. Se o paciente morresse, cada um dizia "A minha parte estava ótima". O [[Cyber_CNAPP]] é o **Médico Legista Chefe com o Prontuário Integrado**. Ele analisa o corpo de forma holística e prova que o remédio receitado pelo ortopedista causou a falência do coração, pois ele enxerga as conexões e a toxicidade entre os domínios que antes eram silos isolados.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A força do CNAPP se manifesta em gráficos de correlação (Attack Path Analysis), mas a base de consulta é puramente API. Exemplo de query conceitual para um motor CNAPP mapeando a tempestade perfeita:
```graphql
# Caça de vetor crítico: Servidor exposto + Vulnerabilidade letal + Permissão Alta
query {
  CloudResource(type: "EC2") {
    exposed_to_internet: true
    vulnerabilities(severity: "CRITICAL")
    iam_roles(permissions: "Admin")
  }
}
````

5. História do Conteúdo

O termo foi cunhado pela consultoria Gartner (liderada por analistas como Neil MacDonald) em 2021. A indústria chegou a um ponto de ruptura financeira e cognitiva: os CISOs não aguentavam mais gerenciar 15 painéis (dashboards) diferentes de segurança que não conversavam entre si e geravam _Fadiga de Alertas_. O CNAPP foi a resposta do mercado para consolidar aquisições e transformar a segurança na nuvem em uma esteira única e unificada.