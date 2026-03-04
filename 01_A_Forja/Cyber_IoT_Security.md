---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Cyber_IoT_Security

#### 1. O Axioma (A Definição Rígida)
**O que é:** A Segurança IoT (Internet of Things) é o escopo da cibersegurança focado em proteger dispositivos físicos "burros" (câmeras, sensores industriais, geladeiras) que foram integrados às redes TCP/IP modernas para comunicação e automação.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de focar em sistemas operacionais robustos (Windows/Linux), a segurança IoT lida com firmwares limitados embarcados no silício. Envolve proteger a comunicação sem fio, fechar portas de gerenciamento abertas (como [[Rede_Telnet]]) e isolar esses dispositivos em [[Rede_VLAN]]s restritas.
* **O Problema que Causa:** Previne que dispositivos integrados a sistemas críticos sirvam de ponte não monitorada para que atacantes acessem a rede corporativa principal ou transformem esses equipamentos num exército zumbi ([[Cyber_Malware_Trojan|Botnets]]).
*   **Visão Sênior (Vulnerabilidades/Escala):** É o maior pesadelo da infraestrutura atual. O hardware IoT é barato, frágil e possui uma cultura de *Deploy and Forget* (Instale e Esqueça). Os processadores são tão fracos que não suportam o peso matemático de rodar um [[Rede_TLS]] decente. Pior: fabricantes costumam colocar credenciais administrativas *hardcoded* (embutidas direto no código, não alteráveis pelo usuário). Você não pode instalar um antivírus numa lâmpada inteligente.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Ligar a IoT na sua rede corporativa sem isolamento é como **substituir a porta do cofre de um banco por uma porta de papelão porque ela abre sozinha com o vento**. A conveniência de ligar o ar-condicionado da empresa pelo celular é cobrada com a expansão brutal da superfície de ataque. Se o atacante não consegue invadir o [[Rede_Firewall]] milionário do servidor, ele invade o termostato inteligente do aquário do saguão de visitas (que está na mesma rede IP) e usa ele como trampolim.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A primeira regra prática da segurança IoT (mencionada na Aula 5 da FIAP) é o mapeamento ativo. Se você não sabe o que está na rede, você não pode proteger.
Uso do Nmap para encontrar dispositivos IoT clandestinos usando protocolos vulneráveis locais:
```bash
# Varrer a rede interna ignorando Ping (-Pn) para caçar serviços (como telnet ou painéis HTTP) em portas exóticas comuns em IoT usando [[Ferramenta_Nmap|Nmap]]
nmap -p 23,80,8080,554,8000,9000 -sV -Pn 192.168.1.0/24
````

5. História do Conteúdo

A falência da IoT foi exibida ao mundo em Setembro de 2016. Um hacker lançou o malware _Mirai_, que constantemente varria a internet atrás de câmeras IP e roteadores domésticos e testava 61 senhas padrão de fábrica (como "admin/admin"). Ele dominou centenas de milhares de dispositivos silenciosamente e comandou que todos acessassem os servidores da empresa Dyn DNS ao mesmo tempo ([[Cyber_Ataque_DDoS]]), derrubando a internet de metade da costa leste dos Estados Unidos.