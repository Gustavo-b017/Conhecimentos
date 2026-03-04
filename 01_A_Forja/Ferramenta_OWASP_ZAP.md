---
tags:
  - tipo/ferramenta
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Ferramenta_OWASP_ZAP

#### 1. O Axioma (A Definição Rígida)
**O que é:** O OWASP Zed Attack Proxy (ZAP) é um scanner de vulnerabilidades integrado e um proxy de interceptação passiva/ativa focado na realização de [[Cyber_Pentest]] em aplicações web para encontrar falhas de segurança durante o desenvolvimento e execução.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente do [[Ferramenta_Wireshark]] que lê cabos e portas de rede frias, o ZAP atua explicitamente como um homem-no-meio (Man-in-the-Middle) na camada de aplicação HTTP/HTTPS. Você configura seu navegador para passar por ele. O ZAP segura a requisição antes de enviá-la para o site, permitindo que você reescreva os campos para testar uma Injeção de SQL ou adulterar o seu cookie de administrador.
*   **O Problema que Resolve:** Para os analistas, a ferramenta varre as aplicações web ("Spidering") e descobre as rotas e falhas sozinhas através de scanners ativos que metralham o site com as 10 ameaças principais de segurança web (OWASP Top 10).
*   **Visão Sênior (Vulnerabilidades/Escala):** Scanners web automatizados são barulhentos, "burros" e causam caos em ambientes de produção. O ZAP não sabe a diferença entre um botão "Pesquisar" e um botão "Deletar Banco de Dados". Se você rodar o scanner ativo (Active Scan) num site de produção, a ferramenta clicará no botão "Excluir Conta" 5.000 vezes testando vulnerabilidades, destruindo a base de dados em minutos. Sempre se utiliza em instâncias cegas de homologação.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se o firewall é a muralha, usar o ZAP é **colocar um Raio-X com um braço mecânico na porta dos Correios**. Você pega uma carta fechada (Requisição HTTP), joga na máquina e aperta o botão "Pausar". O braço mecânico abre a carta, lê que o valor da transferência bancária é R$ 100, rasura o valor para R$ 1.000.000 e então manda a carta seguir viagem até o servidor do banco para ver como o código fonte do banco reage a essa mentira de entrada. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
Em arquiteturas de *Desenvolvimento Seguro* modernas (SecDevOps), o ZAP não é usado apenas com cliques na interface gráfica. Ele é invocado dentro do pipeline de automação (CI/CD) via linha de comando ou Docker para barrar o código mal feito (evitando acesso indevido e vazamento) de subir pro servidor:
```bash
# Exemplo de comando automatizado executando o ZAP via container Docker contra uma aplicação de homologação local para procurar falhas antes do lançamento:
docker run -t owasp/zap2docker-stable zap-baseline.py -t https://www.aplicacao-teste.com.br
````

5. História do Conteúdo

Mantido pela Open Worldwide Application Security Project (OWASP) e inicialmente criado por Simon Bennetts em 2010. Foi criado para ser uma alternativa de código aberto gratuita à gigante e caríssima ferramenta comercial _Burp Suite_ (da PortSwigger). O ZAP popularizou a capacidade de qualquer desenvolvedor ou pequeno laboratório rodar auditorias web letais sem precisar pagar milhares de dólares em licenças.