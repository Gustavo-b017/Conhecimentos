---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

# Rede_Roteamento
## 1. O Axioma (A Definição Rígida)
> **O que é:** Roteamento é o processo de decisão algorítmica pelo qual roteadores (Camada 3) trocam mapas e calculam ativamente a rota mais rápida e eficiente para entregar pacotes de [[Rede_IP]] de uma rede origem até uma rede destino.

## 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Roteamento Estático:** O administrador digita manualmente a rota. Ex: "Para ir à rede X, jogue o pacote na porta 2". Não consome CPU, mas se o cabo romper, o pacote morre.
*   **Roteamento Dinâmico (IGP):** Roteadores de uma mesma empresa conversam usando protocolos como **[[Rede_OSPF]]** ou **EIGRP**. Eles desenham o mapa inteiro sozinhos e, se um link cair, eles recalculam a rota em milissegundos.
*   **Roteamento Global (EGP - Protocolo BGP):** É o roteamento que sustenta a internet. Em vez de achar o cabo mais rápido, o [[Rede_BGP]] acha o "Provedor" mais eficiente. 
*   **O Problema que Resolve:** Escala e Resiliência. Ninguém no mundo conseguiria atualizar as rotas da internet manualmente quando um cabo submarino rompesse.
*   **Visão Sênior (Vulnerabilidades/Escala):** O **[[Rede_BGP]]** (Border Gateway Protocol) confia cegamente no que os outros roteadores dizem. O maior pesadelo da infraestrutura global é o *BGP Hijacking*. Um provedor menor (ou um atacante) anuncia por engano: "Ei, o Google.com agora mora na minha rede". O resto do mundo acredita e desvia todo o tráfego global para um buraco negro, tirando sites do ar no planeta inteiro.

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se o [[Rede_IP]] é o CEP de destino e a [[Rede_Topologias]] são as ruas físicas, o Roteamento é o algoritmo do **Waze**. Roteamento Estático é você ter o trajeto desenhado num papel no colo: se a ponte cair, você não sabe o que fazer. Roteamento Dinâmico (OSPF) é o Waze detectando trânsito vermelho na avenida principal e dizendo em tempo real: *"Detectamos tráfego lento (Custo Alto), redirecionando pela rota alternativa"*. O protocolo descarta a menor distância física para abraçar a maior largura de banda disponível. O [[Rede_Flex_Algo]] leva isso além, criando fatias lógicas para necessidades específicas.

## 4. Pragmatismo Aplicado (Código e Implementação)
Para você olhar agora o mapa de roteamento (Tabela de Rotas) que a sua máquina usa para saber por onde mandar os pacotes:

**No Windows:**
```powershell
# Mostra todos os caminhos que seu PC conhece
route print
````

**No Linux (Comando moderno):**

```
ip route show
# A linha que diz "default via 192.168.x.x" é a sua rota estática padrão (o roteador que te liga à internet).
```

5. História do Conteúdo

O roteamento dinâmico foi o cerne do projeto militar da ARPANET durante a Guerra Fria. Os militares precisavam de uma rede de comunicações que, no evento de uma cidade inteira (e seus roteadores) ser vaporizada por um ataque nuclear soviético, o restante da rede percebesse o desaparecimento dos nós e recalculasse matematicamente o trajeto dos dados contornando a cratera de forma autônoma. O protocolo que nasceu da paranoia do apocalipse nuclear é o que hoje permite que sua série da Netflix não trave quando o provedor de internet muda de rota.