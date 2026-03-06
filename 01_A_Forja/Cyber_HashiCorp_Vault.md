---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/devsecops
---

### Cyber_HashiCorp_Vault

#### 1. O Axioma (A Definição Rígida)
**O que é:** O HashiCorp Vault é a infraestrutura de cofre digital padrão ouro do mercado, criada para centralizar, auditar e controlar de forma absoluta o armazenamento e a distribuição de senhas, chaves de API e certificados em ambientes dinâmicos e efêmeros de nuvem.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** As aplicações não guardam mais senhas no banco de dados, nem arquivos de propriedade (`.env`). Quando a aplicação inicializa, ela se autentica no Vault (via [[Cyber_IAM]] ou identidade da máquina), o Vault valida a permissão, abre seu núcleo protegido por criptografia em memória, e devolve a senha em texto claro temporariamente.
*   **O Problema que Resolve:** O espalhamento (Sprawl) de segredos. Antes, trocar a senha do banco de dados exigia reiniciar e reconfigurar 50 microsserviços. Com o Vault, você muda a senha apenas no cofre central, e os microsserviços apenas consultam a nova chave via [[Arquitetura_API_Gateway|API]].
*   **Visão Sênior (Vulnerabilidades/Escala):** Ao centralizar todas as chaves mestre da empresa, o Vault se converte no mais letal [[Infra_SPOF]] e no alvo número 1 dos invasores. Se o Cluster do Vault cai, toda a empresa apaga imediatamente, pois nenhuma aplicação sabe logar no banco. Além disso, quando o servidor do Vault é reiniciado, ele nasce "Selado" (Sealed). Apenas uma cerimônia rigorosa envolvendo múltiplos diretores inserindo fragmentos matemáticos separados (Shamir's Secret Sharing) pode destrancar a memória criptografada para o sistema voltar ao ar.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_HashiCorp_Vault]] atua como o **Tesoureiro Central de um Cassino**. Os crupiês (Microsserviços) não têm os próprios cofres nem guardam dinheiro infinito debaixo da mesa. Quando precisam pagar um jogador, o crupiê vai até o Tesoureiro, apresenta a própria identidade, assina um termo de responsabilidade, e o Tesoureiro entrega exatamente o valor necessário para aquela rodada. Nenhuma ficha dorme fora do cofre principal.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O consumo de uma chave estática dentro do cofre operado no terminal pelo administrador da infraestrutura (ou via API REST pela aplicação):
```bash
# Buscando a senha do banco de dados de produção armazenada no motor KV (Key-Value) do cofre
vault kv get -field=password secret/producao/banco_financeiro
````

5. História do Conteúdo

Criado pela HashiCorp (mesma criadora do Terraform) em 2015. A invenção da [[Cyber_Immutable_Infrastructure]] e dos contêineres Docker criou um caos gerencial. Servidores passaram a ser destruídos e recriados milhares de vezes por dia. Como você injeta uma senha em uma máquina que não existia há 5 minutos e vai sumir em 1 hora? O Vault foi a resposta do mercado para forjar identidades para "máquinas" e não apenas para "humanos".