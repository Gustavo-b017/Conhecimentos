---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_IAM

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Identity and Access Management (IAM) é o framework de segurança e a disciplina de negócios que garante que as entidades corretas (pessoas ou máquinas) tenham o acesso adequado aos recursos tecnológicos corretos, no momento exato e pelos motivos certos.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** É a separação técnica entre **Autenticação** (provar quem você é, via senhas ou [[Cyber_MFA]]) e **Autorização** (o que você tem permissão para fazer, via controle de acesso baseado em função - RBAC). Ele centraliza a governança: se um funcionário é demitido, o IAM revoga o acesso dele ao e-mail, à VPN e ao banco de dados em um único clique.
*   **O Problema que Resolve:** Elimina o pesadelo logístico e a vulnerabilidade das "Senhas Descentralizadas". Sem IAM, um usuário cria 10 senhas diferentes para 10 sistemas da empresa, esquece metade, anota num post-it e cria um risco colossal.
*   **Visão Sênior (Vulnerabilidades/Escala):** O provedor de IAM (como o Microsoft Entra ID ou Okta) torna-se o calcanhar de Aquiles da corporação. Como ele fornece as chaves para todos os reinos (o conceito de *Single Sign-On* - SSO), se o servidor do IAM for comprometido, o atacante ganha o controle absoluto da infraestrutura inteira instantaneamente, tornando o "[[Infra_SPOF|Ponto Único de Falha]]" o alvo principal de ameaças avançadas.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_IAM]] é o **Segurança com a Prancheta VIP na porta da boate**. Ele não apenas olha a sua identidade para ver se a foto bate com o seu rosto (Autenticação), ele checa o seu nome na lista para ver se você comprou o ingresso da pista ou do camarote aberto (Autorização). Se você for da pista e tentar subir as escadas, o segurança interno te barra, porque a sua identidade é válida, mas o seu nível de acesso não permite aquela ação.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação do IAM na nuvem não é feita com cliques, mas com código declarativo rigoroso. Exemplo de uma política em JSON na AWS (AWS IAM Policy) aplicando o princípio do "Menor Privilégio", permitindo que um usuário apenas leia arquivos de um único servidor (S3), sendo estritamente proibido de deletar algo:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::meu-banco-de-dados-seguro",
        "arn:aws:s3:::meu-banco-de-dados-seguro/*"
      ]
    }
  ]
}
````

5. História do Conteúdo

A Gestão de Identidades começou nos anos 90 puramente para conectar computadores em um escritório fechado, consolidada pelo lançamento do _Active Directory_ (AD) da Microsoft no Windows 2000. No entanto, com a explosão da adoção da computação em nuvem nos anos 2010, o antigo AD (hoje evoluído para ferramentas como o [[Ferramenta_Microsoft_Intune]]) não conseguia controlar logins de funcionários usando celulares pessoais para acessar o Google Workspace na rua, forçando o nascimento da geração de Identidade como Serviço (IDaaS).