---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/ataque
---

### Cyber_Ataque_SSRF

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Server-Side Request Forgery (SSRF) é uma vulnerabilidade severa na qual um atacante injeta URLs maliciosas forçando o próprio servidor backend da aplicação a realizar requisições não autorizadas para recursos internos protegidos ou instâncias de metadados em nuvem.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O atacante encontra um campo na aplicação web que aceita uma URL para processar dados (ex: um gerador de PDF, um webhook ou uma requisição de imagem). Ele injeta o endereço interno da nuvem (como `169.254.169.254` na AWS). O servidor, acreditando que a ordem é legítima, faz a chamada HTTP, lê o dado interno e devolve o conteúdo proibido ao invasor.
*   **O Problema que Causa:** O SSRF "assassina" a proteção do [[Rede_Firewall]] perimetral. Como o pedido de dados sai de *dentro* do próprio servidor, as ACLs da rede permitem o tráfego [5]. É o vetor primário para roubo de tokens do Instance Metadata Service (IMDS), levando ao comprometimento total da conta de nuvem (Account Takeover).
*   **Visão Sênior (Vulnerabilidades/Escala):** A versão 1 do IMDS na AWS era letalmente ingênua por permitir requisições GET simples, facilitando a extração via bibliotecas vulneráveis de renderização (como o Pandoc sem a flag de sandbox). A mitigação sênior e absoluta exige a imposição global do **IMDSv2**, que demanda uma sessão iniciada via token PUT com cabeçalhos HTTP estritos, anulando a falsificação simples à distância.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O SSRF é a arte de **fazer a recepcionista do banco roubar o cofre para você**. O assaltante (Atacante) não tem a senha e não consegue passar pelo segurança armado na porta ([[Cyber_Firewall_WAF]]). Ele liga para a recepcionista (A Aplicação Web vulnerável) e diz: "Por favor, vá até a sala do gerente e traga a pasta confidencial". A recepcionista caminha livremente pelo banco, pois ela tem autorização interna (Confiança Lógica), pega a pasta no cofre do gerente (IMDS Metadata) e entrega pela janela para o criminoso.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O *payload* bruto clássico injetado em um parâmetro HTTP de entrada (`?url=`) de uma aplicação web hospedada na AWS, projetado para extrair credenciais de IAM atreladas à máquina vulnerável:
```http
GET /proxy?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/ HTTP/1.1
Host: www.site-vulneravel.com
````

5. História do Conteúdo

Embora o ataque já existisse em redes locais fechadas, sua ascensão à categoria de ameaça crítica global explodiu com a popularização da nuvem pública (AWS, Azure e GCP). O divisor de águas foi o mega vazamento do banco Capital One em 2019, onde a falha grotesca em um WAF de código aberto aliado a um SSRF permitiu que um atacante sugasse os dados de mais de 100 milhões de clientes puxando a chave mestra via IMDS, forçando a AWS a reescrever a arquitetura de segurança dos seus metadados (IMDSv2) para estancar a hemorragia sistêmica