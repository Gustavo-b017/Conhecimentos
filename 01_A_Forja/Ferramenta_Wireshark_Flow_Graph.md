---
tags:
  - tipo/ferramenta
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Ferramenta_Wireshark_Flow_Graph

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Flow Graph (Gráfico de Fluxo) é uma ferramenta do Wireshark que gera uma representação visual interativa e cronológica em formato de diagrama de escada (Sequence Diagram), mapeando o fluxo interativo das comunicações entre diferentes nós da rede.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Coloca os endereços IPs envolvidos no topo como colunas verticais. Conforme o tempo avança de cima para baixo na tela esquerda, flechas horizontais disparam de um IP para o outro, detalhando exatamente qual flag ou requisição transitou (ex: requisição [[Rede_TCP_Flags_e_Header|TCP SYN]], requisição Client Hello do [[Rede_TLS]]).
*   **O Problema que Resolve:** Resolve a complexidade mental de reconstruir conversas TCP/IP mentalmente. Ver 5 linhas de texto bruto no painel principal exige enorme carga cognitiva. Ver uma "seta de ida e uma seta de volta com um erro vermelho no meio" atesta graficamente o ponto de falha exato daquela sessão de banco de dados.
*   **Visão Sênior (Vulnerabilidades/Escala):** Desenhar o gráfico exige muito processamento gráfico (RAM). Se um analista tentar rodar um Flow Graph sem antes aplicar um Filtro de Exibição (Display Filter) rigoroso, limitando a análise apenas a dois IPs de interesse, o Wireshark tentará plotar milhões de setas de toda a internet simultaneamente e inevitavelmente causará o travamento completo (Crash) do aplicativo pericial na máquina de análise.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O Flow Graph é o **Replay Tático com desenho de setas num programa esportivo**. Em vez de você ler um texto corrido dizendo "o jogador A passou a bola para B que perdeu para C", você olha a lousa do técnico. O IP de origem envia a seta com o TCP SYN; se o destino demorar mais de 30 milissegundos para devolver o SYN-ACK, você enxerga perfeitamente a [[Rede_Latencia|latência]] temporal grafada no meio do espaço em branco da tela, provando a emboscada na rede.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O analista isola primeiramente uma conversa de interesse na interface de texto (Follow TCP Stream) para depois exigir a renderização do fluxo:
```text
# Menu Path prático após a aplicação de um filtro como (ip.addr == 192.168.1.5 and tcp.port == 443):
Statistics -> Flow Graph
# Dica Sênior: Selecione "Limit to display filter" para não travar seu computador renderizando o lixo da rede.
````

5. História do Conteúdo

Os diagramas de sequência foram inicialmente padronizados na engenharia de software pela UML (Unified Modeling Language) nos anos 1990. Os desenvolvedores do Wireshark apenas "emprestaram" a clareza inegável do diagrama de UML dos programadores e a aplicaram de forma dinâmica na leitura matemática dos pacotes crús de rede, revolucionando a análise forense de incidentes.