---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_DWDM_e_ROADM

#### 1. O Axioma (A Definição Rígida)
**O que é:** O DWDM (Dense Wavelength Division Multiplexing) é a tecnologia fotônica que multiplica a capacidade de uma fibra óptica ao injetar múltiplos comprimentos de onda (lasers de cores diferentes) simultaneamente. O ROADM (Reconfigurable Optical Add-Drop Multiplexer) é o switch analógico que desvia e roteia essas luzes pela malha óptica sem convertê-las em sinais elétricos.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Transponders convertem o tráfego elétrico (Ethernet/OTN) em uma onda de luz padrão ITU-T (Conversão E-O). Esses múltiplos canais de luz viajam juntos pela mesma fibra. Em nós intermediários, os ROADMs interceptam a fibra óptica e decidem fisicamente se a cor de um laser passa direto (Express) ou se deve ser "desembarcada" na cidade (Drop) e convertida de volta para sinal elétrico (O-E)
*   **O Problema que Resolve:** O lançamento de cabos ópticos subterrâneos e submarinos custa bilhões. O DWDM e os ROADMs aumentam virtualmente a capacidade da rede de forma ilimitada mexendo apenas nas pontas, provendo roteamento passivo e fotônico por software.
*   **Visão Sênior (Vulnerabilidades/Escala):** A física cobra seu preço. Quando a luz viaja, o sinal sofre com a dispersão cromática e atenuação, exigindo a instalação em cascata de amplificadores EDFA ópticos, que inevitavelmente introduzem ruído não linear e reduzem o índice de qualidade OSNR (Optical Signal-to-Noise Ratio). Para matar a necessidade do hardware externo de transponder, a arquitetura de ponta atual é a **CORA (Converged Optical Routing Architecture) / IPoDWDM**, que ploga conectores coerentes de 400G/800G diretamente na porta do Roteador IP, colapsando a camada 1 e 3 para reduzir o TCO pela metade.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O cabo fotônico DWDM é uma **Rodovia de 100 faixas superpostas ocupando o espaço de apenas uma faixa**, onde cada "carro" viaja usando uma frequência de luz de cor sutilmente diferente. O ROADM é o **Viaduto Analógico**. Antigamente, num roteamento comum, o carro teria que frear no pedágio (conversão óptico-elétrica), o cobrador leria a placa, e o carro aceleraria novamente. O ROADM simplesmente entende que o carro é da "cor verde" e aciona um prisma refletor para jogá-lo numa alça de saída em tempo real, sem que o pacote perca um milissegundo de velocidade.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Não há linha de comando genérica para manipular ondas de luz fotônica brutas (varia dramaticamente entre fornecedores como Ciena, Infinera ou Juniper). Porém, ao desenhar topologias lógicas, engenheiros modelam a perda baseada na atenuação. Um caminho via ROADM requer o cálculo do OSNR para garantir que a luz consiga ser "lida" na chegada, utilizando módulos de planejamento de rede para evitar erros de BER (Bit Error Rate) não tratáveis.

#### 5. História do Conteúdo
Nasceu da crise de infraestrutura global de telecom dos anos 90. Antes, cada feixe de luz precisava de um cabo inteiro. Se a operadora quisesse mandar outro fluxo de dados entre SP e NY, navios tinham que jogar mais cabos no oceano. O advento do DWDM permitiu modular dezenas (e hoje, centenas) de comprimentos de onda diferentes, espremendo 800 Gbps com modulações como QAM e PAM4 num mesmo filamento de vidro mais fino que um fio de cabelo.