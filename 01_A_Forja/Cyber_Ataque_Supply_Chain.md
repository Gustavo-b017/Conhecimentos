---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/media
  - status/3_incubadora
---

### Cyber_Ataque_Supply_Chain

#### 1. O Axioma (A Definição Rígida)
**O que é:** Ataques à cadeia de suprimentos de software ocorrem quando agentes maliciosos exploram vulnerabilidades em componentes indiretos, softwares de terceiros ou bibliotecas de código open-source usados no desenvolvimento ou na distribuição de uma aplicação final.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O atacante não invade o banco alvo diretamente, pois o banco tem um [[Rede_Firewall]] perfeito. Em vez disso, o atacante invade a empresa menor que cria o software de folha de pagamento que o banco usa. O atacante injeta código malicioso na atualização oficial do software. Quando o banco baixar a atualização aprovada, o malware entrará pela porta da frente, assinada digitalmente.
*   **O Problema que Causa:** Contorna completamente as fortificações milionárias do perímetro. Ele destrói o conceito de confiança em atualizações de software legítimo, disseminando um único payload malicioso para milhares de clientes corporativos simultaneamente através de um único fornecedor comprometido.
*   **Visão Sênior (Vulnerabilidades/Escala):** É hoje uma das maiores dores de cabeça do Desenvolvimento Seguro (SecDevOps). Projetos modernos de programação (Node.js, Python) baixam milhares de pacotes da internet (`npm`, `pip`) automaticamente. Se um invasor comprometer uma única biblioteca matemática obscura mantida por um voluntário na internet e adicionar uma linha de [[Cyber_Malware_Backdoor|backdoor]], todas as empresas da Fortune 500 que utilizarem essa biblioteca estarão comprometidas no próximo *build*. A defesa exige auditoria de SBOM (Software Bill of Materials).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_Ataque_Supply_Chain]] é o equivalente a **envenenar a farinha no moinho em vez de atacar o castelo do rei**. O castelo é inexpugnável pelas muralhas. Contudo, o rei compra pão da vila vizinha. O assassino envenena a farinha que vai para o padeiro; o padeiro asse o pão legítimo e as carroças reais entregam o pão venenoso diretamente na mesa do rei sem levantar suspeitas.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A mitigação no ciclo de desenvolvimento não se faz impedindo o código de rodar, mas varrendo e analisando a composição das bibliotecas de terceiros importadas no projeto usando ferramentas de SCA (Software Composition Analysis).
```bash
# Exemplo de comando do utilitário 'npm audit' para checar vulnerabilidades na cadeia de suprimentos JavaScript em um projeto
npm audit --audit-level=critical

# Se houver um pacote envenenado reportado na árvore de dependências, o desenvolvedor é avisado antes de compilar o código.
````

5. História do Conteúdo

Tornou-se o ataque preferido de nações-estado (APT) na década atual. O caso mais aterrorizante da história foi a infecção do sistema _SolarWinds Orion_ em 2020 (atribuído a hackers russos). Os invasores invadiram a SolarWinds, enxertaram um [[Cyber_Malware_Trojan|cavalo de troia]] sutil no software de monitoramento de redes da empresa, e a própria SolarWinds distribuiu essa versão maliciosa "oficialmente" para agências do governo americano (incluindo o Tesouro e a Energia) e gigantes de tecnologia, comprometendo a espinha dorsal dos EUA.