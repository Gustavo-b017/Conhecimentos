---
tags:
- tipo/conceito
- contexto/dev/infra
- afinidade/media
- status/3_incubadora
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/baixa
  - status/4_evergreen
---

# Rede_Hardware

## 1. O Axioma (A Definição Rígida)
> **O que é:** A distinção física e lógica entre os equipamentos que movem os dados: Hub (L1 - Burro), Switch (L2 - Inteligente local) e Roteador (L3 - Inteligente global).

## 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Hub:** Repete o sinal para todos. Gera colisão. (Obsoleto).
*   **Switch:** Aprende [[Rede_MAC]]. Cria circuitos dedicados (ASICs). Alta velocidade. Base da topologia Estrela. É aqui que as [[Rede_VLAN]]s residem.
*   **Roteador:** Toma decisões baseadas em [[Rede_IPv4]]/IP. Conecta redes diferentes (LAN com WAN). Baseado em CPU (mais lento que Switch). É o motor do [[Rede_Roteamento]].
* **Visão Sênior (Vulnerabilidades/Escala):** Switches L3 (Multilayer) borram a linha, fazendo roteamento na velocidade do hardware. O gargalo físico (Backplane) do switch é onde redes de alta performance morrem.

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
*   **Hub:** Um megafone numa praça. Todos ouvem tudo.
*   **Switch:** Um sistema de tubos pneumáticos direto para a mesa da pessoa certa.
*   **Roteador:** O correio internacional que sabe como mandar o pacote para a China.

## 4. Pragmatismo Aplicado (Código e Implementação)
Identificar o hardware vizinho via protocolo de descoberta (CDP/LLDP).
```bash
# Cisco: Ver vizinhos conectados (descobre se é switch ou roteador)
show cdp neighbors detail
```

# No ROUTER: Verificando a tabela de caminhos lógicos para outros países/redes (Camada 3)
show ip route
````

#### 5. História do Conteúdo

A evolução foi puramente pautada na dor do silício. Nos anos 80, usavam-se Hubs. O choque de dados nos fios era literal (colisão elétrica). Se duas pessoas mandassem um e-mail ao mesmo tempo, a voltagem subia e a mensagem corrompia. Tiveram que criar regras matemáticas de espera (CSMA/CD). Nos anos 90, os engenheiros colocaram ASICs (chips específicos) dentro dos aparelhos criando o "Switch", onde a placa-mãe criava um "cano virtual privado" entre a origem e o destino em nanosegundos, aniquilando de vez as colisões e explodindo a velocidade das redes locais.
## 5. História do Conteúdo
A evolução do silício permitiu que switches fizessem o trabalho de roteadores, criando a categoria "Layer 3 Switch", essencial para Data Centers modernos.