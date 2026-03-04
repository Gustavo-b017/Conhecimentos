---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/4_evergreen
---

# Rede_BGP

## 1. O Axioma (A Definição Rígida)
> **O que é:** O BGP (Border Gateway Protocol) é o protocolo de roteamento exterior que faz a internet funcionar, conectando diferentes Sistemas Autônomos (AS) como provedores (ISPs), Google e Bancos. É o "Protocolo da Internet".

## 2. A Desconstrução (Mecânica e Pontos de Falha)
* **Como Funciona:** Não busca o caminho mais rápido, mas sim o caminho baseado em **Políticas** (Path Vector). "Eu prefiro enviar dados pela rota mais barata, não pela mais curta".
* **O Problema que Resolve:** Interconexão global descentralizada. Permite que a Vivo fale com a Claro e com a AT&T.
* **Visão Sênior (Vulnerabilidades/Escala):** BGP Hijacking. Como o BGP é baseado em confiança, se um provedor na Indonésia anunciar por engano que "Eu sou o YouTube", o tráfego mundial do YouTube pode ser desviado para lá, derrubando o serviço globalmente.

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
O BGP é a **Diplomacia Internacional**. O Brasil (AS X) concorda em enviar cargas para a China (AS Y) passando pela África, porque o tratado comercial (Peering) é mais barato do que passar pelos EUA, mesmo que o caminho seja mais longo.

## 4. Pragmatismo Aplicado (Código e Implementação)
Verificar a tabela de rotas global (Looking Glass) ou local.
```bash
# Cisco: Ver resumo dos vizinhos BGP
show ip bgp summary
```

5. História do Conteúdo

Criado em 1989 (RFC 1105) num episódio lendário da engenharia. Os pesquisadores Kirk Lougheed (Cisco) e Yakov Rekhter (IBM) perceberam que o antigo protocolo (EGP) estava em colapso devido à expansão descentralizada da rede. Durante uma conferência (IETF), eles desenharam as bases lógicas do BGP inteiro à mão nas costas de um guardanapo manchado de ketchup (conhecido na academia como o "Two-Napkin Protocol"). Essa anotação de bar é o que matematicamente mantém a internet inteira no ar até hoje.
## 5. História do Conteúdo
Dizem que o BGP foi desenhado em dois guardanapos de papel ("Two Napkins Protocol") em 1989. É lento, complexo, mas é a única coisa que segura a internet unida.