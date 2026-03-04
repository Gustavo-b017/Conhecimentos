---
tags:
- tipo/conceito
- contexto/dev/infra
- afinidade/media
- status/3_incubadora
---
### Rede_Hardware
#### 1. O Axioma (A Definição Rígida)
**O que é:** É a infraestrutura física mandatória que manipula bits e rotas; focada no *Switch*, que distribui dados cirurgicamente via MAC em uma rede local (Camada 2), e no *Router*, que despacha pacotes entre redes distintas via IP (Camada 3).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** 
    *   **Hub (Legado/Camada 1):** Recebe energia em uma porta e "grita" replicando para todas as outras (Domínio de colisão gigante). 
    *   **Switch (Camada 2):** Grava o [[Rede_MAC]] de cada máquina em uma tabela. Quando os dados chegam, ele encaminha *apenas* para o cabo/porta do destinatário certo.
    *   **Router (Roteador/Camada 3):** Conecta o switch local ao resto do mundo. Ele ignora o MAC e lê o [[Rede_IP]] para calcular o salto mais curto até outra rede/país. 
*   **O Problema que Resolve:** O gargalo e o caos. Se todos os 500 computadores de uma empresa "gritassem" ao mesmo tempo num mesmo cabo (como era na época dos Hubs), a rede travaria. O Switch isola a conversa, o Router isola o país.
*   **Visão Sênior (Vulnerabilidades/Escala):** Switches são vulneráveis a *loops* infinitos caso dois cabos sejam plugados na mesma rede por acidente (o tráfego fica rodando até derreter a CPU, mitigado pelo Spanning Tree Protocol - STP). Roteadores consomem altíssimo processamento, pois precisam reescrever cabeçalhos e consultar tabelas de dezenas de milhares de rotas em tempo real (ex: tabela BGP da internet global).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O Switch é o carteiro interno do seu prédio corporativo; ele sabe o seu nome exato (MAC) e entrega na sua mesa (Porta) de forma privada, os outros funcionários do andar não vêem a carta. Já o Roteador é o despachante da alfândega; ele não faz ideia de quem você é ou qual sua mesa, ele só olha para o seu país/cidade destino (IP) e despacha a caixa para o próximo aeroporto mais próximo da rota. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
A diferença brutal visualizada em equipamentos Cisco:

```bash
# No SWITCH: Verificando as portas físicas e para qual MAC elas entregam as cartas (Camada 2)
show mac address-table

# No ROUTER: Verificando a tabela de caminhos lógicos para outros países/redes (Camada 3)
show ip route
````

#### 5. História do Conteúdo

A evolução foi puramente pautada na dor do silício. Nos anos 80, usavam-se Hubs. O choque de dados nos fios era literal (colisão elétrica). Se duas pessoas mandassem um e-mail ao mesmo tempo, a voltagem subia e a mensagem corrompia. Tiveram que criar regras matemáticas de espera (CSMA/CD). Nos anos 90, os engenheiros colocaram ASICs (chips específicos) dentro dos aparelhos criando o "Switch", onde a placa-mãe criava um "cano virtual privado" entre a origem e o destino em nanosegundos, aniquilando de vez as colisões e explodindo a velocidade das redes locais.