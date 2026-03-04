---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

### Rede_WLAN_e_WiFi
#### 1. O Axioma (A Definição Rígida)
**O que é:** A Wireless Local Area Network (WLAN) é a extensão de uma rede local que substitui os cabos físicos de transmissão (Ethernet) por ondas de rádio (frequências de 2.4 GHz e 5 GHz), operando através do padrão IEEE 802.11 (Wi-Fi).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Utiliza os chamados Wireless Access Points (WAPs). O WAP atua como uma ponte (Bridge) operando na Camada 2 (Enlace), traduzindo o tráfego da infraestrutura cabeada para sinais de rádio frequência que os adaptadores sem fio (NICs) dos laptops e celulares conseguem ler.
*   **O Problema que Resolve:** A mobilidade e o custo. Elimina a necessidade de passar cabos estruturados caros por dentro das paredes de um prédio para suportar políticas de trabalho flexível (como o BYOD - *Bring Your Own Device*).
*   **Visão Sênior (Vulnerabilidades/Escala):** A WLAN sofre problemas físicos severos, como a interferência eletromagnética e limitações de distância (atenuação). No quesito segurança, é o elo mais fraco da infraestrutura: o sinal de rádio vaza pelas paredes da empresa para a rua. Sem protocolos rigorosos de criptografia (como WPA2 ou o moderno WPA3), qualquer atacante na calçada pode capturar os pacotes e realizar ataques de *Eavesdropping* ou *Man-in-the-Middle*.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se a [[Rede_LAN]] cabeada é uma conversa privada por telefones com fio em salas isoladas, a [[Rede_WLAN_e_WiFi]] é um **palestrante gritando com um megafone em uma praça pública**. Todas as pessoas num raio de 50 metros (inclusive os espiões) ouvem exatamente a mesma mensagem (o meio de transmissão é compartilhado). Para manter a confidencialidade no meio da praça, o palestrante e seus convidados precisam falar num dialeto criptografado inquebrável (WPA3).

#### 4. Pragmatismo Aplicado (Código e Implementação)
Para auditar pelo terminal o status da sua interface de rede sem fio e o padrão de rádio associado:
**No Linux:**
```bash
iwconfig
# Mostrará a interface (ex: wlan0), o padrão IEEE (ex: 802.11ac) e a qualidade do link em dBm.
````

5. História do Conteúdo

O precursor do Wi-Fi moderno foi o ALOHAnet, criado em 1971 na Universidade do Havaí. Como as ilhas havaianas não podiam ser facilmente conectadas por cabos de cobre através do oceano e das montanhas vulcânicas, os pesquisadores forjaram a primeira rede de computadores baseada em UHF para transmitir dados pelo ar. A genialidade desse modelo pavimentou o caminho para a criação da Ethernet local e, décadas depois, do protocolo 802.11.