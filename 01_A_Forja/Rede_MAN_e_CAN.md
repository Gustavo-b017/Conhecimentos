---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

### Rede_MAN_e_CAN
#### 1. O Axioma (A Definição Rígida)
**O que é:** Escopos de rede intermediários. A **MAN** (Metropolitan Area Network) abrange uma cidade inteira, enquanto a **CAN** (Campus Area Network) interliga múltiplos prédios corporativos ou universitários contíguos. Ambas existem para fundir múltiplas LANs sem pagar o preço de lentidão da WAN.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de usar os links comuns de internet, uma CAN ou MAN é frequentemente construída sobre anéis dedicados de Fibra Óptica ou conexões Micro-ondas.
*   **O Problema que Resolve:** Imagine uma universidade gigante ou uma empresa com um prédio de RH e um prédio de Engenharia separados por 3 quarteirões. Passar o tráfego pesado entre eles via internet normal (WAN) seria caríssimo e lento. A MAN/CAN cria uma "super rodovia" metropolitana que faz os dois prédios parecerem estar na mesma [[Rede_LAN]] gigantesca.
*   **Visão Sênior (Vulnerabilidades/Escala):** Rompimentos físicos são críticos. Se uma retroescavadeira corta o link de fibra óptica da rua principal (MAN), prédios inteiros ficam isolados. Exigem altíssimo investimento (CAPEX) para lançamento de cabos subterrâneos ou aluguel de "Fibra Apagada" (Dark Fiber) de prefeituras e operadoras de telefonia local.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se a LAN é a sua casa e a WAN são as rodovias interestaduais; a MAN é o **Sistema de Avenidas e Ruas do seu bairro**. Você usa a MAN quando quer visitar o seu vizinho no fim da rua sem precisar pegar a estrada interestadual. A CAN é como um **Condomínio Fechado Gigante**: há várias casas separadas (LANs), mas a infraestrutura das ruas ligando elas pertence ao próprio síndico da universidade ou empresa.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Não há um comando específico no SO que mostre "Você está numa MAN". Mas em termos de arquitetura e contratação (Telecom), você usa tecnologias como *Metro Ethernet* para configurar essas redes corporativas como se estivessem num mesmo switch:
```text
Porta 1 do Switch (Edifício A) ----------> Anel Óptico Metropolitano ----------> Porta 10 do Switch (Edifício B)
# O sistema operacional de ambos os lados pensa estar no mesmo prédio físico (Layer 2).
````

5. História do Conteúdo

A evolução das redes metropolitanas (MANs) está diretamente ligada às antigas operadoras de TV a Cabo nos anos 80 e 90. Quando as operadoras perceberam que podiam usar os mesmos cabos coaxiais subterrâneos que levavam televisão para os bairros para também conectar os computadores das empresas da cidade inteira em alta velocidade, o conceito de "Rede Metropolitana" explodiu, criando o mercado moderno de provedores locais.