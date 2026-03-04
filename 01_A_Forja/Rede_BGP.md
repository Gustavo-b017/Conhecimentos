---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/4_evergreen
---

### Rede_BGP
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Border Gateway Protocol (BGP) é o protocolo de roteamento externo absoluto (EGP) que sustenta a internet global, operando através da troca de informações de acessibilidade de rede (rotas) entre diferentes Sistemas Autônomos (ASNs).

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente do [[Rede_OSPF]] (que acha a rota física mais rápida), o BGP é um protocolo de "Vetor de Caminho" (Path-Vector) focado em regras de negócios. Ele toma decisões de roteamento com base em atributos políticos, econômicos e de caminho (como o *AS-PATH*, que conta por quantos provedores o pacote vai passar).
*   **O Problema que Resolve:** A escala global e a diplomacia corporativa. Ele permite que a operadora Claro decida não enviar tráfego pela operadora Vivo por questões contratuais, forçando o tráfego a passar por Miami antes, mesmo que a rota física pela Vivo fosse mais curta.
*   **Visão Sênior (Vulnerabilidades/Escala):** A confiança cega do BGP é o maior risco geopolítico da internet. Ele foi desenhado sem validação criptográfica nativa. O resultado é o *BGP Hijacking*: um provedor de internet menor (ou um governo hostil) pode anunciar acidentalmente ou maliciosamente para o mundo que o "YouTube" agora reside na rede deles. A internet acredita, e todo o tráfego global do YouTube é sugado para um "buraco negro" ou interceptado.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O BGP é o **GPS do Comércio Exterior Internacional**. Se você mandar um contêiner da China para o Brasil via [[Rede_OSPF]], ele traçará uma linha reta pelo mapa, ignorando tudo. Se mandar pelo [[Rede_BGP]], ele olha as regras: "Temos embargo com o país X? O pedágio do país Y é muito caro?". O BGP prefere dar a volta ao mundo de navio a quebrar um contrato comercial entre operadoras (Sistemas Autônomos - ASNs).

#### 4. Pragmatismo Aplicado (Código e Implementação)
Quando você faz um *Traceroute* para um servidor internacional, cada "salto" para uma rede completamente diferente é mediado pelo BGP. Em um roteador Cisco, a declaração de quem são os "vizinhos" comerciais é feita assim:
```bash
router bgp 65000
 # Declara quem é o parceiro de negócios (Outro ASN) para trocar rotas
 neighbor 198.51.100.1 remote-as 64512
 # Manda a internet inteira do meu roteador para ele
 network 10.0.0.0 mask 255.255.0.0
````

5. História do Conteúdo

Criado em 1989 (RFC 1105) num episódio lendário da engenharia. Os pesquisadores Kirk Lougheed (Cisco) e Yakov Rekhter (IBM) perceberam que o antigo protocolo (EGP) estava em colapso devido à expansão descentralizada da rede. Durante uma conferência (IETF), eles desenharam as bases lógicas do BGP inteiro à mão nas costas de um guardanapo manchado de ketchup (conhecido na academia como o "Two-Napkin Protocol"). Essa anotação de bar é o que matematicamente mantém a internet inteira no ar até hoje.