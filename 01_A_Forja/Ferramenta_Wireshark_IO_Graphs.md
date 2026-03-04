---
tags:
  - tipo/ferramenta
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Ferramenta_Wireshark_IO_Graphs

#### 1. O Axioma (A Definição Rígida)
**O que é:** Os I/O Graphs (Input/Output) formam um painel de visualização bidimensional do Wireshark que plota métricas brutas de transferência de dados (Pacotes ou Bits por Segundo) contra o tempo, atestando picos e quedas súbitas da rede de forma imediata.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Traça o tráfego como um gráfico de linhas contínuo. O eixo X é o tempo absoluto (em segundos) da gravação; o eixo Y mostra os Bytes ou Pacotes. Permite sobrepor cores diferentes utilizando filtros avançados (ex: Linha Verde para o tráfego total, Linha Vermelha sobreposta apenas para erros TCP).
*   **O Problema que Resolve:** Evidencia ataques volumétricos e gargalos físicos de infraestrutura na força bruta. Sem esse gráfico, um ataque [[Cyber_Ataque_DDoS]] passaria como tráfego normal intenso nas linhas de texto. O gráfico expõe a "Parede de Volume", um pico quase vertical impossível de ser gerado legitimamente pelo tráfego humano.
*   **Visão Sênior (Vulnerabilidades/Escala):** A genialidade para os Blue Teams (defesa) e caçadores de anomalias é a capacidade de suavizar os gráficos utilizando o "Tick Interval" (frações de tempo). Observar a taxa de I/O em janelas de 1 segundo pode ocultar exfiltrações curtas; reduzir o cálculo do gráfico para 0.01 segundos revela micro-picos causados por malwares automatizados que operam em rajadas invisíveis aos olhos humanos.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O I/O Graph é o **Eletrocardiograma (ECG) rítmico do paciente**. Enquanto a "Hierarquia de Protocolos" faz a autópsia macro da rede, o gráfico I/O observa o batimento no leito da UTI. Se a linha do gráfico estiver flutuando calmamente e, de repente, entrar em um estado ininterrupto no topo do quadro (Taquicardia Digital), a porta da rede está sendo brutalmente estrangulada e exige o disparo de uma intervenção tipo "Reset" (RST).

#### 4. Pragmatismo Aplicado (Código e Implementação)
A auditoria visual comparativa baseia-se em mapear erros da rede perante a carga de tráfego usando Display Filters diretamente nas configurações das linhas do gráfico:
```wireshark
# Caminho: Statistics -> I/O Graphs
# Configuração Letal de Gráfico Duplo:
Graph 1: Y Axis (Packets/s). Filtro: tcp
Graph 2: Y Axis (Packets/s). Filtro: tcp.analysis.retransmission (Cor Vermelha).
# Se a curva vermelha acompanhar o pico da linha de tráfego, o link físico da empresa entrou em colapso.
````

5. História do Conteúdo

Embutido como uma ferramenta fundamental para monitoramento visual quando a engenharia de redes precisou correlacionar reclamações verbais ("A internet está lenta hoje às 14h") com provas matemáticas ("Aqui está o gráfico provando que às 14h a sua máquina baixou a ISO inteira de um jogo de 100GB, saturando o roteador"). Substituiu o achismo corporativo pela incontestabilidade pericial.