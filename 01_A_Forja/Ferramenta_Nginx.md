---
tags:
  - tipo/ferramenta
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Ferramenta_Nginx

#### 1. O Axioma (A Definição Rígida)
**O que é:** O NGINX é um software de altíssima performance para infraestrutura web, operando primariamente como servidor HTTP, proxy reverso, balanceador de carga (Load Balancer) e terminador de criptografia SSL/TLS.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Diferente de servidores legados que criavam um processo ou *thread* inteiro de CPU para cada novo usuário que acessava o site, o NGINX trabalha de forma *event-driven* e assíncrona. Ele usa apenas um ou poucos *workers* (processos operários) para gerenciar centenas de milhares de conexões HTTP e HTTPS simultaneamente com uso mínimo de memória RAM.
- **O Problema que Resolve:** Resolve o gargalo de exaustão de memória em infraestruturas submetidas a cargas extremas de tráfego, servindo tanto para entregar páginas estáticas em milissegundos quanto para mascarar e distribuir requisições complexas para bancos de dados ou APIs no back-end.
- **Visão Sênior (Vulnerabilidades/Escala):** A adoção de tecnologias experimentais no núcleo do NGINX gera débito de segurança. A vulnerabilidade catalogada como CVE-2024-31079 expôs uma falha grave de corrupção de memória (*stack-based buffer overflow*) no módulo HTTP/3 QUIC. Ao configurar o servidor para rodar esse protocolo novo (compilado por padrão no NGINX Plus), requisições HTTP/3 clandestinas forjadas para coincidir com o exato momento de drenagem da conexão (*connection draining process*) forçavam a interrupção súbita (*termination*) dos processos *worker* do NGINX, resultando em interrupção direta do servidor.

#### 3. As Sinapses (Conexões Livres)
O NGINX opera como o **Maestro da Orquestra Sinfônica em um teatro hiperlotado**. Quando a porta da frente (a porta 80 ou 443) recebe 100 mil pedidos de clientes ao mesmo tempo, ele não tenta processar todos eles no caixa; ele rapidamente pega os pedidos, impõe políticas de bloqueio, adiciona criptografia e distribui (Balanceamento de Carga) de forma invisível para os servidores menores e escondidos no porão da empresa. 

#### 4. Pragmatismo Aplicado (Código/Implementação)
As implementações cruciais do NGINX giram em torno da imposição de segurança ponta a ponta e bloqueio de protocolos mortos para aprovação em auditorias como o PCI-DSS.
```nginx
# Forçar terminação TLS moderna e rejeição imediata de SSL legados vulneráveis (como bloqueio contra o ataque POODLE):
server {
    listen 443 ssl;
    server_name mestre.com.br;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    
    # Repassar tráfego blindado para a aplicação interna
    location / {
        proxy_pass http://localhost:8080;
    }
}
````

5. História do Conteúdo

Criado por Igor Sysoev em 2004 para resolver o infame "Problema C10k" (o desafio tecnológico de gerenciar dez mil conexões simultâneas num único servidor web sem travar). O software engoliu o mercado e destronou gigantes como o Apache por sua arquitetura leve, sendo a espinha dorsal nativa da entrega de conteúdo moderno de plataformas como a [[Netflix]].