---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_FTP
#### 1. O Axioma (A Definição Rígida)
**O que é:** O *File Transfer Protocol* (FTP) é um protocolo padrão de rede clássico que opera na Camada 7 (Aplicação) do modelo OSI, projetado para a transferência de arquivos entre um cliente e um servidor em uma rede de computadores.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Opera sobre o protocolo TCP na Camada de Transporte, geralmente utilizando as portas 20 e 21.
*   **O Problema que Resolveu:** Padronizou a forma como arquivos massivos eram enviados ou recebidos em servidores remotos antes da existência generalizada da navegação Web amigável.
*   **Visão Sênior (Vulnerabilidades/Escala):** É um protocolo morto para aplicações de segurança por enviar credenciais (usuários e senhas) e os próprios dados em texto claro (não criptografado). Qualquer atacante na rede utilizando um *sniffer* pode interceptar os arquivos lidos. A prática sênior exige sua substituição mandatória por protocolos seguros como SCP (*Secure Copy Protocol*) ou SFTP, que rodam envelopados pelo SSH.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Usar o [[Rede_FTP]] é o mesmo que **enviar malotes de dinheiro por um mensageiro caminhando no meio de uma feira lotada usando uma mochila transparente**. O dinheiro chegará ao destino corretamente, mas qualquer um na multidão que olhar para a mochila saberá exatamente o que você está enviando, e se encostar na mochila, pode subtrair o valor sem esforço.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O comando básico (que hoje deve ser substituído pelo `scp`) costumava ser:
```bash
# Conectando a um servidor inseguro:
ftp servidor.alvo.com
# Após login em texto claro, enviava-se o arquivo
put arquivo.txt
````

5. História do Conteúdo

Criado no alvorecer das redes (1971), anos antes do TCP/IP moderno, foi fundamental para compartilhar códigos e publicações em laboratórios acadêmicos [history]. Como a segurança dependia da limitação física de acesso aos computadores da época, a criptografia não foi incluída em seu design.