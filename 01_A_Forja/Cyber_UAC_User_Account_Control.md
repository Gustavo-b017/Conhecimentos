---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_UAC

#### 1. O Axioma (A Definição Rígida)
**O que é:** O User Account Control (UAC) é uma arquitetura de segurança nativa do Windows que restringe a execução de softwares aos privilégios de um usuário padrão até que uma elevação de autoridade seja explicitamente autorizada e confirmada na tela.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Mesmo que você esteja logado na conta de Administrador do Windows, o kernel do sistema o trata com um "Token de Acesso Restrito" por padrão. Se um programa tenta alterar arquivos críticos do sistema ou o Registro, o UAC pausa a execução, escurece o restante da tela (Desktop Seguro) e exibe uma caixa de diálogo exigindo um clique manual ("Sim/Não") ou uma credencial.
* **O Problema que Causa:** Acabou com o "Oeste Selvagem" do Windows XP, onde os usuários operavam permanentemente como Administradores. Sem o UAC, qualquer [[Cyber_Malware_Worm]] ou Trojan que entrasse na máquina ganhava controle de "Deus" (Root) instantaneamente de forma invisível.
*   **Visão Sênior (Vulnerabilidades/Escala):** O calcanhar de Aquiles do UAC é a psicologia. Foi apelidado de "Fadiga de Clique". Se o sistema grita a cada 5 minutos, o usuário entra em transe e clica em "Sim" para absolutamente tudo de forma instintiva. Além disso, hackers exploram binários nativos de "Auto-Elevação" da própria Microsoft (UAC Bypass) para forçar o sistema a dar privilégios máximos aos vírus sem que a caixa de aviso apareça para o usuário.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_UAC]] é **o gerente de banco precisando girar a chave do caixa**. O funcionário do caixa (o Usuário Padrão) pode receber depósitos e pagar contas normais de forma livre e autônoma. Porém, se alguém tenta sacar 1 Milhão de Reais (Uma alteração de sistema), o teclado trava. O caixa precisa chamar o Gerente (O Prompt do UAC), que vai até lá fisicamente, analisa a transação, digita a senha master dele e libera aquela execução específica, retornando o caixa ao status de restrição logo em seguida.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Profissionais de segurança não configuram o UAC clicando em painéis. Em escalas corporativas, as Políticas Locais (Local Policies Security Options) listadas no material da FIAP são injetadas em milhares de máquinas simultaneamente via Intune ou Active Directory:
```powershell
# Script em PowerShell manipulando o Registro para forçar o UAC a pedir a senha administrativa sempre (evitando o simples clique no "Sim")
Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "ConsentPromptBehaviorAdmin" -Value 1
````

5. História do Conteúdo

Foi a resposta drástica da Microsoft no Windows Vista (2007) à enxurrada de vírus do Windows XP. A implementação inicial foi desastrosa: o sistema era tão paranoico e gerava tantos pop-ups para tarefas banais (como mudar a hora do relógio) que se tornou o alvo principal de piadas na indústria tech (como nas famosas propagandas de TV "Mac vs PC" da Apple). A Microsoft foi forçada a refinar a agressividade nos Windows 7 e 10, tornando-o o padrão silencioso, mas letal, de contenção moderna.