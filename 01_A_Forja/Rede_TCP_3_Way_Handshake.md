---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

### Rede_TCP_3_Way_Handshake
#### 1. O Axioma (A Definição Rígida)
**O que é:** O TCP 3-Way Handshake é o processo obrigatório de três etapas (SYN, SYN-ACK, ACK) exigido para estabelecer uma conexão confiável e sincronizada entre um cliente e um servidor antes de qualquer byte de dados reais ser transferido.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** 
    *   **Passo 1 (SYN):** O cliente envia um pacote com a flag SYN (Synchronize) ativa e um Número de Sequência Inicial (ISN) randômico propondo a conexão. O estado do cliente vai para `SYN-SENT`.
    *   **Passo 2 (SYN-ACK):** O servidor, que estava ouvindo (`LISTEN`), recebe o pedido, reconhece o ISN do cliente (ACK) e envia o seu próprio ISN (SYN). O estado do servidor vai para `SYN-RECEIVED`.
    *   **Passo 3 (ACK):** O cliente confirma o recebimento do ISN do servidor com um último ACK. Ambos entram no estado `ESTABLISHED` e a transferência de dados inicia.
*   **O Problema que Resolve:** Garante que ambos os lados estão vivos, acessíveis e prontos para conversar, além de sincronizar os números de sequência para que pacotes perdidos ou fora de ordem possam ser reorganizados corretamente.
*   **Visão Sênior (Vulnerabilidades/Escala):** É o calcanhar de Aquiles do TCP. Um atacante pode realizar um ataque de *SYN Flood (DDoS)*, enviando milhares de solicitações SYN falsas e nunca respondendo com o ACK final. O servidor aloca memória RAM para cada "meia-conexão" (half-open) até travar. A mitigação arquitetural para isso é forçar o uso de *SYN Cookies* no servidor, aliviando a alocação de estado na memória.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O 3-way handshake é exatamente um aperto de mão cerimonial de negócios. Você estende a mão e diz *"Olá, sou o João"* (SYN). A outra pessoa aperta sua mão e diz *"Olá João, entendi, eu sou a Maria"* (SYN-ACK). Você sorri e finaliza *"Prazer em conhecê-la, Maria"* (ACK). Ferramentas de segurança como o [[Rede_Nmap]] quebram esse protocolo de propósito: eles fazem o "Half-Open Scan" (-sS), enviando apenas o SYN. Quando o servidor envia o SYN-ACK, o Nmap envia um RST (Reset) cortando a conversa na cara do servidor. Ele descobre que a porta está aberta sem registrar uma conexão completa nos logs de auditoria.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Para diagnosticar falhas de handshake (ex: o servidor não está respondendo) ou ver o estado real das conexões na sua máquina:
**No Linux (listar conexões ativas):**
```bash
# Mostra processos em estado ESTABLISHED e LISTEN
ss -ltnp
````

_Se você notar milhares de IPs presos no estado_ _SYN-RECV__, seu servidor está sofrendo um ataque DDoS de SYN Flood neste momento._

5. História do Conteúdo

Surgido junto com o TCP original, a criação desse aperto de mão meticuloso reflete a desconfiança inerente dos engenheiros da ARPANET com a infraestrutura física. A premissa era: "Cabos falham e roteadores queimam. Não mande dados úteis até ter a confirmação matemática absoluta de que a máquina de destino existe, está ligada e concorda em nos ouvir." Trocaram a velocidade de início de comunicação pela garantia paranoica de resiliência.