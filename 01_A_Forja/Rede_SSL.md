---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Rede_SSL

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Secure Sockets Layer (SSL) é um protocolo criptográfico depreciado, obsoleto e rompido, operante na Camada 6/7, originalmente criado para estabelecer links autênticos e criptografados entre navegadores e servidores web.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Usava certificados de chave pública (X.509) para atestar a identidade do servidor e criptografia simétrica para fechar os dados do usuário.
- **O Problema que Resolveu (No Passado):** Quando a web nasceu, o [[Rede_HTTP]] transitava tudo em texto claro. O SSL resolveu o problema da criação do comércio eletrônico global, impedindo que cartões de crédito fossem lidos por qualquer roteador no meio do caminho.
- **Visão Sênior (Vulnerabilidades/Escala):** O SSL (nas suas versões 1.0, 2.0 e 3.0) está matematicamente **MORTO**. Suas falhas de design permitem a extração das chaves criptográficas através de ataques severos como o POODLE e BEAST. Qualquer servidor corporativo hoje que ainda permita conexão de retorno via SSL 3.0 (Downgrade Attack) reprova instantaneamente em frameworks de segurança e falha nas normas PCI-DSS.

#### 3. As Sinapses (Conexões Livres)
O [[Rede_SSL]] é o **velho cadeado de latão com o miolo enferrujado**. Ele serviu perfeitamente na época em que os ladrões só conheciam pés de cabra. Contudo, as ameaças evoluíram, os hackers trouxeram gazuas matemáticas, e o cadeado de latão agora se abre com um simples grampo de cabelo. Infelizmente, o nome "SSL" ficou cravado na cultura; mesmo usando a tecnologia blindada e moderna do [[Rede_TLS]], as pessoas e empresas ainda chamam de "Certificado SSL".

#### 4. Pragmatismo Aplicado (Código/Implementação)
Comando mandatório para administradores testarem se a falha crítica está ativa, forçando o servidor a tentar conversar usando o protocolo falho SSLv3. Se ele aceitar, o servidor está condenado.
```bash
# Uso do cliente OpenSSL para testar downgrade; o esperado é que a conexão seja rejeitada.
openssl s_client -connect www.banco.com.br:443 -ssl3
````

5. História do Conteúdo

Criado pela empresa Netscape Communications em 1995 de forma proprietária. A versão 1.0 nunca foi a público por ser cheia de furos estruturais. A versão 2.0 e 3.0 construíram o boom da "Ponto Com" nos anos 90, mas como a Netscape queria manter o controle sobre o padrão, a indústria rebelou-se, forçando a depreciação global em prol de um protocolo aberto.