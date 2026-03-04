---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/4_evergreen
---

### Rede_HTTP

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Hypertext Transfer Protocol (HTTP) é a linguagem síncrona não criptografada da camada de [[Rede_Camada_Aplicacao]], que opera como o motor fundamental subjacente à World Wide Web para requisitar e entregar documentos hipermídia.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** É inerentemente [[Rede_Stateless]]. O navegador (cliente) manda um verbo em texto claro (GET, POST) para o servidor, pedindo uma página ou imagem. O servidor recebe, processa e joga o arquivo de volta na porta 80 do [[Rede_TCP]]. O servidor esquece o usuário logo em seguida.
- **O Problema que Resolve:** Antes do HTTP, usar a internet significava decorar códigos de terminais FTP, Telnet ou Gopher. O HTTP permitiu que textos tivessem "hiperlinks" que apontassem para outros computadores de forma fluida, popularizando a rede para leigos.
- **Visão Sênior (Vulnerabilidades/Escala):** O HTTP quebra o conceito de Confidencialidade da Segurança. Sendo texto claro, qualquer nó na rede (um roteador, a operadora, ou um atacante no café usando [[Ferramenta_Wireshark]] via [[Cyber_Eavesdropping]]) consegue ler o usuário, senha, cookie ou texto que você enviou. Sistemas críticos rodando sob a Porta 80 hoje são um atestado de falência da infraestrutura.

#### 3. As Sinapses (Conexões Livres)
Mandar dados por [[Rede_HTTP]] é despachar um **Cartão Postal sem envelope por um sistema de correios corrupto**. Você escreve a sua senha atrás do cartão na caneta azul e joga na caixa. O caminhão dos correios (o Roteamento), os separadores de correspondência (os Gateways) e o carteiro que o entrega têm plena capacidade de ler, fotografar e até alterar o texto escrito com corretivo antes da carta chegar ao servidor de destino.

#### 4. Pragmatismo Aplicado (Código/Implementação)
A fragilidade de texto plano da camada de aplicação sendo lida no nível de linha de comando usando telnet ou netcat na porta bruta 80:
```http
# Você digita diretamente no terminal conectado ao servidor:
GET /login.html HTTP/1.1
Host: siteruim.com.br

# O servidor cospe o HTML cru de volta na sua cara na tela
````

5. História do Conteúdo

Criado por Tim Berners-Lee no CERN em 1989 para resolver o caos da documentação acadêmica espalhada em computadores diferentes. O HTTP, aliado à linguagem HTML, pretendia ser apenas um repositório distribuído de textos científicos. Ninguém imaginava que as pessoas usariam essa vitrine acadêmica para colocar números de cartão de crédito.