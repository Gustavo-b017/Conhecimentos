---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Ataque_HNDL
#### 1. O Axioma (A Definição Rígida)
**O que é:** O *Harvest Now, Decrypt Later* (HNDL) é um ataque criptográfico de longo prazo, operante na Camada 6 (Apresentação), onde adversários interceptam e armazenam dados fortemente criptografados no presente com a intenção de decifrá-los no futuro.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de tentar quebrar a criptografia [[Cyber_AES_256|AES]] ou [[Rede_TLS|TLS]] em tempo real (o que é computacionalmente impossível hoje), o atacante simplesmente copia e arquiva o tráfego interceptado. Ele aposta na obsolescência matemática.
*   **O Problema que Causa:** Compromete severamente a confidencialidade de dados de vida longa (como segredos de estado ou dados de saúde). A segurança de hoje torna-se a vulnerabilidade de amanhã.
*   **Visão Sênior (Vulnerabilidades/Escala):** A viabilidade deste ataque está diretamente ligada ao advento da [[Cyber_Computacao_Quantica|computação quântica]], que promete quebrar os algoritmos assimétricos ([[Cyber_Criptografia_Assimetrica]]) atuais em segundos. A mitigação sênior exige a adoção precoce de criptografia pós-quântica para proteger o tráfego contra a "colheita" atual.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_Ataque_HNDL]] é como **roubar um cofre de titânio indestrutível hoje e enterrá-lo no quintal**. O ladrão não tem a ferramenta para abri-lo agora, mas ele sabe que, daqui a 10 anos, inventarão um laser capaz de cortar titânio. Ele tem paciência para esperar.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Não há ferramenta defensiva reativa; a proteção é proativa. Organizações mitigam isso forçando o descarte rápido de chaves via *Perfect Forward Secrecy* no TLS, o que garante que o comprometimento futuro de uma chave mestre não decifre as sessões antigas armazenadas.

#### 5. História do Conteúdo
Conceito que ganhou força na última década com o avanço rápido das pesquisas quânticas, forçando órgãos como o NIST a acelerar os processos de padronização de novos algoritmos de criptografia para proteger infraestruturas contra agentes estatais que possuem capacidade massiva de armazenamento de dados