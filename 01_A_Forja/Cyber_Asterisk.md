---
tags:
  - tipo/ferramenta
  - contexto/dev/cyber/ataque
  - afinidade/media
  - status/3_incubadora
---

### Cyber_Asterisk

#### 1. O Axioma (A Definição Rígida)
Asterisk é um software open-source de PABX (Private Branch Exchange) que controla e roteia chamadas de telefonia digital ([[Rede_VoIP]]), sendo frequentemente abusado por criminosos para mascarar identidades em campanhas de fraude.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Transforma um computador ou servidor Linux comum em uma central telefônica complexa. Ele lida com filas de espera, gravação, correio de voz e roteamento [[Rede_Protocolo_SIP|SIP]] (Session Initiation Protocol).
- **O Problema que Resolve:** Destruiu o monopólio bilionário do hardware proprietário de telefonia corporativa (da Cisco, Avaya), permitindo que qualquer empresa criasse uma central telefônica global via software gratuito.
- **Visão Sênior (Vulnerabilidades/Escala):** Por ser extremamente flexível, o Asterisk não força autenticidade de origem. Um invasor usando um servidor Asterisk barato pode configurar o arquivo de plano de discagem (`extensions.conf`) para forjar o número de telefone que vai aparecer no visor do alvo ("[[Cyber_Spoofing|Caller ID Spoofing]]"), simulando ser o suporte da Microsoft ou o banco da vítima.

#### 3. As Sinapses (Conexões Livres)
O [[Cyber_Asterisk]] é o "roteador de internet" do mundo da voz. Porém, a sua capacidade de mentir é a espinha dorsal do [[Cyber_Vishing]]. Ele atua como uma **máquina de crachás falsos**; você digita no terminal qual número quer fingir ser, e ele joga a sua chamada na rede [[Rede_VoIP]] com a máscara perfeita. A falha humana de confiar na tela do celular é o que garante o lucro do atacante.

#### 4. Pragmatismo Aplicado (Código/Implementação)
Código real retirado de investigações de segurança cibernética (citado em fontes) demonstrando como um servidor Asterisk malicioso adultera a identificação da chamada para aplicar o golpe do Suporte da Microsoft [2]:
```conf
# Configuração no arquivo extensions.conf para forjar (Spoofing) a origem:
[vishing_outbound]
exten => _X.,1,Set(CALLERID(all)="Suporte Microsoft" <08001234567>)
exten => _X.,2,Dial(SIP/${EXTEN}@provedor_voip)
````

5. História do Conteúdo

Criado em 1999 por Mark Spencer. Ele fundou a Linux Support Services, mas não tinha US$ 4.000 para comprar um PABX físico para atender seus clientes. Ele escreveu seu próprio sistema de telefonia em C. A ferramenta ficou tão poderosa que revolucionou a telefonia digital, embora hoje seja a base operacional de 99% das centrais clandestinas de telemarketing fraudulento no mundo.