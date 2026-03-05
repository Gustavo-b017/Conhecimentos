---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/media
  - status/3_incubadora
---

### Arquitetura_SOA

#### 1. O Axioma (A Definição Rígida)
**O que é:** A Arquitetura Orientada a Serviços (SOA) é um modelo de design corporativo onde grandes blocos monolíticos de software são fatiados em serviços de negócio independentes, reutilizáveis e governados por contratos estritos sobre a rede.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Em vez do sistema inteiro rodar num único processo, capacidades lógicas (como "Consultar Fatura") são isoladas. A comunicação é forçada a passar por contratos rigorosos (geralmente WSDL) orquestrados por uma camada centralizadora.
- **O Problema que Resolve:** Destrói a caótica [[Arquitetura_Ponto_a_Ponto|Ponto a Ponto]] ([[Mindset_Ordem_e_Caos]]). Impõe governança, reutilização de código e rastreabilidade para megacorporações que possuem centenas de sistemas legados que precisam interoperar.
- **Visão Sênior (Vulnerabilidades/Escala):** O SOA falhou não pela técnica, mas pelo seu peso burocrático. A exigência de governança pesada (fases de Plan, Define, Enable, Measure) engessa o desenvolvimento. Um desenvolvedor não pode simplesmente criar um serviço; ele precisa que um comitê de arquitetura aprove o contrato XML. Além disso, no SOA clássico, diferentes serviços ainda compartilham o mesmo Banco de Dados físico, o que mata a independência de *deploy* e não resolve o acoplamento de dados subjacente.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O SOA atua como a **União Europeia no seu início burocrático**. Antes, os países (sistemas) guerreavam ([[Arquitetura_Ponto_a_Ponto]]). O SOA cria um Parlamento Central e uma moeda única. Todos podem conversar e fazer comércio (reutilização de serviços), mas para importar um queijo da França para a Alemanha, você é obrigado a preencher um formulário alfandegário de 10 páginas (Protocolo [[Arquitetura_SOAP|SOAP]]) carimbado pela central. É extremamente seguro e auditável, mas mortalmente lento para um mundo ágil que prefere [[Arquitetura_Microsservicos|Microsserviços]].

#### 4. Pragmatismo Aplicado (Código e Implementação)
O ciclo de Governança SOA dita que a arquitetura não começa no código, mas no negócio. A tabela tática que o arquiteto preenche antes de escrever uma linha de Java:
- **Plan:** Qual o ROI (Retorno sobre Investimento) se transformarmos "Cobrança" em serviço?
- **Define:** Qual será a padronização do contrato XML (WSDL)?
- **Enable:** Onde o serviço rodará fisicamente (VMs)?
- **Measure:** Qual o SLA de resposta (Latência máxima) que o contrato garante?

#### 5. História do Conteúdo
SOA surgiu no fim dos anos 1990 e dominou a década de 2000. Foi a bala de prata vendida por consultorias como Gartner e empresas como IBM e Oracle. O objetivo financeiro real não era "melhorar o código", mas sim vender caríssimas plataformas de integração ([[Infra_Middleware|Middlewares]]) para os bancos e governos, permitindo que seus velhos mainframes COBOL conversassem com os novos portais web em Java.