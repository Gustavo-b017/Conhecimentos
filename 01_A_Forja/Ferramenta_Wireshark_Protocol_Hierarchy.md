---
tags:
  - tipo/ferramenta
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Ferramenta_Wireshark_Protocol_Hierarchy

#### 1. O Axioma (A Definição Rígida)
**O que é:** A Hierarquia de Protocolos (Protocol Hierarchy) é o módulo estatístico macroscópico do Wireshark que exibe a distribuição percentual de todos os protocolos identificados em uma captura de rede, organizados em uma árvore lógica.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de listar os pacotes na ordem em que chegaram, o Wireshark compila os dados e os agrupa por encapsulamento (ex: `Ethernet -> IPv4 -> TCP -> HTTP`). Ele mostra quantos pacotes (Packets) e qual o volume de banda (Bytes) cada protocolo consumiu.
*   **O Problema que Resolve:** Resolve a "cegueira do volume". Analisar manualmente 1 milhão de pacotes para descobrir o que está acontecendo na rede é humanamente impossível. Esta ferramenta permite atestar em 2 segundos se a rede está sofrendo um pico anômalo de tráfego DNS ou de vídeo.
*   **Visão Sênior (Vulnerabilidades/Escala):** Se um atacante estiver extraindo dados do banco de dados disfarçando o tráfego dentro de requisições DNS (DNS Tunneling), a aba de hierarquia vai dedurar que a proporção de tráfego DNS da rede subiu de 1% para 40% do volume total. A falha é que a ferramenta confia cegamente nos cabeçalhos; se o tráfego estiver duplamente criptografado e rodando em portas não padrão, ele cairá no genérico "Data".

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A Hierarquia de Protocolo é o **Balanço Contábil (DRE) da sua empresa**. O log pacote a pacote é o livro-caixa diário onde você anota cada café pago. A Hierarquia agrupa tudo e te diz: "No final do mês, 80% do dinheiro foi para Fornecedores (TCP), 15% para Impostos (UDP) e 5% para Manutenção (ICMP)". É a visão do CEO para tomada de decisão rápida.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Acesso através da interface gráfica do analista para isolar imediatamente uma anomalia protocolar e aplicar um filtro com o clique direito:
```text
# Menu Path:
Statistics -> Protocol Hierarchy
# Ao clicar com o botão direito na árvore do protocolo suspeito:
Apply as Filter -> Selected
````

5. História do Conteúdo

Adicionada nos primórdios do projeto Ethereal (antigo nome do Wireshark), a ferramenta estatística foi a resposta direta à inviabilidade da análise de redes de grandes corporações. À medida que as conexões Gigabit se tornaram padrão, o cérebro humano não conseguia mais acompanhar o _scroll_ de dados flutuando na tela, forçando a criação de mapas hierárquicos instantâneos.