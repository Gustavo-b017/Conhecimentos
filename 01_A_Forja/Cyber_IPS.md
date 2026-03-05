---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_IPS
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Intrusion Prevention System (IPS) é um mecanismo ativo de contenção instalado diretamente na rota do tráfego (in-line) que analisa profundamente os pacotes e aniquila proativamente conexões maliciosas em tempo real antes que atinjam o destino.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente do [[Cyber_IDS]] que apenas olha uma "cópia" do tráfego, o IPS fica fisicamente no meio do fio (geralmente integrado hoje em um [[Cyber_Firewall_NGFW]]). O pacote é obrigado a passar por dentro dele. Se o IPS detecta um payload malicioso (ex: um *exploit* do protocolo SMB), ele descarta o pacote (Drop) e encerra a sessão [[Rede_TCP|TCP]] com um pacote RST falsificado.
*   **O Problema que Resolve:** Elimina o tempo de latência entre a detecção de um ataque e a intervenção humana. Quando [[Cyber_Malware_Worm|Worms]] de rede começaram a se espalhar em milissegundos, esperar um humano ler um log de IDS e criar uma regra no firewall tornou-se obsoleto. O IPS automatiza a defesa contra ameaças dinâmicas.
*   **Visão Sênior (Vulnerabilidades/Escala):** A força do IPS é sua maior fraqueza arquitetural. Primeiro: ele é um gargalo físico; se o IPS travar, a internet inteira da empresa cai (Ponto Único de Falha), a menos que seja configurado para falhar de forma aberta (*fail-open*), o que destrói a segurança. Segundo: Falsos Positivos aqui são catastróficos. Se o IPS confundir um tráfego vital de banco de dados com um ataque, ele aniquila a operação da empresa, gerando prejuízos imediatos.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se o IDS é o alarme, o [[Cyber_IPS]] é o **Guarda-costas armado com permissão para atirar**. Ele fica fisicamente no único corredor de acesso. Ele não apita; se ele enxergar o padrão catalogado como hostil, ele derruba o invasor na hora. Essa proatividade tem um preço logístico: o guarda-costas precisa revistar todo mundo, o que gera uma fila gigantesca (Latência de Rede). Se houver muito tráfego simultâneo (como num ataque [[Cyber_Ataque_DDoS_SYN_Flood|DDoS]]), o guarda-costas perde a capacidade de processamento e a porta é arrombada por esgotamento de recursos (CPU/RAM).

#### 4. Pragmatismo Aplicado (Código e Implementação)
A sintaxe de prevenção utilizando *Suricata* (o principal concorrente evoluído do Snort) muda a ação principal de `alert` para `drop`. 
```text
# Regra do Suricata em modo in-line (IPS): Derruba o pacote imediatamente se detectar a string maliciosa do malware "Mirai" trafegando.
drop tcp any any -> $HOME_NET 23 (msg:"BLOQUEIO IPS: Malware Mirai IoT Detectado"; content:"mirai"; nocase; sid:2000002; rev:1;)
````

5. História do Conteúdo

A evolução do IDS para o IPS (no final dos anos 1990) foi puramente impulsionada pela velocidade das máquinas. O tráfego de internet aumentou e os vírus evoluíram de arquivos atachados para worms de rede autorreplicáveis. Os processadores de roteadores finalmente ficaram rápidos o suficiente para permitir que a inspeção ocorresse no meio do caminho (in-line) sem que o delay destruísse a experiência do usuário, forçando o mercado a adotar a prevenção ativa.