---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Rede_Network_Slicing

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Fatiamento de Rede (Network Slicing) é a supercapacidade ponta a ponta do 5G de instanciar redes lógicas e independentes orquestradas através do mesmo meio físico, garantindo matematicamente isolamento de dados e Acordos de Qualidade (SLA) imutáveis de banda, latência e segurança.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Quando um chip conecta, a Função Mestra do core 5GC (NSSF - Network Slice Selection Function) decide a qual fatia o pacote pertence através do Identificador da Fatia (S-NSSAI). Se ele for de telemedicina, o pacote ganha prioridade no escalonamento do ar na antena (RAN), entra numa rota isolada e pré-calculada por engenharia no asfalto óptico (via [[Rede_Flex_Algo]] ou [[Rede_Segment_Routing_SRv6]]) e vai ancorar em instâncias dedicadas de Core (AMF e UPF) que atendem *apenas àquele hospital*.
*   **O Problema que Resolve:** No passado "Melhor Esforço", existia uma vala comum e o congestionamento generalizado atingia a todos (você não assistia ao seu Netflix em HD na rodoviária entupida, e o terminal POS da empresa logística do lado também caía junto). O Fatiamento separa as topologias lógicas e permite monetizar as três classes nativas em paralelos imutáveis: Muito Banda (eMBB), Microlatência (URLLC), Muita Densidade Elétrica (mMTC).
*   **Visão Sênior (Vulnerabilidades/Escala):** A fraqueza na vida real está no perigo do "Soft Slicing". Apenas priorizar filas (QoS via QoS Flows) no software não isola o buffer do silício. O verdadeiro **Hard Slicing** requer isolamento no metal nos links da fibra metropolitana (via Transporte TSN ou Time-Division como [[Rede_FlexE]]) blindando o canal de luz L1. Se houver "Vizinhos Barulhentos" que saturem a placa do roteador na entrada, o tráfego da Cirurgia Robótica URLLC sofre variações imprevistas e o carro autônomo esmaga seu prazo de tolerância fatal de 1 milissegundo.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Network Slicing é a verdadeira **Rodovia Inteligente Comissionada**. As velhas redes (4G/Fibra Best Effort) eram o trânsito clássico em São Paulo: ambulâncias, Ferraris e tratores batendo cabeça nas mesmas filas e buracos. O fatiamento inteligente de Transporte desenhou uma utopia: A pista da direita é apartada com muros elétricos e não tem limites, só andam os dados de missão crítica (URLLC). A pista da esquerda é o escoamento bruto diário para dezenas de gigantes caminhões (eMBB). A canaleta secundária recebe milhões de motoboys frenéticos transportando gramas de carga de pequenos lojistas (mMTC e medidores residenciais IoT). Tudo ancorado e financiado em cima do mesmíssimo asfalto cinza de vidro óptico, construído com o mesmo maquinário e investimento da operadora primária.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Fatiamento ponta a ponta exige configuração e amarração de QoS/Tags desde as regras NSSF nos roteadores de transporte físico na WAN. Nos provedores de alta capacidade usando Segment Routing e Flex-Algo (IOS-XR):

```bash
# Declarando a Fatia URLLC e acoplando seu roteamento base ao Algoritmo de "Mínimo Atraso (Delay) 128"
network-slicing
 profile 1
  description CIRURGIA_URLLC_HOSPITAL
  transport srv6 flex-algorithm 128
````

5. História do Conteúdo

Embora abordado em projetos anteriores, o fatiamento real ganhou existência normativa e pragmática no Release 15 de 2018 (3GPP). A indústria entendeu que a única forma de telecomunicações competir pelo capital corporativo massivo do B2B e da Indústria 4.0 era vendendo a garantia contratual em SLA, fornecendo conectividade premium separada da multidão frenética da internet residencial sob o paradigma "Network as a Service".