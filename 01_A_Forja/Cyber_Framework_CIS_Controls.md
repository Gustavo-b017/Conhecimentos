---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Framework_CIS_Controls

#### 1. O Axioma (A Definição Rígida)
**O que é:** O CIS Controls (Center for Internet Security Controls) é um conjunto priorizado de 18 ações e melhores práticas de defesa cibernética criadas por especialistas globais com o objetivo exclusivo de bloquear os ataques cibernéticos mais penetrantes, perigosos e comuns.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente de normas quilométricas, os Controles CIS são divididos em três Grupos de Implementação (Implementation Groups - IGs), que vão da higiene básica (IG1 - para pequenas empresas) até a proteção avançada (IG3 - para grandes corporações). Os controles iniciais são implacáveis: Controle 1 (Inventário de Equipamentos) e Controle 2 (Inventário de Software).
*   **O Problema que Resolve:** Cura a "Fadiga de Frameworks". Normas como a [[Cyber_ISO_27001]] são maravilhosas para a gerência, mas são densas, teóricas e cheias de burocracia. O CIS Controls foi desenhado para o analista de TI prático. Ele diz exatamente o que instalar e o que fechar primeiro para sobreviver a 85% dos ataques massivos.
*   **Visão Sênior (Vulnerabilidades/Escala):** A diferença tática crucial de um arquiteto é entender que **CIS Controls** (O que fazer no escopo da empresa) anda de mãos dadas com os **CIS Benchmarks** (Como apertar os parafusos na máquina). O Controle 4 exige a "Configuração Segura dos Ativos". Para executá-lo, o administrador baixa o "CIS Benchmark do Ubuntu 22.04", que é um PDF de 800 páginas explicando quais linhas exatas de código alterar no sistema operacional Linux para torná-lo à prova de balas militar.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se a ISO 27001 é o "Plano de Gerenciamento de Riscos de um Acampamento no Deserto", os CIS Controls são a **Lista de Sobrevivência Brutal**. A ISO diz "avalie se você terá sede". O CIS Controle 1 diz "Compre água agora". O CIS Controle 2 diz "Compre um mapa". Ele não perde tempo discutindo a filosofia do risco; ele foca na alocação imediata de recursos vitais porque assume que o ataque (o calor do deserto) é uma certeza matemática.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O CIS Control 1 (Inventário e Controle de Ativos de Redes) não é preenchido com planilhas de Excel. Um profissional executa isso mapeando ativamente a infraestrutura para descobrir o que está ligado na sombra usando ferramentas do laboratório (Aula 5) como o Nmap:
```bash
# Pragmatismo do Controle 1: Descoberta de ativos locais. "Você não pode proteger o que não sabe que existe."
# Varre a sub-rede via ping sweep apenas para levantar os IPs ativos e atualizar o inventário.
nmap -sn 192.168.1.0/24
````

5. História do Conteúdo

Originalmente lançado em 2008 pelo SANS Institute em colaboração com o FBI, era conhecido informalmente como o "SANS Top 20". A lista nasceu da frustração de agências do governo americano que notaram que a vasta maioria das violações de dados gigantescas poderiam ter sido evitadas se as vítimas simplesmente tivessem implementado higiene digital básica (como saber quais computadores estão na rede e remover permissões de admin de quem não precisa).