---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_SIP

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Session Initiation Protocol (SIP) é um protocolo flexível da Camada de Aplicação (Camada 7) criado estritamente para a sinalização, negociação, estabelecimento e encerramento de sessões multimídia interativas e de voz sobre IP (VoIP).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** É baseado em texto puro e modelado sob a mesma arquitetura do HTTP (usa requisições baseadas em texto como INVITE, ACK, BYE, operando tradicionalmente na porta 5060). Ele apenas cuida da burocracia e do "convite". O SIP "acorda" a máquina do outro lado, dita qual será o Codec de áudio e as portas a serem usadas, e sai de cena. O áudio real da conversa vai trafegar em um protocolo parceiro completamente diferente (o RTP) pela internet de forma contínua no UDP.
- **O Problema que Resolve:** Desvincula a inteligência da conexão das redes engessadas da telefonia e empurra para a internet. Ele permite criar sistemas onde a ligação de um computador em Nova York "ache" um celular temporariamente conectado em Tóquio através de registros em servidores Proxy SIP.
- **Visão Sênior (Vulnerabilidades/Escala):** O SIP é inimigo letal do protocolo *NAT (Network Address Translation)*. Como o SIP é texto da Camada 7, ele escreve o seu IP Privado dentro do corpo da mensagem HTTP-like antes de enviar. Quando o NAT do roteador converte o cabeçalho do IP Privado para o IP Público (Camada 3), ele não reescreve o texto de dentro da mensagem SIP. O servidor remoto tenta responder para o IP privado escrito no texto (ex: 192.168.0.5) através da rede pública, resultando no infame cenário de "One-Way Audio" (quando apenas um lado da chamada escuta o áudio). Para resolver isso na força bruta, os roteadores usam ALGs (Application Layer Gateways) para interceptar e reescrever o pacote da Camada 7, destruindo a integridade dos pacotes encriptados.

#### 3. As Sinapses (Conexões Livres)
O [[Rede_SIP]] não é o carteiro da conversa, é o **Mestre de Cerimônias e Cerimonialista de um evento**. Ele liga para a noiva, liga para o noivo, verifica as agendas deles, define qual será o salão de festas e arruma os protocolos de convidados. Assim que a noiva entra no salão (a voz em tempo real através do RTP), o Mestre de Cerimônias vira as costas e vai embora até o momento em que for necessário encerrar a festa formalmente (BYE). 

#### 4. Pragmatismo Aplicado (Código/Implementação)
As mensagens SIP circulam na rede de forma extremamente legível. Quando extraímos os pacotes brutos com o Wireshark, vemos a anatomia clássica de uma requisição de abertura de chamada SIP INVITE:
```http
INVITE sip:telefone-destino@empresa.com SIP/2.0
Via: SIP/2.0/UDP 192.168.1.10:5060;branch=z9hG4bK-d8754z-
From: <sip:funcionario-origem@empresa.com>;tag=12345
To: <sip:telefone-destino@empresa.com>
Call-ID: 987654321@192.168.1.10
User-Agent: Telefone-IP-Grandstream
````

5. História do Conteúdo

Padronizado no final dos anos 90 (IETF RFC 3261), o SIP nasceu especificamente pela frustração generalizada com o protocolo antigo e pesadíssimo da época (o H.323), que tentava simular as regras matemáticas cruéis e estritas da telefonia física antiga dentro da internet. Os engenheiros criaram o SIP inspirado no sucesso e na fluidez de leitura humana do protocolo HTTP web, adotando uma arquitetura simples para construir o ecossistema telefônico global moderno baseado em softwares como o PABX Asterisk.