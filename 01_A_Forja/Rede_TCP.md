---
tags:
- tipo/conceito
- contexto/dev/infra
- afinidade/media
- status/3_incubadora
---
### Rede_TCP
#### 1. O Axioma (A Definição Rígida)
**O que é:** O TCP (Transmission Control Protocol) é um protocolo da Camada 4 orientado à conexão, que garante que os pacotes de dados cheguem completos, na ordem correta, sem falhas e controlando congestionamentos de rede.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** 
    * Estabelece acordo via *3-Way Handshake* (SYN -> SYN-ACK -> ACK) antes de mandar 1 byte sequer de dados úteis.
    * Quebra a informação em "segmentos", enumerando-os. Exige confirmação (ACK) do recebedor para cada lote enviado (Windowing). Se não receber confirmação, retransmite os dados perdidos.
*   **O Problema que Resolve:** O [[Rede_IP]] subjacente é caótico, roteadores descartam pacotes sem aviso prévio. O TCP tira a responsabilidade do programador de software de checar a integridade, gerando um "tubo confiável virtual" sob uma infraestrutura falha.
*   **Visão Sênior (Vulnerabilidades/Escala):** Lentidão por excesso de zelo. O cabeçalho gordo (20-60 bytes) mais as viagens de confirmação geram latência. Sofre de *Head-of-Line Blocking* (um pacote perdido paralisa a fila inteira). É alvo crônico de *SYN Flood*, onde hackers inundam a porta de escuta do servidor com inícios de handshake falsos (SYN) para estourar o limite de memória.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O TCP atua como um Burocrata Perfeccionista dos Correios via Carta Registrada: ele exige a sua assinatura ao enviar, anota o peso da caixa, e não encerra o serviço enquanto o destinatário não assinar o Aviso de Recebimento. Em jogos online ou em videochamadas, todo esse zelo trava a tela do jogador, motivo pelo qual optam pelo [[Rede_UDP]] (o panfleto atirado de helicóptero). Portas lógicas de rede (como 443 para o HTTPs) são as "caixas de correio" que o TCP usa para separar o tráfego do navegador do tráfego do Spotify simultaneamente (Multiplexação).

#### 4. Pragmatismo Aplicado (Código e Implementação)
Observando o comportamento de portas TCP e sockets ativos. Este é o comando número 1 no dia a dia de Cyber Security e Infraestrutura para debugar serviços caídos:

**No Linux:**
```bash
# Mostrar todas as portas TCP escutando (Listen) e estabelecidas com o processo atrelado
ss -ltnp
````

**No Windows:**

```
# Ver conexões ativas e a porta origem/destino 
netstat -ano | findstr TCP
```

#### 5. História do Conteúdo

Concebido pela DARPA nos anos 1970 para sobrevivência militar. Vint Cerf elaborou o TCP partindo do pressuposto de que as redes de rádio e cabos da época poderiam ser destruídas durante uma transmissão por bombas soviéticas. "O protocolo deve tolerar a falha maciça e tentar novamente até o fim". A resiliência paranóica criada para resistir a ataques nucleares se tornou o motor invisível e incansável que sustenta 90% da internet civil hoje, desde transferências bancárias até o envio seguro desta mesma nota de texto.