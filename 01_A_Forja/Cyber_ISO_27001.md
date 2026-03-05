---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_ISO_27001

#### 1. O Axioma (A Definição Rígida)
**O que é:** A ISO/IEC 27001 é o padrão global absoluto que especifica os requisitos para estabelecer, implementar, manter e melhorar continuamente um Sistema de Gestão de Segurança da Informação (SGSI/ISMS) dentro do contexto dos riscos do negócio.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Ela não te diz *como* apertar os parafusos do servidor; ela te obriga a criar um processo administrativo documentado. Exige que a diretoria assuma a responsabilidade, que os riscos sejam mapeados matematicamente ([[Cyber_Risco|Gestão de Riscos]]) e que existam auditorias internas periódicas.
*   **O Problema que Resolve:** Elimina a segurança cibernética baseada no "achismo" técnico. Fornece uma chancela internacional (Certificação) que atesta para o mercado e parceiros B2B que a sua empresa não trata a proteção de dados como um hobby de TI.
*   **Visão Sênior (Vulnerabilidades/Escala):** A maior falha na adoção da ISO 27001 é a burocratização cega. Muitas empresas forjam toneladas de PDFs inúteis apenas para passar na auditoria anual, enquanto, na prática (no terminal de comando), os servidores continuam expostos e vulneráveis. O certificado na parede não blinda a rede contra um [[Cyber_Vulnerabilidade_Zero_Day|Zero-Day]], apenas prova que você tem um plano de contenção quando o desastre ocorrer.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A [[Cyber_ISO_27001]] é o **Plano Diretor de um Município**. O Plano Diretor dita que todo prédio precisa ter um sistema de esgoto, uma saída de emergência e regras de zoneamento para evitar o colapso da cidade. Ele é estritamente administrativo e jurídico. Contudo, o Plano Diretor *não* ensina o pedreiro a misturar o cimento ou calcular a pressão do cano (para isso, usa-se a [[Cyber_ISO_27002]]).

#### 4. Pragmatismo Aplicado (Código e Implementação)
*(A ISO 27001 não é código, é governança. A sua implementação ocorre através da confecção do documento mestre do SGSI: A Política de Segurança da Informação).*
Exemplo de declaração obrigatória de SGSI:
```text
"Política de Controle de Acesso:
1. Todo ativo de informação crítica deve ser acessado via Autenticação Multifator ([[Cyber_MFA|MFA]]).
2. O princípio do Menor Privilégio ([[Cyber_Zero_Trust|Zero Trust]]) será imposto a todos os usuários.
3. Auditorias de contas inativas devem ser rodadas a cada 90 dias pelos gestores de área."
````

5. História do Conteúdo

Nasceu da norma britânica BS 7799 na década de 1990, quando o governo do Reino Unido percebeu que as empresas estavam se digitalizando sem qualquer bússola gerencial. Foi publicada oficialmente pela Organização Internacional para Padronização (ISO) em 2005 e revisada recentemente para abranger a rápida escalada do trabalho remoto e da computação em nuvem.