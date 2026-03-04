---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Phishing

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Phishing é o vetor de ataque primário de [[Cyber_Engenharia_Social|engenharia social]] que utiliza comunicações eletrônicas fraudulentas (como e-mails ou sites falsos) para induzir vítimas a revelar credenciais ou instalar cargas maliciosas ([[Cyber_Malware]]).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O atacante clona a estética, os logotipos e a linguagem de uma entidade de confiança (um banco, a equipe de TI). O texto apela para gatilhos de urgência ou medo, forçando o clique em um link que leva a um servidor de coleta de dados sob o controle do criminoso.
- **O Problema que Resolve:** Para o atacante, contorna orçamentos milionários de segurança técnica. O Phishing ataca o elo não mais fraco da rede: o cérebro humano.
- **Visão Sênior (Vulnerabilidades/Escala):** Profissionais ingênuos confiam apenas em filtros de [[Cyber_Engenharia_Social_Spam|Anti-Spam]]. Ataques direcionados (*Spear Phishing*) ou focados em altos executivos (*Whaling*) são cirurgicamente construídos com [[Cyber_OSINT]] e escapam de filtros de palavras-chave facilmente. A única defesa arquitetural inquebrável contra a entrega de senhas via Phishing é o [[Cyber_MFA|MFA]] (Multi-Factor Authentication) amarrado ao hardware (FIDO2) do modelo [[Cyber_Zero_Trust]].

#### 3. As Sinapses (Conexões Livres)
O [[Cyber_Phishing]] opera exatamente como **pescar com uma isca de plástico realista**. O atacante atira milhares de e-mails na água escura da internet usando a tática de [[Cyber_Engenharia_Social]]. Se o peixe (o usuário) olhar apenas para o formato e não para o cheiro, ele morde a isca. O atacante não invadiu o aquário; o próprio peixe engoliu o anzol voluntariamente.

#### 4. Pragmatismo Aplicado (Código/Implementação)
O diagnóstico de Phishing não ocorre no código, mas na auditoria forense do cabeçalho do e-mail. Analisando o domínio real de origem versus o domínio mascarado:
```text
# Cabeçalho de E-mail Extraído (Sintoma de Phishing)
From: "Suporte TI Corporativo" <admin@it-suportt.com>  # Erro de digitação intencional (suportt)
To: <vitima@empresa.com>
Return-Path: <hacker33@ru.server.net> # A resposta vai para a Rússia, não para a TI
````

5. História do Conteúdo

A palavra "Phishing" (pescaria, com "ph" por influência da cultura hacker "phreaking") foi cunhada em meados de 1996 nos grupos de bate-papo da AOL (America Online). Atacantes roubavam contas mandando mensagens aos usuários fingindo ser administradores da AOL pedindo verificação de faturamento.