---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/ataque
---

### Cyber_Ataque_XXE

#### 1. O Axioma (A Definição Rígida)
**O que é:** O XML External Entity (XXE) é um vetor de ataque no qual a aplicação parseia entradas XML contendo entidades externas forjadas, resultando na extração de arquivos confidenciais do disco local do servidor ou na viabilização de negações de serviço e chamadas SSRF subjacentes.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** A linguagem [[DB_XML]] possui um recurso legítimo chamado DTD (Document Type Definition), que permite declarar "Entidades" (uma espécie de variável dinâmica). O invasor forja uma entidade para apontar diretamente para caminhos do sistema operacional do servidor (como `file:///etc/passwd`). Quando o parser XML da aplicação processa o documento, ele substitui a variável pelo conteúdo do arquivo e o retorna.
*   **O Problema que Causa:** O XXE destrói a Confidencialidade e a Disponibilidade. Permite o *Local File Inclusion* (LFI), escanear portas internas, e executar o apocalíptico ataque *Billion Laughs*, onde uma entidade XML se chama recursivamente de forma exponencial, estourando a memória RAM (DoS).
*   **Visão Sênior (Vulnerabilidades/Escala):** A culpa quase nunca é do desenvolvedor que escreveu o código de negócios, mas sim da configuração omissa (default) da biblioteca de processamento XML da linguagem (ex: no Java ou C#). XXEs modernos estão escondidos nos recônditos de APIs legadas ([[Arquitetura_SOAP]]) ou injetados furtivamente em fluxos de autenticação [[Cyber_IAM]] baseados em SAML. A mitigação impiedosa consiste em desabilitar completamente a resolução de DTDs externas no compilador XML.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O ataque XXE atua exatamente como a **Boneca Russa Matrioska Explosiva**. O sistema (o servidor) pede que você envie uma caixa padronizada (o XML). Você manda a caixa, mas escreve na tampa uma instrução: "Antes de me abrir, vá até o arquivo confidencial do RH, tire uma cópia e coloque dentro de mim". O carteiro burro (o parser XML mal configurado) obedece à instrução da etiqueta rigorosamente, insere os dados do RH na caixa e, quando a devolve, o segredo vaza. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
A injeção anatômica bruta. O invasor define a entidade externa `&xxe;` na DTD e a evoca na tag `<user>`, forçando a leitura de um arquivo vital do kernel do Linux:
```xml
<!-- Payload interceptado na requisição HTTP POST -->
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<userData>
    <user>&xxe;</user>
</userData>
````

5. História do Conteúdo

Foi extremamente comum e devastador durante os anos 2000, época em que integrações entre sistemas Enterprise eram fundamentadas puramente em contratos e envelopes [[Arquitetura_SOAP]] em XML. Com a migração brutal da web para o padrão [[Front_JSON]], o XXE caiu drasticamente na prevalência. Contudo, ele sobrevive hoje como uma ameaça furtiva disfarçada em funcionalidades modernas de uploads de arquivos, pois documentos .docx (Microsoft Word) e .xlsx (Excel) nada mais são do que arquivos XML compactados e zippados.