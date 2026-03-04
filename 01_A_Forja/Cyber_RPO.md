---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_RPO

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Recovery Point Objective (RPO), ou Objetivo de Ponto de Recuperação, é a métrica mandatória de continuidade de negócios que define a quantidade máxima de perda de dados (medida em tempo) que uma organização tolera suportar após um desastre.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ele dita matematicamente a frequência dos seus backups. Se a diretoria define que o RPO do banco de dados de vendas é de 1 hora, a TI é obrigada a configurar o [[Ferramenta_Rsync]] ou sistema de  *Snapshots* para rodar a cada 60 minutos. 
*   **O Problema que Resolve:** Resolve o descompasso entre a expectativa da diretoria e a realidade da TI. Se um [[Cyber_Malware_Ransomware]] criptografa o servidor às 16h00 e o seu último backup foi feito à meia-noite (RPO real de 16 horas), a empresa perdeu um dia inteiro de faturamento. O RPO força o investimento preventivo na periodicidade da cópia.
*   **Visão Sênior (Vulnerabilidades/Escala):** O RPO é inimigo do orçamento. Um RPO de 24 horas exige apenas uma fita magnética barata rodando de madrugada. Um RPO de "Zero Segundos" (Nenhuma perda de dado tolerada) exige espelhamento síncrono em fibra óptica dedicada entre dois Data Centers distintos, custando milhões. A vulnerabilidade gerencial é a empresa estipular um RPO de 5 minutos, mas comprar hardware que só aguenta fazer backup a cada 5 horas.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A diferença entre [[Cyber_RTO]] e [[Cyber_RPO]] é a mecânica do **"Save Game" em um Videogame**. 
O **RPO** é de quanto em quanto tempo o jogo salva o seu progresso automaticamente. Se a luz cair e seu último "save" foi há 3 horas, você perdeu 3 horas de jogo (Sua perda de dados).
O **RTO** é o tempo que o seu videogame demora para reiniciar, carregar o sistema e abrir o menu para você voltar a jogar. 

#### 4. Pragmatismo Aplicado (Código e Implementação)
O RPO dita o código de agendamento (Cron) da infraestrutura. Para garantir um RPO rígido de 1 hora num servidor Linux usando sincronização para um disco externo, o engenheiro injeta a seguinte linha no `crontab`:
```bash
# Executa o backup rsync rigorosamente no minuto zero de cada hora (*), todos os dias, garantindo um RPO de 60 minutos.
0 * * * * rsync -a /var/www/html/ /mnt/backup_seguro/
````

5. História do Conteúdo

O conceito de RPO foi cimentado na ISO 22301 (Business Continuity Management). Ganhou foco de vida ou morte na última década porque, diferentemente dos desastres naturais (incêndios) que destroem o hardware (afetando o RTO), o Cibercrime moderno (Ransomware) foca em destruir o dado enquanto o hardware continua intacto, fazendo da "frequência do backup" (RPO) a única linha de defesa real contra a falência.