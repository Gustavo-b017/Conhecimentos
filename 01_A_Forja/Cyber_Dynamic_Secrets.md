---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/devsecops
---

### Cyber_Dynamic_Secrets

#### 1. O Axioma (A Definição Rígida)
**O que é:** Os Segredos Dinâmicos são credenciais forjadas sob demanda na exata fração de segundo em que são solicitadas, programadas com um "Tempo de Vida" (TTL) rigoroso para se autodestruírem e revogarem o acesso logo em seguida.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O [[Cyber_HashiCorp_Vault]] conecta-se ao servidor de Banco de Dados. Quando o app de Vendas pede uma senha, o Vault não lê uma senha anotada. Ele roda dinamicamente um comando `CREATE USER` no banco gerando a senha "XyZ123" e entrega ao app. Após 10 minutos (TTL), o Vault entra no banco de dados de novo e roda `DROP USER`, matando a conexão.
*   **O Problema que Resolve:** Assassina o uso de senhas estáticas corporativas e a "Janela de Oportunidade" de invasões. Mata os ataques de vazamento silencioso de longa duração.
*   **Visão Sênior (Vulnerabilidades/Escala):** Se um atacante usar um [[Cyber_Malware_Spyware]] e roubar a credencial em trânsito, ele também tem acesso ao banco, *mas apenas pelos 10 minutos restantes*. A movimentação lateral é castrada temporalmente. A falha técnica reside no atrito de processamento: criar e destruir usuários dinâmicos 10.000 vezes por hora devora a CPU do banco de dados subjacente e fragmenta logs de auditoria, exigindo calibração perfeita de conexão contínua.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O uso tradicional de senhas estáticas é como entregar a **Chave de Metal da sua casa para a Faxineira**. Se ela fizer uma cópia, pode roubar sua casa 5 anos depois. O [[Cyber_Dynamic_Secrets]] é o **Crachá de Visitante com Tinta Evaporativa**. Você emite o crachá para o técnico que entrou na matriz (A Aplicação); a química do crachá é projetada para derreter o código de barras automaticamente em 30 minutos. Ele não precisa devolver o crachá na saída; a chave deixa de existir fisicamente no universo.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Ordem tática de requisição onde o sistema pede uma credencial descartável para o banco PostgreSQL gerida ativamente pelo motor do Vault:
```bash
# Lendo uma credencial que acaba de ser fabricada no banco de dados e que se autodestruirá com base na política atrelada ao papel (role) 'app-vendas'
vault read database/creds/app-vendas
````

_(O output retorna um usuário/senha aleatórios e o tempo exato (TTL) até a bomba-relógio matemática expirar a credencial)._

5. História do Conteúdo

A evolução foi necessária para complementar o Vault. Mesmo escondendo as senhas estáticas, se o código fonte ou a memória da aplicação fosse _dumpada_ via [[Cyber_Process_Hollowing]], o atacante achava a senha em texto claro em uso. A comunidade sênior de infraestrutura percebeu que a única forma de garantir a segurança na nuvem pública era tratar a própria credencial como algo mutável e inerentemente mortal.