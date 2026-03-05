---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Cyber_Firewall_PacketFilter
#### 1. O Axioma (A Definição Rígida)
**O que é:** O firewall de filtro de pacotes (Stateless) é a linha de defesa mais rudimentar de uma rede, analisando pacotes de dados de forma estrita e individual para permitir ou bloquear o tráfego baseando-se apenas em regras predefinidas de endereço [[Rede_IP]], portas e protocolos.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ele lê exclusivamente os cabeçalhos das [[Rede_Camada_Internet|Camada 3]] (Rede) e [[Rede_Camada_Transporte|Camada 4]] do [[Rede_Modelo_OSI]]. Ele checa a lista de controle de acesso (ACL) de cima para baixo. Bateu com a regra de bloqueio? Descarta o pacote. Bateu com a de permissão? Deixa passar.
*   **O Problema que Resolve:** Permite o isolamento primitivo e veloz de [[Rede_Subnet|sub-redes]] e o bloqueio de origens conhecidas maliciosas sem consumir quase nenhum recurso de processamento ([[Hardware_CPU|CPU]]).
*   **Visão Sênior (Vulnerabilidades/Escala):** Ele é "Stateless" (não possui estado/memória). Ele não sabe se um pacote de entrada é a resposta de um pedido que você fez ou um ataque aleatório. Para a internet funcionar, você é obrigado a deixar milhares de [[Rede_Portas_Logicas|portas]] permanentemente abertas para o tráfego de retorno, criando uma superfície de ataque colossal. Além disso, é cego a ataques de falsificação de IP ([[Cyber_Spoofing|IP Spoofing]]) e não enxerga o payload (carga útil) do pacote.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_Firewall_PacketFilter]] opera como um **Guarda de Trânsito com amnésia anterógrada**. Ele fica na fronteira da [[Rede_LAN|LAN]] e só sabe ler a placa do carro ([[Rede_IP|IP]] de origem), a cidade de destino (IP de destino) e qual faixa da rodovia o carro quer usar (Porta). Ele toma a decisão instantânea de abrir ou fechar a cancela. Porém, ele nunca abre o porta-malas para ver se há contrabando (não lê a [[Rede_Camada_Aplicacao|Camada 7]]) e, 1 segundo depois que o carro passa, ele esquece completamente que aquele carro existe. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
A forma mais clássica de um Packet Filter é a configuração de uma Access Control List (ACL) básica em um roteador da Cisco (IOS) para negar o tráfego de um IP específico:
```text
# Entrar no modo de configuração e criar uma lista de acesso estática
access-list 100 deny ip 192.168.1.50 0.0.0.0 any
access-list 100 permit ip any any

# Aplicar a regra cega na interface de entrada
interface GigabitEthernet0/0
 ip access-group 100 in
````

5. História do Conteúdo

Nascido no final dos anos 1980 na esteira da expansão da ARPANET. Quando os primeiros vermes e acessos não autorizados começaram a trafegar, os engenheiros precisavam de um "tampão" rápido. Eles inseriram essa lógica nos roteadores básicos da época. Era eficiente porque a internet era pequena, confiável e as regras cabiam em poucas linhas de texto. Morreu como linha de frente com o surgimento das conexões dinâmicas complexas (exigindo o [[Cyber_Firewall_Stateful]]), mas ainda vive no núcleo de firewalls modernos ([[Cyber_Firewall_NGFW]]) como a primeira camada de triagem para economizar CPU.