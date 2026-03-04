---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Infra_Apache_Tomcat

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Apache Tomcat é um *Servlet Container* open-source que provê o ambiente de execução físico e as pontes de rede HTTP nativas necessárias para hospedar e rodar aplicações corporativas baseadas em Java.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Ele atua na fronteira da Camada 7. Ele escuta as portas de rede (ex: 8080 TCP), intercepta a requisição [[Ferramenta_Nginx|HTTP]] bruta em formato de texto, empacota isso em objetos nativos (`HttpServletRequest`) e entrega para o código Java rodar a regra de negócio.
- **O Problema que Resolve:** Abstrai a engenharia de baixo nível do Sistema Operacional. Sem um contêiner, o programador Java teria que escrever código do zero para abrir *Sockets* na placa de rede, ler *headers* HTTP byte a byte e gerenciar o pool de *threads* na unha.
- **Visão Sênior (Vulnerabilidades/Escala):** O modelo clássico do Tomcat aloca pesadamente uma Thread de RAM do Sistema Operacional para cada requisição simultânea. Sob ataques de [[Cyber_Ataque_DDoS_SYN_Flood]] ou em picos de Black Friday, as threads esgotam rapidamente, causando *Crash*. Hoje, arquiteturas sêniores usam o Tomcat *Embarcado* direto na aplicação ([[Java_Rest_Controller|Spring Boot]]) e rodam múltiplas réplicas orquestradas em Kubernetes, não dependendo de um [[Infra_SPOF|servidor físico único]].

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O Tomcat é o **Garçom e a Bandeja** em um restaurante onde o seu código Java (O Spring) é o Chef de Cozinha. O cliente da rua (o Navegador) não pode entrar na cozinha gritando ordens cruas. O garçom (Tomcat) anota o pedido no formato correto, entrega o papel limpo ao Chef, espera o prato ficar pronto, coloca na bandeja e o devolve de forma elegante à mesa do usuário final através da porta da frente.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O poder do ecossistema moderno de infraestrutura abstraída. Hoje, você não instala o Tomcat no Linux. O [[Java_SpringBoot]] carrega o servidor dentro de si via dependência Maven, levantando a infraestrutura dinamicamente:
```xml
<!-- Apenas adicionar isso faz a infraestrutura do Tomcat subir na porta 8080 -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
````

5. História do Conteúdo

Criado por James Duncan Davidson na Sun Microsystems em 1999 e rapidamente doado à Apache Software Foundation. O nome "Tomcat" (Gato) foi escolhido porque James queria um animal independente que representasse algo que "pudesse se virar sozinho". Ele se tornou a espinha dorsal de 90% das integrações Java globais nas últimas duas décadas.