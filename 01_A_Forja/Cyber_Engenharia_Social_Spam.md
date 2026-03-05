---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/baixa
  - status/3_incubadora
---

### Cyber_Engenharia_Social_Spam

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Spam é o envio de mensagens eletrônicas em massa e não solicitadas, predominantemente via e-mail ou SMS corporativo, servindo historicamente para marketing agressivo, mas usado por cibercriminosos como vetor estatístico de distribuição de ameaças.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Atacantes compram bancos de dados vazados ([[Cyber_OSINT]]) na Dark Web contendo milhões de endereços de e-mails. Eles alugam servidores de envio ou formam [[Cyber_Botnet|botnets]] ([[Cyber_IoT_Security|IoT]]) e disparam milhões de e-mails usando infraestrutura barata. 
*   **O Problema que Causa:** Estatisticamente, gera desperdício brutal de banda de rede e armazenamento nos servidores de e-mail das empresas. Para a cibersegurança, é o "Meio de Transporte" logístico de ameaças, carregando PDFs infectados com [[Cyber_Malware_Trojan|Trojans]], anexos de [[Cyber_Malware_Ransomware|Ransomware]] e links de [[Cyber_Phishing]].
*   **Visão Sênior (Vulnerabilidades/Escala):** A falha ocorre na natureza antiga e não autenticada do protocolo [[Rede_Protocolo_SMTP|SMTP]]. Originalmente, qualquer um podia enviar e-mail dizendo ser outra pessoa. A mitigação sênior exige o endurecimento (Hardening) dos registros de [[Rede_DNS|DNS]] da empresa. Configurar de forma implacável os registros **SPF** (Autoriza IPs a mandarem e-mail), **DKIM** (Assina e-mails criptograficamente) e **DMARC** (Diz para a internet rejeitar qualquer e-mail que falhar nos testes anteriores).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A lógica do Spam é atirar **Uma rede de pesca com buracos grandes num mar morto**. O pescador joga a rede (1 milhão de e-mails com vírus). 999.000 peixes passam pelos buracos da rede, ou os filtros do mar (Gateways Anti-Spam) bloqueiam. O pescador não se importa. Ele só quer os 1.000 peixes inocentes (usuários desatentos) que se prenderam nas malhas para gerar o lucro.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A checagem técnica para ver se uma empresa está preparada para barrar Spoofing e lixo não solicitado envolvendo o próprio nome dela baseia-se na verificação do registro TXT de DMARC no seu DNS:
```bash
# Comando de investigação de OSINT num terminal (Dig) buscando as proteções de autenticidade de um domínio contra o uso em Spam:
dig _dmarc.empresa-alvo.com.br TXT
````

5. História do Conteúdo

A palavra "Spam" vem de uma marca de carne enlatada barata da Hormel Foods, que popularizou-se mundialmente por conta de um esquete do programa de comédia _Monty Python_ nos anos 70, onde os personagens num café não conseguiam conversar porque um grupo de vikings cantava a palavra "Spam" repetidamente, afogando o diálogo. No final dos anos 80, os nerds da Usenet adotaram a piada para descrever pessoas que enviavam lixo massivo nos fóruns e inviabilizavam a comunicação real.