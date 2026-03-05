---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Framework_MITRE_ATTACK

#### 1. O Axioma (A Definição Rígida)
**O que é:** O MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) é uma base de conhecimento global, acessível e em constante atualização, que cataloga e categoriza rigorosamente o comportamento de atacantes cibernéticos com base em observações de invasões do mundo real.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O framework organiza o ataque em uma matriz de **Táticas** (o objetivo do invasor, ex: "Roubar Credenciais") e **Técnicas** (como ele atinge o objetivo, ex: "Keylogger"). Cada técnica possui um ID específico, exemplos de grupos criminosos (APTs) que a utilizam e formas de mitigação associadas.
*   **O Problema que Resolve:** Destrói a dependência de "Indicadores de Comprometimento" (IoCs) estáticos. Bloquear um IP ou um Hash de vírus (IoC) é inútil, pois o atacante muda isso em um segundo. O MITRE resolve o problema mudando o foco da defesa para o **Comportamento** (TTPs - Tactics, Techniques, and Procedures). O atacante sofre muito mais para mudar *como* ele age do que a ferramenta que ele usa.
*   **Visão Sênior (Vulnerabilidades/Escala):** O MITRE não é um checklist de conformidade ou uma ferramenta para passar em auditoria (como a [[Cyber_ISO_27001]]). É um mapa de caça. Equipes de *Threat Hunting* seniores e de *Red Team* ([[Cyber_Pentest]]) usam o MITRE para emular ameaças específicas. A vulnerabilidade corporativa é tentar mapear todas as centenas de técnicas de uma vez, esgotando o orçamento do SIEM ([[Cyber_Monitoramento_Continuo]]) em vez de focar nas técnicas mais prováveis para o seu setor de negócios.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O MITRE ATT&CK é o **Playbook (Livro de Jogadas) do Time Inimigo no Futebol Americano**. O técnico da defesa (o CISO) não tenta adivinhar o que o ataque vai fazer baseando-se na cor da chuteira do adversário (IoC). Ele estuda o Playbook do adversário, que diz: "Na 3ª descida, eles sempre fazem um passe curto pela lateral esquerda" (Comportamento/Tática). Sabendo disso, o técnico posiciona seus zagueiros (Firewall/EDR) exatamente naquela rota. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
O MITRE dita a inteligência das ferramentas de detecção modernas (como as buscas no Microsoft Sentinel ou Splunk). Um analista procura uma técnica específica, como "T1059.001 - [[Cyber_Phishing_Spear|Spearphishing Attachment]]", usando a matriz como guia de consulta (KQL - Kusto Query Language):
```kusto
# Consulta caçando o comportamento da Técnica MITRE T1059.001 (Anexo malicioso abrindo prompt de comando no Windows)
DeviceProcessEvents
| where InitiatingProcessFileName in~ ("winword.exe", "excel.exe", "powerpnt.exe")
| where FileName in~ ("cmd.exe", "powershell.exe")
````

5. História do Conteúdo

Criado em 2013 pela organização MITRE (a mesma corporação sem fins lucrativos que gerencia a lista global de [[Cyber_CVE|CVEs]] - Common Vulnerabilities and Exposures). O objetivo original era documentar as táticas usadas em simulações de ataques no próprio ambiente interno da MITRE, provando que a indústria de segurança precisava de um idioma comum para descrever "o que o atacante faz depois que o alarme toca".