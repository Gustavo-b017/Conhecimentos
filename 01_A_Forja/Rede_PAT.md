---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/4_evergreen
---

### Rede_PAT
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Port Address Translation (PAT), também conhecido como *NAT Overload* ou *NAPT*, é a variação agressiva do [[Rede_NAT]] que mapeia múltiplos endereços IP privados internos para um **único** endereço IP público, utilizando a diferenciação através de portas lógicas (Camada 4).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Quando o PC 1 (192.168.1.10) e o PC 2 (192.168.1.11) tentam acessar a internet, o roteador substitui os dois IPs de origem pelo seu único IP público (ex: 200.1.1.1). Para saber a quem devolver a resposta depois, o roteador altera dinamicamente a porta de origem do pacote. (Ex: PC 1 sai pela porta 50001; PC 2 sai pela porta 50002). O roteador anota essa tradução em sua RAM.
*   **O Problema que Resolve:** O NAT Estático exigia que você comprasse 1 IP Público para cada máquina da empresa (1 para 1). O PAT permite o milagre financeiro e logístico de colocar 65.000 dispositivos de uma rede corporativa ou doméstica inteira navegando simultaneamente usando apenar 1 IP Público alugado da operadora.
*   **Visão Sênior (Vulnerabilidades/Escala):** O limite matemático do PAT é a *Port Exhaustion* (Esgotamento de Portas). Como o protocolo TCP só possui cerca de 65.535 portas efêmeras por IP, se uma empresa possui 2.000 funcionários e cada um abre 30 abas no navegador ao mesmo tempo, a tabela de traduções do roteador lota. Novas conexões começam a falhar misteriosamente e a internet da empresa "cai", mesmo o link estando perfeito.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Rede_PAT]] é a **Recepcionista de um Prédio de 500 andares com um único número de telefone**. Quando o João liga para a pizzaria, no bina da pizzaria aparece o telefone geral do prédio. Quando a pizzaria liga de volta para avisar que a pizza chegou, a recepcionista consulta o caderninho dela (A Tabela NAT), onde ela anotou: "A ligação feita às 20h para a pizzaria foi o João do Ramal 45 (A Porta)". Ela transfere a ligação internamente. O mundo externo nunca precisa saber da existência do João ou do seu ramal; eles só conversam com a Recepcionista.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O engenheiro de redes identifica que uma empresa está usando PAT auditando a tabela de translações do roteador. No Cisco IOS, o comando abaixo prova que vários IPs internos estão se disfarçando atrás de apenas um IP externo (Inside Global):
```bash
show ip nat translations
# Pro tcp 200.1.1.1:51234  192.168.1.10:80
# Pro tcp 200.1.1.1:51235  192.168.1.11:80
````

5. História do Conteúdo

O conceito de tradução atrelada a portas surgiu no final dos anos 1990. Foi a gambiarra mais bem sucedida e permanente da história da tecnologia. O espaço do IPv4 estava colapsando matematicamente. O PAT não foi criado para ser um sistema de segurança, foi criado para dar tempo para os engenheiros finalizarem o IPv6. Ironicamente, o mercado gostou tanto de "esconder" os computadores internos atrás do PAT que a tecnologia se recusou a morrer, atrasando a adoção do IPv6 em 20 anos.