---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/baixa
  - status/3_incubadora
---

### Rede_Gopher
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Gopher é um protocolo de Camada de Aplicação da rede, estritamente baseado em menus de texto, focado na distribuição, busca e recuperação rápida de documentos em formato hierárquico pela internet.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez de usar páginas interligadas de formato rico, o Gopher atuava indexando documentos de forma semelhante à árvore de pastas de um sistema de arquivos do computador, navegados apenas por menus numerados em texto puro.
*   **O Problema que Resolveu:** Antes do protocolo HTTP e do navegador web, achar arquivos na internet exigia que você soubesse exatamente em qual servidor FTP entrar [history]. O Gopher organizou a desordem em uma estrutura de busca unificada e indexada.
*   **Visão Sênior (Vulnerabilidades/Escala):** Arquiteturalmente morto e obsoleto. Foi completamente devorado pelo HTTP por causa da falta de interface gráfica e hipermídia. Além disso, assim como o FTP e o Telnet, é um protocolo engessado sem camadas de criptografia nativas, não sobrevivendo à era moderna da segurança.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O protocolo [[Rede_Gopher]] era a **biblioteca física de arquivos em pastas suspensas** da internet primária. Você entrava, via o índice numérico da gaveta, e puxava o texto exato. Quando o HTTP surgiu, ele substituiu a gaveta de metal por uma galeria de arte com imagens e botões clicáveis, tornando a fria burocracia dos menus de texto instantaneamente indesejável.

#### 4. Pragmatismo Aplicado (Código e Implementação)
*(Como o protocolo é obsoleto e sem uso em auditorias de segurança modernas, ferramentas padrão de SO não trazem mais clientes nativos).*

#### 5. História do Conteúdo
Foi criado em 1991 na Universidade de Minnesota. *Gopher* (Esquilo) era a mascote da universidade e um jogo de palavras, pois a ferramenta "cavava" na rede atrás de informações. Por um curto período nos anos 90, Gopher e a World Wide Web (HTTP) disputaram o controle de como a internet seria acessada pelas pessoas. A universidade tentou cobrar taxas de licenciamento pelo uso comercial do servidor Gopher, o que resultou no êxodo global para a plataforma HTTP, que era gratuita, livre e mais bonita [history].