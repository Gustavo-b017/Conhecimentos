---
tags:
- tipo/conceito
- contexto/dev/infra
- afinidade/media
- status/3_incubadora
---

### Rede_UDP
#### 1. O Axioma (A Definição Rígida)
**O que é:** O UDP (User Datagram Protocol) é um protocolo da Camada 4 (Transporte) não orientado à conexão. Ele atira datagramas na rede com esforço máximo ("best-effort"), priorizando velocidade e baixo custo computacional sobre a confiabilidade e garantia de entrega.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** 
    * Não realiza o *3-Way Handshake* (SYN, SYN-ACK, ACK). Simplesmente empacota o dado e envia.
    * O cabeçalho é minúsculo (apenas 8 bytes, contra 20-60 bytes do TCP), contendo apenas portas de origem/destino, comprimento e checksum.
    * Não retransmite pacotes perdidos, não reordena pacotes que chegam fora de ordem e não controla congestionamento.
*   **O Problema que Resolve:** O [[Rede_TCP]] é lento demais para comunicações em tempo real. O UDP resolve a necessidade de transmitir fluxos contínuos onde perder uma fração de segundo de dado é melhor do que pausar tudo para recuperar a perda.
*   **Visão Sênior (Vulnerabilidades/Escala):** É o vetor favorito para ataques volumétricos (DDoS). Como não há checagem de conexão (handshake), é trivial falsificar o IP de origem (IP Spoofing) em pacotes UDP. Atacantes mandam requisições UDP falsas para servidores DNS/NTP, que respondem com pacotes gigantescos para a vítima (Ataques de Amplificação e Reflexão).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se o [[Rede_TCP]] é uma Carta Registrada com Aviso de Recebimento, o UDP é atirar panfletos de um helicóptero: é barato, imediato e atinge o alvo rápido, mas você nunca saberá exatamente quais panfletos caíram no rio e quem os leu. Na gastronomia, o UDP é o *Fast Food* no horário de pico: o hambúrguer sai rápido; se faltou uma batata frita, não vão parar a esteira para consertar. É usado para streaming de vídeo, VoIP (Discord/Skype), jogos online e consultas [[Rede_DNS]] (pela rapidez). 

#### 4. Pragmatismo Aplicado (Código e Implementação)
Para escutar ativamente o tráfego UDP em um servidor ou debugar portas abertas:

**No Linux:**
```bash
# Mostra todas as portas UDP (-u) ouvindo (-l) numericamente (-n) e os processos (-p)
ss -unlp
````

**Para testar se uma porta UDP está aberta (Netcat):**

```
nc -u -v -z 8.8.8.8 53
```

5. História do Conteúdo

Criado por David P. Reed em 1980 (RFC 768). Durante os primórdios do desenvolvimento da internet, percebeu-se que o TCP (o único protocolo de transporte da época) era rígido demais. Reed estava projetando sistemas experimentais de voz e os atrasos causados pelas retransmissões do TCP tornavam a fala humana ininteligível ("efeito robô gaguejando"). O UDP foi forjado como uma rebelião à burocracia do TCP, permitindo que a aplicação decidisse como lidar com as perdas, em vez do sistema operacional.