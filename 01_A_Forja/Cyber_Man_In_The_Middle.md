---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Man_In_The_Middle

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Man-in-the-Middle (MiTM) é um ataque hostil de interceptação e manipulação de tráfego, onde o cibercriminoso se posiciona sorrateiramente no meio da comunicação entre dois nós, podendo alterar, roubar e redirecionar dados em tempo real.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O atacante frauda ativamente a rede (geralmente usando o frágil [[Rede_ARP|ARP Spoofing]] ([[Cyber_Spoofing]]) ou injetando-se em sessões de roteamento e serviços desconfigurados). Ele engana a vítima dizendo "Eu sou o servidor", e engana o servidor dizendo "Eu sou a vítima". O tráfego de ambos passa pelo computador do invasor antes de ir para o destino.
- **O Problema que Resolve:** Para o atacante, eleva a escuta clandestina ([[Cyber_Eavesdropping]]) para manipulação destrutiva. Ele pode degradar uma conexão criptografada ([[Cyber_Ataque_POODLE]] ou SSL Stripping), injetar links de [[Cyber_Phishing|Phishing]] em tempo real ou reescrever transações financeiras.
- **Visão Sênior (Vulnerabilidades/Escala):** Protocolos modernos em Nuvem mitigam esse ataque forçando [[Rede_TLS|TLS 1.3]] ponta a ponta e certificados HSTS. Contudo, no ambiente local de uma empresa, se o switch central não possuir inspeções agressivas de portas (DAI), e não existir a cultura do [[Cyber_Zero_Trust]] que obrigue autenticação contínua mesmo dentro da [[Rede_LAN]], o atacante ganha o controle total das sessões.

#### 3. As Sinapses (Conexões Livres)
A mecânica do [[Cyber_Man_In_The_Middle]] é a do **Carteiro Sociopata**. Você escreve uma carta com sua senha para o banco de dados. O carteiro pega a carta, abre, rouba sua senha, copia o texto perfeitamente em um papel novo, altera a conta de destino para a conta dele e envia ao banco. O banco processa e devolve o comprovante. O carteiro intercepta o comprovante, frauda um novo para você e te entrega sorrindo. O sistema operou como esperado por ambas as pontas da vítima, mas a entidade no meio assumiu o controle bi-direcional.

#### 4. Pragmatismo Aplicado (Código/Implementação)
O comando mais temido de execução rápida do ataque usando a ferramenta de linha de comando em redes legadas, focando no gateway da infraestrutura:
```bash
# Forçando a máquina alvo (192.168.1.10) a achar que a minha placa de rede (eth0) é o Gateway (192.168.1.1)
sudo arpspoof -i eth0 -t 192.168.1.10 192.168.1.1
````

5. História do Conteúdo

Este ataque migrou da clássica violação de correspondência de inteligência governamental em períodos de guerra para os protocolos abertos TCP/IP na década de 1990. Redes locais nunca foram forjadas com suspeita interna. O princípio primário do design de redes era "todos os computadores do prédio confiam uns nos outros", premissa que gerou o déficit de segurança multibilionário que sofremos hoje,.