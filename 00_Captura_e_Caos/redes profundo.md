Pilar 1: Transporte Óptico e A Física da Luz (A Base)

As redes não rodam no ar, rodam em vidro. As fontes fornecem a base do padrão ITU-T G.709. Precisamos forjar:

- [x] **Rede_DWDM_e_ROADM**: O axioma de como multiplexamos cores (comprimentos de onda) na mesma fibra e como os ROADMs desviam luz sem conversão elétrica.
- [x] **Rede_OTN**: O padrão G.709 (Digital Wrapper). A diferença entre ODU, OTU e OPU, e o salvador Forward Error Correction (FEC).
- [x] **Rede_FlexE**: A "gambiarra" genial (Shim layer) que permite fatiar ou agregar portas Ethernet físicas (ex: usar 50G de uma porta de 100G) para mapear eficientemente no OTN.

Pilar 2: Sincronismo e o Relógio da Rede

Sem isso, o 5G cai e o mercado financeiro colapsa.

- [x] **Rede_PTP_1588**: O Precision Time Protocol. O axioma de como sincronizamos Fase e Tempo em nanossegundos via pacotes IP, e os papéis dos Grandmaster, Boundary e Transparent Clocks.
- [x] **Rede_SyncE**: O Synchronous Ethernet. Como a própria pulsação elétrica da porta física garante o sincronismo de Frequência, servindo de base para o PTP.

Pilar 3: O Novo Roteamento Global (Segment Routing)

A morte do MPLS tradicional e do RSVP-TE. A ascensão do roteamento na origem.

- [x] **Rede_Segment_Routing_SRv6**: O uso do próprio cabeçalho IPv6 (SRH) para ditar o caminho do pacote instrução por instrução, matando a necessidade de protocolos legados como LDP.
- [x] **Rede_SRv6_uSID**: A otimização (Micro-SID). O SRv6 puro gasta muita banda com cabeçalhos gigantes; o uSID comprime essas instruções para caber nas limitações do silício dos roteadores.
- [x] **Rede_Flex_Algo**: Como criamos "dimensões paralelas" no OSPF/IS-IS. (Ex: O tráfego de vídeo usa o mapa de "menor latência", o tráfego de e-mail usa o mapa de "menor custo").
- [x] **Rede_TI_LFA**: Topology-Independent Loop-Free Alternate. A magia matemática que garante a recuperação de um link rompido em menos de 50 milissegundos, antes mesmo da rede perceber que caiu.

Pilar 4: Telco Cloud e Redes Móveis (5G)

Como transformar antenas de celular em instâncias de Kubernetes.

- [x] **Rede_5G_SBA**: Service-Based Architecture. O fim das caixas pretas de telecom. O Core do 5G (AMF, SMF) rodando via APIs, HTTP/2 e microsserviços.
- [x] **Rede_5G_CUPS_e_UPF**: A separação cérebro/músculo (Control and User Plane Separation). A User Plane Function (UPF) despachando o tráfego pesado do usuário na borda com ultra-baixa latência.
- [x] **Rede_O_RAN**: Open RAN. A quebra das antenas proprietárias em Fronthaul, Midhaul e Backhaul (RU, DU e CU), virtualizando o rádio.
- [x] **Rede_Network_Slicing**: O produto final que junta tudo. Vender uma fatia isolada de ponta a ponta (do rádio ao roteador SRv6) com garantia de banda para um carro autônomo ou indústria.

Pilar 5: Programabilidade de Borda e Qualidade

O software controlando o silício.

- [x] **Rede_P4_Lang**: A linguagem de programação que permite reescrever como o chip (ASIC) do switch processa pacotes no nível atômico, sem trocar o hardware.
- [x] **Rede_QoS_Avancado**: Diferenciar LLQ (Low Latency Queuing) de CBWFQ (Class-Based Weighted Fair Queuing) e entender buffers como VOQ (Virtual Output Queues) para evitar engarrafamentos no switch.

Pilar 6: Segurança de Acesso e Balanceamento em Nuvem

A borda final e a entrega segura da aplicação.

- [x] **Rede_GSLB**: Global Server Load Balancing. Como usar Anycast, verificações de saúde e peso geográfico para jogar o usuário para a nuvem mais próxima e viva.
- [x] **Cyber_SDA_SGT**: Software-Defined Access e Security Group Tags. A evolução do NAC clássico (802.1X). Marcar o usuário com uma tag de segurança (SGT) dentro do pacote VXLAN para garantir isolamento (Microsegmentação).
- [x] **Cyber_Diameter**: A evolução do protocolo RADIUS, focado em alta disponibilidade e usado agressivamente para AAA (Autenticação, Autorização e Contabilidade) e bilhetagem no coração das redes 4G/5G.