---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_RTO

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Recovery Time Objective (RTO), ou Objetivo de Tempo de Recuperação, é a métrica corporativa mandatória que define o tempo máximo tolerável que um computador, sistema, rede ou aplicação pode ficar inoperante após uma falha ou desastre cibernético antes que cause danos inaceitáveis ao negócio.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** É um cronômetro de contagem regressiva. Se o RTO do servidor de vendas for de 4 horas, a equipe de TI e segurança tem exatamente 4 horas a partir do momento em que o servidor cai ou sofre um [[Cyber_Ataque_DDoS]] para restaurá-lo e voltar a operar.
* **O Problema que Causa:** Elimina a subjetividade da área técnica ("vamos consertar o mais rápido possível") e impõe um acordo contratual rígido entre a TI e a Diretoria sobre o nível de investimento em redundância necessário.
*   **Visão Sênior (Vulnerabilidades/Escala):** A falha fatal na gestão de crise é estabelecer um RTO de 15 minutos, mas manter uma arquitetura barata (como backups locais em fita). Se o data center queimar, reconstruir servidores físicos do zero leva dias. RTOs agressivos (próximos de zero) exigem orçamentos astronômicos com replicação ativa em nuvem (Alta Disponibilidade) espalhada por múltiplos continentes.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_RTO]] é o **limite de oxigênio de um mergulhador**. Quando o suprimento de ar principal (o Servidor) falha debaixo d'água, o mergulhador não morre imediatamente. Ele tem os pulmões cheios (a tolerância do negócio). O RTO é a quantidade exata de minutos que a equipe de resgate tem para entregar um cilindro de ar reserva antes que a asfixia (a falência comercial) seja irreversível.

#### 4. Pragmatismo Aplicado (Código e Implementação)
*(O RTO não é escrito em código, mas dita como a arquitetura do código de infraestrutura é feita. Um RTO de minutos exige automação via Terraform/Kubernetes para subir réplicas instantâneas. Abaixo, uma declaração de lógica num documento de DRP - Disaster Recovery Plan).*
```text
Ativo: Banco de Dados de Pagamentos (PostgreSQL)
RTO: 30 Minutos.
Mitigação Exigida: Réplica de Leitura/Escrita Ativa-Ativa na AWS (usando Multi-AZ). Em caso de queda do Node A, o Load Balancer deve redirecionar o tráfego para o Node B em menos de 10 segundos.
````

5. História do Conteúdo

Criado no berço dos planejamentos de Continuidade de Negócios (Business Continuity Planning - BCP) do setor financeiro nos anos 1980 e padronizado em normas como a ISO 22301 e materiais do [[Cyber_PCI_DSS]]. Diretores de bancos precisavam de uma régua para calcular o quanto custava cada segundo do sistema inoperante versus o quanto custava manter um computador extra desligado esperando uma emergência.