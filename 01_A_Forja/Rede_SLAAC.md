---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

# Rede_SLAAC
## 1. O Axioma (A Definição Rígida)
> **O que é:** O SLAAC (Stateless Address Autoconfiguration) é um mecanismo nativo do [[Rede_IPv6]] que permite a um dispositivo hospedeiro (host) gerar autonomamente o seu próprio endereço IP roteável e único, sem a necessidade de solicitar isso a um servidor centralizado como o [[Rede_DHCP]].

## 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O dispositivo escuta mensagens de *Router Advertisement* (RA) enviadas periodicamente pelos roteadores locais via protocolo NDP. O roteador entrega o "Prefixo da Rede" (os primeiros 64 bits). O dispositivo pega esse prefixo e junta com um identificador único gerado a partir do seu próprio [[Rede_MAC]] (processo EUI-64) ou através de uma string randômica (Privacy Extensions), formando um IP de 128 bits completo.
*   **O Problema que Resolve:** No IPv4, a dependência do DHCP cria um Ponto Único de Falha; se o servidor DHCP cai, ninguém pega IP e a rede morre. Como o IPv6 foi projetado para a Internet das Coisas (IoT) com bilhões de dispositivos conectando simultaneamente, o SLAAC descentraliza a distribuição de endereços, tornando a rede infinitamente escalável.
*   **Visão Sênior (Vulnerabilidades/Escala):** O SLAAC puro não entrega configurações cruciais adicionais, como o endereço do servidor [[Rede_DNS]]. Para corrigir isso, a arquitetura moderna utiliza as "Flags" nos pacotes RA (como a *O Flag* - Other Configuration) para dizer ao host: "Crie seu próprio IP, mas vá perguntar ao DHCPv6 apenas onde fica o DNS".

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
O processo do SLAAC é como **se mudar para um novo país e gerar seu próprio número de telefone**. No modelo antigo (DHCP), você entrava no país e ia para uma fila burocrática no governo pedir um número de telefone. No SLAAC, você cruza a fronteira e vê uma placa na estrada dizendo "O código de área deste país é +55" (Prefixo do Roteador). Você pega esse código, anexa ao número de chassi do seu celular (O MAC Address) e começa a fazer ligações imediatamente.

Essa mágica, porém, depende da estrada. Se a [[Rede_Topologias]] for mal projetada (ex: gargalos no Switch central da topologia Estrela), a "placa na estrada" (o pacote RA) nunca chega ao viajante, e a autoconfiguração falha.

## 4. Pragmatismo Aplicado (Código e Implementação)
Quando você inspeciona as interfaces de rede do seu sistema e encontra múltiplos IPs na versão 6 para a mesma placa, você está vendo o SLAAC em ação gerando IPs temporários e privados de forma autônoma para dificultar o rastreamento na web.

```bash
# Linux: Verificar IPs gerados via SLAAC (procure por "scope global dynamic")
ip -6 addr show

# Windows: Listar endereços IPv6
ipconfig /all
```

#### 5. História do Conteúdo
Criado em conjunto com o design do IPv6 no final dos anos 1990 (RFC 4862). Os arquitetos sabiam que a rede do futuro não poderia ser algemada à burocracia de servidores locais. A visão era um ecossistema "Plug and Play" total: você tira uma geladeira inteligente da caixa, liga na tomada, e em milissegundos ela deduz matematicamente seu próprio endereço global e começa a operar.