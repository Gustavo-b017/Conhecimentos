---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_CSMA_CD
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Carrier Sense Multiple Access with Collision Detection (CSMA/CD) é o algoritmo clássico de controle de acesso à mídia utilizado pelo Ethernet na Camada de Enlace para governar como dispositivos compartilham o mesmo cabo elétrico sem corromper as transmissões uns dos outros.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** 
    1. A máquina "escuta" o cabo para ver se há corrente elétrica de dados passando (Carrier Sense).
    2. Se estiver vazio, ela transmite.
    3. Se duas máquinas transmitirem no exato mesmo milissegundo, ocorre um pico de voltagem que corrompe o dado (Colisão).
    4. As placas detectam a anomalia (Collision Detection), enviam um sinal de cancelamento (Jam Signal) e aguardam um tempo aleatório (*Backoff Algorithm*) antes de tentar de novo.
*   **O Problema que Resolve:** Evita que a rede local (LAN) se transforme num caos elétrico ilegível em topologias baseadas em Hubs, onde apenas um computador pode falar de cada vez (Half-Duplex).
*   **Visão Sênior (Vulnerabilidades/Escala):** Em infraestruturas cabeadas modernas (que utilizam Switches e comunicação Full-Duplex), colisões são fisicamente impossíveis, tornando o CSMA/CD **obsoleto**. Contudo, o seu "irmão gêmeo", o **CSMA/CA** (Collision Avoidance), é a base absoluta de toda a tecnologia sem fio hoje ([[Rede_WLAN_e_WiFi]]), pois o ar é um meio compartilhado onde equipamentos não podem escutar e transmitir rádio ao mesmo tempo.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O funcionamento do [[Rede_CSMA_CD]] é idêntico a uma **reunião de negócios sem um moderador em uma sala escura**. Todo mundo na sala está calado. Você escuta o ambiente; se ninguém estiver falando, você começa a falar. Se você e o seu colega começarem a falar a primeira sílaba ao mesmo tempo (Colisão), ambos calam a boca imediatamente e, mentalmente, escolhem um número aleatório de segundos antes de tentar abrir a boca novamente para que o choque não se repita.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O diagnóstico de falhas de CSMA/CD em redes cabeadas obsoletas ou problemas de duplex mismatch é feito lendo os contadores de colisão da interface do equipamento:
```bash
# Verificando estatísticas de placa de rede no Linux
ifconfig eth0 | grep collisions
# Se o número de colisões for maior que 0 em uma rede moderna com Switch, 
# a porta física está configurada errada (Half-Duplex forçado).
````

5. História do Conteúdo

O conceito CSMA evoluiu diretamente do ALOHAnet (a primeira rede sem fio do Havaí) para o protocolo Ethernet a cabo desenhado por Bob Metcalfe na Xerox PARC nos anos 70. Nos anos 80 e 90, os Hubs baratos inundaram as empresas, e o CSMA/CD foi a única "gambiarra matemática" que permitiu que o mundo conectasse computadores sem que a eletricidade dos cabos entrasse em colapso, até a chegada do [[Rede_Hardware]] isolado (O Switch).