---
tags:
- tipo/conceito
- contexto/dev/infra
- afinidade/media
- status/3_incubadora
---
### Rede_MAC
#### 1. O Axioma (A Definição Rígida)
**O que é:** O MAC (Media Access Control) é um endereço físico, imutável e exclusivo de 48 bits gravado no hardware da placa de rede (NIC). Ele atua na Camada 2 (Enlace) para garantir a entrega de dados entre dispositivos no mesmo segmento físico de rede.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** 
    * O dispositivo emissor encapsula os dados em um *Frame* que contém o MAC de origem e o MAC de destino.
    * Switches (equipamentos de Camada 2) leem o MAC de destino e enviam o pulso elétrico/óptico apenas para a porta física correta, isolando colisões.
*   **O Problema que Resolve:** O roteamento lógico (IP) leva a informação até o prédio correto, mas era impossível saber qual placa de silício específica conectada aos cabos daquele andar deveria processar os bits. O MAC resolve a entrega final local.
*   **Visão Sênior (Vulnerabilidades/Escala):** Inseguro por design. É vulnerável a *MAC Spoofing* (onde um atacante clona via software o endereço físico de uma máquina legítima para burlar filtros) e *MAC Flooding* (onde milhares de MACs falsos são injetados para travar a tabela de memória do switch, forçando-o a vazar tráfego para todas as portas como um *hub* burro).  

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O MAC é o chassi do veículo cravado no metal, enquanto o [[Rede_IP]] é a placa de licença atrelada à cidade atual. Se você viaja com seu laptop, o "chassi" (MAC) permanece o mesmo, mas sua "placa" (IP) muda. Na gastronomia, o MAC atua como o selo de "Denominação de Origem Controlada" de um Champagne original, indicando irrevogavelmente a fábrica de onde aquele chip saiu. Sem o [[Rede_ARP]], seria impossível para a rede lógica IP encontrar esse chassi físico.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Para extrair e analisar o endereço físico (MAC) das placas de rede no terminal local:

**No Windows:**
```powershell
ipconfig /all | findstr "Physical Address"
````

**No Linux:**

```
ip link show
# Ou filtrando por MACs conectados via protocolo ARP na rede:
ip -s -s neigh
```

5. História do Conteúdo

Concebido na década de 1970 no laboratório da Xerox PARC durante a criação da rede Ethernet. Nos primórdios, os computadores eram todos conectados a um único cabo coaxial longo (topologia de barramento). Quando um PC transmitia, a corrente elétrica atingia todos os outros ao mesmo tempo (gritaria total). Eles criaram o MAC de 48 bits para que, quando a energia entrasse na placa, o hardware se perguntasse em nanossegundos: _"Esse código de 48 bits é o meu? Não? Então ignoro."_ O comprimento foi escolhido visando um número de combinações que não se esgotasse por mais de um século.