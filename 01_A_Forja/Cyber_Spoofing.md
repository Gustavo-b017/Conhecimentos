---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Spoofing

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Spoofing é a falsificação deliberada de uma identidade técnica, mascarando a origem de uma comunicação de rede para se passar por um sistema, dispositivo ou usuário legítimo e confiável.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O atacante adultera cabeçalhos não autenticados na base do protocolo. Ele pode forjar endereços IP (IP Spoofing), MAC addresses na rede local, ou registros de nomes (DNS Spoofing) para enganar os roteadores e vítimas.
- **O Problema que Resolve:** Para o atacante, resolve o bloqueio imposto por listas de controle de acesso (ACLs) do [[Rede_Firewall]] e facilita o redirecionamento de tráfego sem disparar alarmes primários.
- **Visão Sênior (Vulnerabilidades/Escala):** A culpa do Spoofing é do design estúpido dos protocolos dos anos 1970, que baseavam tudo em "confiança mútua". A única mitigação real para ataques de falsificação de IP e ARP são controles passivos rígidos na infraestrutura (como Ingress Filtering - BCP38) ou criptografia ponta a ponta para inutilizar o dado roubado.

#### 3. As Sinapses (Conexões Livres)
O [[Cyber_Spoofing]] é o crime de **Falsidade Ideológica** aplicado à matemática. Um golpista veste o uniforme da companhia de luz e entra na sua casa sem arrombar a porta. Na rede, quando o atacante usa o [[Cyber_Man_In_The_Middle]] via envenenamento de tabela ARP, ele literalmente coloca o crachá do seu roteador. A rede, sendo burra e não exigindo biometria criptográfica daquele pacote, entrega todos os seus dados nas mãos do falsário de forma submissa.

#### 4. Pragmatismo Aplicado (Código/Implementação)
Exemplo sênior para prevenir o IP Spoofing bloqueando pacotes que afirmam vir da sua própria rede interna, mas que estão entrando pela porta externa (Internet):
```bash
# Iptables: Descarta pacotes na interface externa (eth0) que forjam IP de origem da rede interna (192.168.1.0/24)
sudo iptables -A INPUT -i eth0 -s 192.168.1.0/24 -j DROP
````

5. História do Conteúdo

Historicamente, o termo surgiu nas fraudes de telecomunicações analógicas (Phreaking) nas décadas de 70 e 80, onde invasores usavam apitos para simular as frequências de moedas nos telefones públicos. Com o nascimento da internet, o termo foi herdado para descrever a adulteração cega de pacotes.