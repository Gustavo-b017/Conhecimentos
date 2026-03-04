---
tags:
- tipo/conceito
- contexto/dev/infra
- afinidade/media
- status/3_incubadora
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

# Rede_ARP

## 1. O Axioma (A Definição Rígida)
> **O que é:** O ARP (Address Resolution Protocol) é a cola fundamental entre a Camada 2 e a Camada 3, responsável por perguntar "Quem tem o IP 192.168.1.1?" e receber a resposta "Eu, o [[Rede_MAC]] AA:BB:CC...".

## 2. A Desconstrução (Mecânica e Pontos de Falha)
* **Como Funciona:** Broadcast. O dispositivo grita para TODOS na rede local. Quem for o dono do IP responde. O resultado fica no Cache ARP.
* **O Problema que Resolve:** O hardware não entende IP, só entende MAC. Sem ARP, o pacote IP não consegue ser encapsulado no quadro Ethernet.
* **Visão Sênior (Vulnerabilidades/Escala):** ARP Spoofing (ou Poisoning). Um atacante responde "Eu sou o Roteador!" antes do roteador verdadeiro. A vítima manda todos os dados para o atacante. É a base de ataques Man-in-the-Middle em LANs.

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
O ARP é um **Grito num Salão de Festas**. Você quer falar com o "Gustavo" (IP), mas não sabe a cara dele (MAC). Você sobe na cadeira e grita "QUEM É O GUSTAVO?". O Gustavo levanta a mão. Se um impostor levantar a mão primeiro, você entrega o segredo para ele.

## 4. Pragmatismo Aplicado (Código e Implementação)
Detectar envenenamento de ARP (dois IPs com o mesmo MAC ou MAC do gateway mudando).
```bash
# Ver tabela ARP atual
arp -a

# Linux: Monitorar mudanças de ARP em tempo real
ip -s neigh
```

5. História do Conteúdo

Publicado no RFC 826 em 1982 por David C. Plummer, o ARP foi forjado durante uma era onde a premissa de redes locais era a "confiança implícita". A comunidade acadêmica acreditava que ninguém na própria LAN seria um agente malicioso. Essa omissão de segurança em favor da baixa latência gerou uma das mais clássicas dores de cabeça corporativas até os dias atuais, onde profissionais precisam implementar controles severos para impedir que estudantes ou funcionários usem pendrives para grampear dados.
## 5. História do Conteúdo
Um protocolo "confiante demais". Criado em 1982, assume que todos na rede são honestos. No [[Rede_IPv6]], o ARP foi substituído pelo NDP (Neighbor Discovery Protocol), que é mais elegante mas sofre de problemas similares.