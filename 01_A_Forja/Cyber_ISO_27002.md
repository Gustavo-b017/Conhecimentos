---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_ISO_27002

#### 1. O Axioma (A Definição Rígida)
**O que é:** A ISO/IEC 27002 é o catálogo de referência detalhado e suplementar à 27001 (frequentemente referido no Anexo A), fornecendo um conjunto abrangente de 93 controles de segurança tecnológica, física e organizacional recomendados para mitigar riscos.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ela age como o menu de um restaurante de defesas. Se a sua análise de risco (pela ISO 27001) diz que invasões de rede são um perigo crítico, você abre a ISO 27002 no "Controle 8.20 (Network Security)" ou "Controle 8.21 (Security of Network Services)" e ela te listará as melhores práticas de como arquitetar firewalls, VPNs e segregação de ambientes.
*   **O Problema que Resolve:** Traduz a burocracia administrativa da 27001 em ações táticas claras para a equipe de tecnologia da informação executar, padronizando a nomenclatura da defesa.
*   **Visão Sênior (Vulnerabilidades/Escala):** Profissionais juniores cometem o erro de tentar implementar os 93 controles simultaneamente, o que destrói o orçamento e a agilidade da empresa. A visão sênior exige o *Tailoring* (Alfaiataria): você escolhe apenas os controles que fazem sentido matemático para a arquitetura da sua nuvem ou infraestrutura local, ignorando o que for excessivo. Além disso, a empresa *não* se certifica na ISO 27002, ela se certifica na 27001 e *usa* a 27002 para alcançar o objetivo.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se a ISO 27001 é o "Plano Diretor", a [[Cyber_ISO_27002]] é o **Manual de Engenharia Civil e Arquitetura do Pedreiro**. Ela que vai dizer, através do Controle 8.20, a espessura exata do concreto do cofre, que o cano de esgoto precisa ser de PVC rígido, e que a porta do banco precisa ter fechaduras duplas. Ela é a ponte entre a prancheta do diretor e o martelo da TI.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Quando a ISO 27002 (Controle 8.20 - Network Security) exige a blindagem das redes contra escuta passiva, a implementação tática recai diretamente na restrição operacional, como fechar o *Eavesdropping* no switch corporativo (ex: em ambientes Cisco via segurança de portas):
```bash
# Implementação tática de um Controle ISO 27002 (Proteção contra ARP Spoofing/MitM na Camada 2):
ip arp inspection vlan 10
ip dhcp snooping vlan 10
````

5. História do Conteúdo

Historicamente conhecida como o "Anexo A", a norma sofreu uma alteração massiva em 2022. O comitê da ISO percebeu que a versão antiga tinha 114 controles defasados e não refletia as ameaças modernas (como Ransomware e Cloud). Eles enxugaram para 93 controles agrupados em apenas 4 temas (Organizacional, Pessoal, Físico e Tecnológico), introduzindo novos controles focados em Inteligência de Ameaças (Threat Intelligence) e delegação segura em nuvem.