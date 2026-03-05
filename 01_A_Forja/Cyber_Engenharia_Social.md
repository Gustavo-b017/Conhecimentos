---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Engenharia_Social
#### 1. O Axioma (A Definição Rígida)
**O que é:** A Engenharia Social é a exploração tática de vieses e vulnerabilidades psicológicas humanas para manipular pessoas, forçando-as a quebrar protocolos de segurança, conceder acessos ou executar cargas maliciosas de forma voluntária.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Emprega [[Mindset_Gatilhos_Mentais]] (Urgência, Autoridade, Medo, Ganância ou Confiança). O atacante frauda a própria identidade ([[Cyber_Spoofing|Spoofing]] visual/vocal) e interage via e-mail (*[[Cyber_Phishing|Phishing]]*), telefone (*[[Cyber_Vishing|Vishing]]*) ou SMS (*[[Cyber_Smishing|Smishing]]*), convencendo o alvo de que está falando com o TI, com o chefe ou com o banco.
* **O Problema que Causa:** Para o atacante, invalida o orçamento multimilionário de defesa da empresa. Por que perder semanas tentando quebrar a criptografia militar [[Cyber_AES_256]] se você pode ligar para a secretária, dizer que é do suporte técnico e pedir para ela ditar a senha?
*   **Visão Sênior (Vulnerabilidades/Escala):** O ser humano não possui pacote de atualização (Patch) e a [[Mindset_Natureza_Humana]] é falha. Treinamentos de conscientização mitigam o risco, mas não o eliminam. A única arquitetura sênior capaz de resistir a um ataque de engenharia social bem-sucedido é a adoção brutal do [[Cyber_Zero_Trust]]: mesmo que o funcionário entregue a senha, o acesso é negado pois o sistema exige um token de hardware de Múltiplo Fator de Autenticação ([[Cyber_MFA|MFA]]) e valida a geolocalização.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A [[Cyber_Engenharia_Social]] é exatamente o conceito do **Cavalo de Tróia de Homero** aplicado à era da informação. Os gregos perceberam que a muralha de Tróia (O [[Rede_Firewall]]) era impenetrável pela força bruta. Eles apelaram para o [[Mindset_Vies_Cognitivo]] de vaidade e religiosidade dos troianos, deixando um "presente" de madeira no portão (o [[Cyber_Malware_Trojan]]). Os troianos, manipulados cognitivamente, abriram as próprias portas e arrastaram a aniquilação para dentro da cidade com as próprias mãos. Na TI, o cavalo de madeira é um e-mail com o assunto "Aumento de Salário.pdf".

#### 4. Pragmatismo Aplicado (Código e Implementação)
O ataque não usa código contra a máquina, usa texto manipulado contra o cérebro. 
*Exemplo prático da anatomia de um e-mail focado no gatilho de "Urgência/Autoridade":*
```text
De: it-support@emppresa.com (Letra 'P' duplicada para enganar os olhos)
Assunto: [CRÍTICO] Sua conta será desativada em 2h

João, identificamos uma falha de sincronização na sua conta Microsoft 365.
Acesse imediatamente o link abaixo e confirme suas credenciais para evitar o bloqueio total no meio do expediente. 
Link falso embutido: [Portal de Sincronização Microsoft]
```

5. História do Conteúdo

A manipulação de confiança é a fraude mais antiga da humanidade, existindo desde os primeiros charlatões em praças públicas. Na cibernética, Kevin Mitnick eternizou a prática na década de 1990. Ele não era um mestre em escrever super-códigos; ele era um mestre em ligar para as companhias telefônicas disfarçado de técnico e convencer os funcionários a lhe entregarem os códigos de roteamento interno.