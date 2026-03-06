---
tags:
  - afinidade/media
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/devsecops
---

### DevSecOps_DAST

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Dynamic Application Security Testing (DAST) é o teste de "caixa-preta" automatizado que simula o comportamento de um hacker externo metralhando a superfície exposta de uma aplicação em execução com payloads maliciosos para verificar como ela responde ao estresse real.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente do SAST, o DAST não olha o código-fonte (ele nem tem acesso a ele). Ele envia requisições forjadas via [[Rede_HTTP]] para as rotas da [[Arquitetura_REST|API]] e analisa a resposta. Ele tenta quebrar logins, testa falhas de autenticação e caça erros de configuração de servidores.
*   **O Problema que Resolve:** Descobre o que a análise de código morto não vê. Um arquivo configurado perfeitamente no SAST pode ser colocado no ar usando um contêiner Docker rodando com permissão de "Root". O SAST não sabe disso, mas o DAST descobre ao forçar um comportamento que só se manifesta durante o processamento de requisições reais.
*   **Visão Sênior (Vulnerabilidades/Escala):** A lentidão extrema. Rodar um scan de DAST completo em um e-commerce gigantesco pode durar 14 horas e encher o banco de dados de lixo ("Test_User_123"). Além disso, o DAST sofre do "Efeito Caixa-Preta": ele te avisa que "A rota /comprar está vulnerável a SQLi", mas ele não te diz *em qual das 5.000 linhas do controlador Java* o problema ocorreu. Isso gera atrito entre a segurança e o desenvolvimento. Nunca deve ser rodado em Produção sem isolamento rigoroso, pois executa rotinas destrutivas.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O SAST lê a planta da casa. O [[DevSecOps_DAST]] é **o Ladrão encapuzado na porta da casa de madrugada**. Ele não sabe como a fechadura foi fabricada, mas ele chuta a porta, enfia um clipe na fechadura, tenta desligar a luz do poste e empurra a janela do banheiro. Ele simula o ataque pela fronteira do [[Cyber_Firewall_WAF]]. Ele testa o sistema em seu "estado de desespero natural".

#### 4. Pragmatismo Aplicado (Código e Implementação)
O uso canônico de ferramentas DAST open-source como o [[Ferramenta_OWASP_ZAP]] rodando de forma embutida via Docker no pipeline para disparar o tráfego ofensivo contra um servidor de homologação:
```bash
# Invocando o scanner ativo DAST do ZAP contra a URL de testes do projeto
docker run -t owasp/zap2docker-stable zap-baseline.py -t https://api.homolog.minhaempresa.com.br
````

5. História do Conteúdo

Nos anos 2000, o teste de invasão ([[Cyber_Pentest]]) era puramente manual e custava fortunas. Especialistas usavam proxies para interceptar tráfego web e adulterar campos. O mercado percebeu que 80% desse trabalho manual de "escrever ' OR 1=1 -- nas barras de pesquisa" era um trabalho de macaco e podia ser escrito em scripts. Esses scripts evoluíram para os motores de varredura ativa modernos, democratizando a mentalidade do Red Team para o fluxo de Integração Contínua (CI).