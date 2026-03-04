---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_VoIP

#### 1. O Axioma (A Definição Rígida)
Voice over IP (VoIP) é o protocolo que converte sinais de áudio analógicos em pacotes digitais de dados, permitindo a transmissão de chamadas telefônicas diretamente sobre a infraestrutura da internet.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Em vez de fios de cobre dedicados (circuito fechado), o hardware capta a voz, codifica (Codecs), empacota no veloz e sem garantias protocolo [[Rede_UDP]] e transmite.
- **O Problema que Resolve:** Barateia agressivamente as comunicações corporativas globais, extinguindo a infraestrutura física separada de telefonia e unificando voz e dados no mesmo cabo de rede.
- **Visão Sênior (Vulnerabilidades/Escala):** Por padrão, a sinalização e o fluxo de voz de protocolos antigos não são criptografados. Se o tráfego não for encapsulado por uma [[Rede_VPN]] ou protocolos seguros, qualquer atacante com o Wireshark na mesma rede pode realizar um ataque de interceptação ([[Cyber_Eavesdropping]]) e remontar a chamada de voz em um arquivo `.wav`, ouvindo senhas ditadas ao telefone.

#### 3. As Sinapses (Conexões Livres)
A [[Rede_VoIP]] transforma a fala humana em cartas postais. No sistema telefônico antigo, você alugava um cano de aço direto da sua casa até a outra pessoa; ninguém no meio entrava no cano. No VoIP, as suas palavras viram cartas despachadas na rede pública ([[Rede_HTTP]]). Como as tecnologias baratas mascaram origens facilmente, o VoIP tornou-se a arma perfeita para fraudadores automatizarem ligações maliciosas globais, executando [[Cyber_Vishing]].

#### 4. Pragmatismo Aplicado (Código/Implementação)
Técnica forense no Wireshark para materializar a fragilidade do VoIP não criptografado. Um analista pode buscar os pacotes RTP e extrair o áudio de volta:
```wireshark
# Filtro base no Wireshark para isolar a sinalização de voz:
sip or rtp
# Em seguida, acessa-se: Telephony > VoIP Calls > Play Streams (Para ouvir a chamada roubada).
````

5. História do Conteúdo

Nasceu em 1995 através do software Internet Phone da empresa VocalTec. A premissa era pura rebeldia e economia financeira: burlar as tarifas obscenas cobradas pelas companhias telefônicas em chamadas interurbanas e internacionais de longa distância, usando a rede de dados para carregar a voz quase de graça.