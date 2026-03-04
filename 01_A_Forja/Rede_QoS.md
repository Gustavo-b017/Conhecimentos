---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/4_evergreen
---

### Rede_QoS
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Quality of Service (QoS) é um conjunto de tecnologias preventivas e algoritmos que gerenciam a capacidade da rede, classificando, marcando e priorizando ativamente tráfego sensível (como voz e vídeo) em detrimento de dados menos urgentes.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Emprega um sistema triplo: **1. Classificação** (Identifica o que é o pacote), **2. Marcação** (Carimba o cabeçalho IP usando DSCP - Differentiated Services Code Point) e **3. Enfileiramento** (Queuing, criando "faixas VIPs" no gargalo do roteador).
*   **O Problema que Resolve:** O congestionamento cego e o *Jitter* (variação de atraso). Se a rede engarrafar, o roteador padrão (que é socialista) descarta os pacotes aleatoriamente. Se descartar um pedaço de um e-mail TCP, o e-mail é reenviado. Se descartar um pedaço da sua ligação [[Rede_VoIP]] UDP, a voz do cliente fica robotizada. O QoS garante que o e-mail espere enquanto a voz passa.
*   **Visão Sênior (Vulnerabilidades/Escala):** O maior mito da TI: "QoS cria largura de banda". Falso. QoS apenas dita **quem deve morrer primeiro** na fila do congestionamento. Além disso, políticas de QoS não sobrevivem à internet pública (WAN). Assim que seu pacote marcado VIP sai da sua empresa e entra no roteador do provedor de internet, o provedor rasga a sua etiqueta de prioridade e a joga no tráfego genérico, forçando o uso de SD-WAN ou links MPLS dedicados para manter a garantia fim a fim.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O QoS é exatamente a mecânica de uma **Fila de Sala de Emergência em um Hospital**. Se o hospital está vazio, todos são atendidos imediatamente (Rede sem congestionamento). Se há um desastre e a recepção lota, o enfermeiro (O Roteador) não atende as pessoas por ordem de chegada (FIFO). Ele faz a Triagem (Classificação), amarra uma pulseira vermelha, amarela ou verde no pulso (Marcação DSCP) e coloca os baleados na frente dos resfriados (Enfileiramento/Policing). O arquivo PDF do RH é o paciente resfriado; a ligação do CEO é o paciente baleado.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação em roteadores corporativos segue o modelo MQC (Modular QoS CLI) da Cisco. Exemplo forçando a rede a reservar 30% da banda vitalícia de uma interface exclusivamente para tráfego de vídeo:
```bash
policy-map GARANTIA_DE_VIDEO
 class TRAFEGO_MARCADO_COMO_VIDEO
  # Garante 30% do cano apenas para as videoconferências, mesmo que o sistema de backup queira os 100%
  bandwidth percent 30 
````

5. História do Conteúdo

Nos primórdios da internet, o modelo era "Best Effort" (Melhor Esforço). Redes de voz eram cabos de telefone (PABX físicos), e redes de dados eram cabos de computador (Ethernet). Quando as corporações decidiram baratear os custos e jogar o telefone por dentro do cabo de rede do computador (nascimento do VoIP), as ligações telefônicas ficaram ininteligíveis. A engenharia foi forçada a criar regras ditatoriais de priorização para evitar que o download de um MP3 destruísse reuniões de diretoria