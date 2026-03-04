---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Rede_5G_SBA

#### 1. O Axioma (A Definição Rígida)
**O que é:** A Service-Based Architecture (SBA) é o framework fundamental do Core 5G (5GC) que abandona a dependência de roteadores monolíticos legados baseados em caixas físicas, substituindo-os por Funções de Rede (NFs) virtualizadas, conteinerizadas e modulares que interagem nativamente via APIs RESTful sobre HTTP/2.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O plano de controle inteiro do celular é decomposto em microsserviços distintos (AMF para gerenciar registro, SMF para gerenciar sessões IP, UDM como banco de dados de chips). Assim como em arquiteturas modernas da web, todas as funções se auto-registram em um diretório central, o NRF (Network Repository Function), onde descobrem e autenticam a comunicação com os serviços pare.
*   **O Problema que Resolve:** Elimina o engessamento de hardware de telecomunicações. Permite CI/CD de redes, fazendo o 5GC escalar em clusters Kubernetes elásticos. Se houver pico de usuários na rede, basta "subir mais instâncias" apenas do serviço impactado (ex: AMF) na nuvem pública ou privada, sem mexer no resto da rede.
*   **Visão Sênior (Vulnerabilidades/Escala):** A SBA mata o protocolo legadíssimo Diameter e traz a stack de TI da internet (HTTP/2, JSON) para o coração do core móvel. Isso cobra um preço perigoso de Segurança Cibernética: abre a rede celular a ataques da web, como Injeção de API, DoS e comprometimento de criptografia, forçando a implementação rígida de novos proxies como o SCP e de firewalls SFW para proteger a borda nativa em nuvem (SEPP).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A transição para o SBA transformou a operadora numa AWS global. O hardware celular clássico (EPC do 4G) era como um gigantesco **Motor a Combustão Selado** (um chassi onde as engrenagens são indivisíveis; se estraga um bloco, desmonta-se tudo). O SBA converteu a rede de telecom numa **Banda de Jazz Dinâmica** (cada microsserviço é um instrumento autônomo que pode ser adicionado, trocado ou removido no palco durante o próprio show sem interromper a música principal), orquestrada pelas requisições ágeis da internet.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Sendo o 5GC uma arquitetura baseada em APIs, a gerência migra do protocolo CLI legado para requisições da web. A descoberta de quem controla as sessões ativas de um core usa o mesmo protocolo das aplicações que você desenvolve, atacando a base de dados do NRF:

```bash
# Descoberta de serviços (SMF) registrados no NRF do Core 5G usando simples requisição HTTP
curl -X GET "https://nrf.5gc.local/nnrf-disc/v1/nf-instances?nf-type=SMF" \
     -H "Accept: application/json"
````

5. História do Conteúdo

Em 2018 (Release 15 do 3GPP), a indústria mundial entrou em consenso: as caixas-pretas de nós monolíticos do 4G baseadas em SCTP/Diameter jamais teriam a flexibilidade ou o tempo de resposta necessários para suportar os casos de uso ágeis da Internet das Coisas (IoT). A solução da academia e corporações foi importar as práticas do Vale do Silício para dentro do rígido fórum de Telecomunicações, consolidando a "nuvem" como ambiente nativo de roteamento global.