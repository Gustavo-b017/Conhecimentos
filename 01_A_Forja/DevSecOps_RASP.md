---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/devsecops
---

### DevSecOps_RASP

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Runtime Application Self-Protection (RASP) é uma tecnologia de autodefesa armada e acoplada no núcleo da aplicação em produção, que possui autoridade e contexto interno para observar comportamentos abusivos em tempo de execução e abater os ataques no milissegundo em que eles tentam se concretizar.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Semelhante ao sensor IAST, ele se hospeda via instrumentação direta no servidor (no kernel da máquina virtual Java ou .NET). Ele não inspeciona rede bruta; ele fica na porta de entrada da API do banco de dados ou do sistema de arquivos. Antes de executar um `eval()` ou lançar uma string no banco, o RASP avalia a intenção. Se for maligna, ele encerra o processo com a força de um [[Cyber_IPS]] e descarta a requisição de dentro para fora
*   **O Problema que Resolve:** A cegueira e a ineficiência do [[Cyber_Firewall_WAF]]. O WAF tenta adivinhar ataques lendo pacotes de texto encriptados do lado de fora do castelo. O WAF erra muito e bloqueia usuários normais (Falso Positivo). O RASP resolve esse caos mitigando exploits obscuros como Insecure Deserialization e Zero-Days sem depender das defesas perimetrais de rede, com exatidão implacável.
*   **Visão Sênior (Vulnerabilidades/Escala):** Se o RASP não for bem ajustado, ele comete suicídio do negócio. Se ele achar que a rotina noturna de faturamento da empresa é um ataque de extração massiva, ele aniquila a esteira de pagamentos em produção instantaneamente. Além disso, introduz latência severa diretamente na aplicação, já que ele age como um juiz extra avaliando cada linha de execução. Não substitui o WAF, ele atua como a última linha de resistência.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O WAF é a  **Pele, o Suor e os Pelos** do corpo humano tentando impedir a entrada de uma bactéria. O [[DevSecOps_RASP]] é o **Sistema Imunológico de Glóbulos Brancos (Macrófagos) correndo nas veias**. Se o [[Cyber_Ataque_SQL_Injection]] encontrar um corte na pele (Vulnerabilidade cega) e entrar na corrente sanguínea (O fluxo de dados da RAM), os glóbulos brancos imediatamente cercam o vírus no nível intracelular e o devoram vivo antes que ele consiga se espalhar para os órgãos vitais (O Banco de Dados). É a segurança operando na própria biologia celular do software.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Igualmente ao IAST, não é um script isolado, é uma configuração residente no momento de injetar o App em produção. Geralmente ligado diretamente às engrenagens do orquestrador em *Kubernetes* ou Docker.
```dockerfile
# Dockerfile tático anexando a autodefesa nativa na compilação da imagem
FROM openjdk:17-alpine
COPY target/app.jar /app.jar
COPY rasp-agent.jar /rasp.jar
# A aplicação já sobe blindada de fábrica
ENTRYPOINT ["java", "-javaagent:/rasp.jar", "-jar", "/app.jar"]
````

5. História do Conteúdo

Cunhado pela Gartner em 2012 e tracionado anos depois. A criação do RASP foi a consequência do apocalipse filosófico da arquitetura de Segurança de Perímetro. Quando o modelo [[Cyber_Zero_Trust]] forçou a indústria a assumir matematicamente que o roteador seria invadido ("Assume Breach"), a responsabilidade de sobreviver foi empurrada para a última camada. A aplicação não podia mais ser uma caixa oca e frágil esperando que o Firewall a protegesse; ela teve que aprender a revidar usando artes marciais de defesa embutidas no próprio tecido de sua compilação.