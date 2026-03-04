---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

### Rede_DNS_Resolvers
#### 1. O Axioma (A Definição Rígida)
**O que é:** A arquitetura do DNS é dividida em duas metades operacionais distintas: o **Servidor Recursivo (Resolver)**, que age como um detetive caçando o IP na internet em nome do usuário, e o **Servidor Autoritativo**, que é o dono absoluto e inquestionável do registro final de um domínio.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Quando você digita um site, seu PC não fala com o dono do site. Ele fala com o *Resolver* (geralmente o 8.8.8.8 do Google ou do seu provedor). O Resolver pergunta à raiz da internet, que o aponta para o servidor `.com`, que o aponta para o *Servidor Autoritativo* da empresa. O Autoritativo devolve a resposta final. O Resolver entrega a você e guarda uma cópia na memória (Cache) baseada no TTL (Time-to-Live).
*   **O Problema que Resolve:** Previne ataques massivos de negação de serviço acidentais à infraestrutura global. Se não houvesse o cache dos servidores recursivos absorvendo 99% das requisições mundiais, os servidores autoritativos de grandes sites derreteriam em segundos.
*   **Visão Sênior (Vulnerabilidades/Escala):** O Servidor Recursivo é inerentemente fofoqueiro e ingênuo. Ele é o alvo clássico do *DNS Cache Poisoning*. Se um atacante forjar a resposta antes do servidor autoritativo e envenenar a memória do Resolver, os próximos 50 mil clientes que pedirem aquele site serão redirecionados silenciosamente para o IP de um servidor de phishing criminoso.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O ecossistema DNS é a interação entre **um Bibliotecário Terceirizado e a Editora do Livro**. O Bibliotecário (Servidor Recursivo) não escreve os livros, ele apenas busca para você. Ele liga para a Editora (Servidor Autoritativo) perguntando onde o livro está. A Editora dá a resposta definitiva. O Bibliotecário te repassa a resposta e anota num post-it (Cache) para que, se o próximo aluno perguntar do mesmo livro na próxima hora, ele não tenha que ligar para a Editora de novo, economizando tempo brutal de latência.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O comando `dig` no Linux é a ferramenta forense para debugar falhas de DNS. Usando o parâmetro `+trace`, você obriga a sua máquina a agir ela mesma como um Servidor Recursivo, ignorando o cache do provedor e perguntando passo a passo até chegar na autoridade:
```bash
dig +trace pudim.com.br
# Ele vai printar a conversa com os Root Servers, depois com o TLD (.br) e finalmente o IP do Autoritativo.
````

5. História do Conteúdo

Essa separação estrita de poderes foi desenhada na década de 1980 por Paul Mockapetris. Na internet militar primitiva, não existia delegação; todo computador possuía uma cópia de toda a rede mundial num arquivo `HOSTS.TXT`. O modelo dividido entre _Resolver_ e _Authoritative_ foi a única arquitetura algorítmica capaz de permitir que a rede crescesse de mil máquinas para bilhões de máquinas sem entrar em colapso termodinâmico de hardware.