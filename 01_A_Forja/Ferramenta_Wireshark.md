---
tags:
  - tipo/ferramenta
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Ferramenta_Wireshark
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Wireshark é o mais avançado analisador e farejador de protocolos do mundo, utilizado para interceptar, registrar e dissecar minuciosamente o tráfego de rede em pacotes individuais de forma visual.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Coloca a placa de rede em modo promíscuo, capturando os pulsos elétricos ou de rádio no nível mais baixo (Ethernet/Wi-Fi). Em seguida, aplica módulos de dissecação para classificar os bits em informações legíveis organizadas por camadas. O analista pode filtrar o tráfego para inspecionar gráficos de fluxo (Flow), estatísticas de Endpoints (quem mais envia/recebe) e categorização por tamanho de pacotes (Packet Lengths).
* **O Problema que Causa:** Destrói a adivinhação. Quando ocorre um incidente de rede ou ataque, o log do servidor muitas vezes é insuficiente. O Wireshark fornece o "cadáver" real da conexão. Permite extrair hierarquia de protocolos, provando matematicamente o momento em que uma falha ou envio anômalo começou [3].
*   **Visão Sênior (Vulnerabilidades/Escala):** A captura cega de dados é suicídio operacional. Farejar o tráfego de um [[Rede_Gateway]] corporativo de 10Gbps sem aplicar "Capture Filters" encherá o disco e a RAM do computador do analista em menos de 1 minuto, travando a máquina da perícia. Além disso, se o tráfego usar TLS 1.3, o Payload do pacote será ilegível sem a injeção prévia das chaves de descriptografia no próprio Wireshark.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O uso do [[Ferramenta_Wireshark]] equivale à **Cena de Crime Isolada para Perícia Criminal**. Sem ele, a TI apenas ouve testemunhas dizendo "A rede caiu". Com ele, a placa de rede varre o chão atrás de sangue. A aba de *Protocol Hierarchy* te diz qual tipo de arma foi usada. A aba de *Endpoints* mostra as pegadas dos criminosos e das vítimas na sala. A aba *Packet Lengths* mostra o calibre da munição, enquanto o *Flow Graph* reconstrói a trajetória da bala frame a frame, ilustrando perfeitamente se um [[Cyber_Ataque_DDoS_SYN_Flood]] parou ou continuou de forma anômala.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Se um [[Cyber_Ataque_DDoS_SYN_Flood]] for realizado, a interface do Wireshark será imediatamente inundada por requisições e respostas não concluídas. O poder real do analista está em usar a sintaxe de Filtro de Exibição (Display Filters) na barra de pesquisa:
```wireshark
# Filtro implacável para localizar os sintomas matemáticos de um SYN Flood:
# Mostrar apenas pacotes de tentativa de início (SYN) sem confirmação (ACK)
tcp.flags.syn == 1 and tcp.flags.ack == 0
````

5. História do Conteúdo

Originalmente lançado em 1998 por Gerald Combs sob o nome de "Ethereal". Naquela época, analisadores de hardware comerciais custavam milhares de dólares, restringindo a auditoria a orçamentos milionários. O projeto open-source quebrou esse monopólio permitindo que qualquer pessoa com um PC dissecasse o [[Rede_Modelo_OSI]]. Em 2006, problemas comerciais com o uso da marca registrada forçaram Combs a renomear o projeto para Wireshark, que se tornou a fundação de estudo padrão global para exames da Cisco e testes de cibersegurança.