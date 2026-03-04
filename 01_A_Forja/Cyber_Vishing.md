---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Cyber_Vishing

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Vishing (Voice Phishing) é o ataque de engenharia social conduzido através de chamadas telefônicas ou de voz (VoIP), visando induzir a vítima por pressão psicológica ao vivo a revelar senhas ou tokens de autenticação.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O criminoso forja o número de identificação da chamada (Caller ID Spoofing) para que no visor da vítima apareça o número do banco dela ou do suporte técnico. Ao atender, o golpista encena autoridade ou pânico para exigir a confirmação de dados críticos na hora.
- **O Problema que Resolve:** Para o atacante, elimina o tempo que a vítima teria para pensar ou pesquisar. O ataque exige resolução em tempo real.
- **Visão Sênior (Vulnerabilidades/Escala):** Ataques de Vishing evoluíram para o "Abismo da IA". Hoje, os atacantes extraem amostras de áudio de redes sociais via [[Cyber_OSINT]] e utilizam *Deepfake* para clonar a exata voz do CEO de uma corporação, ligando para o departamento financeiro ordenando transferências milionárias. Nenhuma ferramenta técnica tradicional consegue barrar um golpe de áudio perfeito.

#### 3. As Sinapses (Conexões Livres)
O [[Cyber_Vishing]] é **o sequestro relâmpago cognitivo**. Enquanto o [[Cyber_Phishing]] é um campo minado onde você pisa se quiser, o Vishing é alguém agarrando o seu colarinho na rua e gritando ordens. A tática se baseia na dissonância cognitiva de autoridade: o ser humano foi treinado desde a infância para obedecer a uma voz confiante e burocrática no telefone. Se a voz disser "Aqui é a segurança do banco, seu cartão foi clonado", o cérebro congela e entrega o PIN de segurança.

#### 4. Pragmatismo Aplicado (Código/Implementação)
A execução moderna de Vishing usa tecnologia VoIP (Voice over IP) barata para mascarar origens de fraude. Softwares baseados em Asterisk permitem a forja do Caller ID facilmente.
```conf
# Configuração maliciosa em um servidor PBX Asterisk para forjar a identidade da chamada de saída (Spoofing)
[vishing_outbound]
exten => _X.,1,Set(CALLERID(all)="Suporte Microsoft" <08001234567>)
exten => _X.,2,Dial(SIP/${EXTEN}@provedor_voip)
````

5. História do Conteúdo

É a tradução direta do _Phreaking_ para os tempos modernos. Nos anos 1990, hackers como Kevin Mitnick tornaram-se lendas não invadindo sistemas com códigos de Matrix, mas apenas ligando para as recepcionistas das grandes teles, fingindo serem técnicos em manutenção e pedindo que elas alterassem as senhas dos roteadores.