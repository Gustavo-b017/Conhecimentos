---
tags:
- tipo/conceito
- contexto/dev/infra
- afinidade/media
- status/3_incubadora
---

### Rede_DNS
#### 1. O Axioma (A Definição Rígida)
**O que é:** O DNS (Domain Name System) é um banco de dados hierárquico e distribuído responsável por traduzir nomes de domínio legíveis por humanos (google.com) em endereços IP roteáveis por máquinas.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ocorre na Camada 7 (Aplicação) primariamente via UDP porta 53 pela velocidade. O processo envolve dois atores principais:
    * **Recursive Resolver:** O "assistente" (geralmente do seu provedor ou 8.8.8.8). Ele busca a resposta para você caçando na hierarquia da internet.
    * **Authoritative Server:** O "dono da verdade". O servidor que guarda o registro oficial daquele domínio.
*   **Registros Atômicos (Records):** A (Mapeia nome p/ IPv4), AAAA (Nome p/ [[Rede_IPv6]]), CNAME (Apelido/Alias para outro nome), MX (Direciona para o servidor de E-mail), TXT (Textos arbitrários, usado para segurança/SPF) .
*   **O Problema que Resolve:** Humanos são péssimos em decorar números abstratos. Sem o DNS, para acessar a Netflix, você precisaria digitar `54.237.226.164`. Ele é a "lista telefônica" da rede.
*   **Visão Sênior (Vulnerabilidades/Escala):** DNS não foi criado com segurança em mente. É vulnerável a *DNS Cache Poisoning* (envenenar o cache do resolver para redirecionar usuários para sites falsos) e *DNS Hijacking*. Hoje, isso é mitigado utilizando DNSSEC (assinatura criptográfica dos registros) e DoH/DoT (DNS sobre HTTPS/TLS) para evitar espionagem.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O DNS é um sistema de delegação cartorial extremamente eficiente. Quando você digita "www.pudim.com.br", o seu computador (Resolver) pergunta ao servidor Raiz (Root) da internet. O Raiz não sabe o IP, mas diz: "Vá falar com o servidor do cartório '.br'". O servidor '.br' diz: "Vá falar com o servidor do dono do 'pudim'". Finalmente, o servidor Autoritativo do Pudim devolve o [[Rede_IP]] exato. É uma estrutura de árvore em que a responsabilidade é sempre empurrada para a ponta. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
Para extrair registros DNS diretamente no terminal, driblando o cache do navegador (fundamental para investigar domínios ou configurações de e-mail):

**No Linux / Mac / WSL:**
```bash
# Busca o IP do servidor web (Record A)
dig +short google.com

# Busca onde os e-mails desse domínio são processados (Record MX)
dig MX pynetlabs.com
````

**No Windows:**

```
nslookup -type=mx pynetlabs.com
```

5. História do Conteúdo

Criado por Paul Mockapetris em 1983. Antes do DNS, a internet era tão pequena que a lista de todos os computadores do mundo (e seus IPs) ficava em um único arquivo de texto chamado `HOSTS.TXT`, mantido pelo Instituto de Pesquisa de Stanford. Os administradores do mundo inteiro tinham que baixar esse arquivo via FTP à noite. Quando a rede passou de centenas para milhares de computadores, o arquivo `HOSTS.TXT` virou um gargalo insustentável. O DNS foi a solução arquitetural que permitiu a internet escalar infinitamente.