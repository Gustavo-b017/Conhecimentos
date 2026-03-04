---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/4_evergreen
---

### Cyber_Hashing
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Hashing é um algoritmo criptográfico determinístico e irreversível que converte dados de tamanho variável e arbitrário em uma sequência de caracteres (String) de tamanho e formato fixos, servindo como uma prova matemática absoluta de integridade do conteúdo.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Você joga um livro inteiro em PDF de 5GB no algoritmo (ex: SHA-256). Ele cospe uma linha de texto de exatos 64 caracteres. Você joga a palavra "Oi". Ele também cospe 64 caracteres diferentes. Se você alterar uma única vírgula no livro de 5GB, o *Avalanche Effect* do algoritmo altera completamente o código final gerado. É matematicamente impossível pegar o código final e "desfazer" a conversão para ler o livro.
*   **O Problema que Resolve:** Extingue o armazenamento e o roubo de senhas. Nenhuma empresa séria guarda sua senha como "12345" no banco de dados. Eles guardam o Hash da senha. Quando você loga, o site faz o Hash da sua tentativa e compara os dois Hashes. Se o banco de dados da empresa vazar na internet, o hacker só leva linhas ininteligíveis que não podem ser revertidas para texto puro. Também prova se um executável (como um ISO do Linux) foi infectado por um [[Cyber_Malware_Virus]] no trajeto.
*   **Visão Sênior (Vulnerabilidades/Escala):** Hashes burros e sem lentidão (como o arcaico MD5) são quebrados rapidamente através do cruzamento de bancos de dados chamados *Rainbow Tables*. Além disso, hackers forçam "Colisões" (dois arquivos diferentes gerando o mesmo Hash). Para proteger o banco de senhas (usado no [[Cyber_MFA]]), o arquiteto sênior não usa apenas SHA-256, ele utiliza o *Salting* (adição de letras aleatórias antes de gerar o hash) atrelado a funções lentas de derivação por design (Bcrypt ou Argon2), estourando o tempo de processamento necessário para um ataque de força bruta dar certo.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se a Criptografia [[Cyber_AES_256]] (ou [[Cyber_Criptografia_Assimetrica]]) é esconder um livro num cofre trancado com chave, o [[Cyber_Hashing]] é **colocar o livro num moedor de carne industrial e transformá-lo num hambúrguer de formato exato**. Ninguém consegue olhar o hambúrguer e transformá-lo num livro de volta (irreversibilidade). Porém, se amanhã você trouxer um novo livro e passar no mesmo moedor, e a composição química da carne moída não for 100% idêntica à do primeiro, eu saberei na mesma hora que você alterou os ingredientes (Validação de Integridade).

#### 4. Pragmatismo Aplicado (Código e Implementação)
Validar a integridade de um arquivo baixado na internet para provar que ele não foi atacado por um Cavalo de Troia na Cadeia de Suprimentos ([[Cyber_Ataque_Supply_Chain]]) via terminal Linux:
```bash
# Você roda o utilitário na sua máquina para extrair o hash matemático daquele arquivo
sha256sum sistema-bancario-installer.exe

# Output gerado: 
# 4d28e7...a19f  sistema-bancario-installer.exe
# Você cruza esse valor gerado com o que está publicado no site oficial. Se 1 letra for diferente, não execute.
````

5. História do Conteúdo

As funções de Hash ganharam protagonismo mundial não por conta da internet básica, mas por serem o pilar estrutural criptográfico do Blockchain e das Criptomoedas como o Bitcoin (lançado em 2008). O complexo "Proof of Work" (Mineração) é essencialmente milhões de computadores pelo mundo torrando energia elétrica numa roleta colossal para tentar adivinhar a entrada certa que fará a função de Hash de uma transação iniciar com uma quantidade específica de "Zeros" na frente.