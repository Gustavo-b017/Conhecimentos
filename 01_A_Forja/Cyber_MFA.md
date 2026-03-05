---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_MFA

#### 1. O Axioma (A Definição Rígida)
**O que é:** A Autenticação Multifator (MFA) é um controle de segurança de identidade que exige que o usuário apresente duas ou mais provas de autenticidade independentes (algo que ele sabe, algo que ele tem, ou algo que ele é) antes de conceder acesso a um sistema.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O processo tradicional de login baseia-se em "Algo que você sabe" (a senha). O MFA adiciona camadas ortogonais: "Algo que você tem" (um token de hardware FIDO2, um celular com [[Ferramenta_Google_Authenticator|Google Authenticator]] gerando um TOTP) ou "Algo que você é" (biometria, impressão digital). A equação só abre a porta se as matrizes baterem simultaneamente.
*   **O Problema que Resolve:** Assassina a eficácia do [[Cyber_Phishing]] e do [[Cyber_Eavesdropping]]. Se o hacker roubar a sua senha no meio do tráfego (ou via [[Cyber_Malware_Keylogger]]), ela é inútil sozinha, pois ele não possui o dispositivo físico que gera o código temporário exigido no segundo passo.
*   **Visão Sênior (Vulnerabilidades/Escala):** O MFA baseado em SMS (Mensagem de Texto) é considerado obsoleto e vulnerável a ataques de *[[Cyber_Vishing|SIM Swapping]]* (onde o invasor suborna o funcionário da operadora de celular para transferir o seu número para o chip dele). O vetor de ataque moderno contra MFAs de aplicativos é o *MFA Fatigue* (Fadiga de MFA): o atacante bombardeia o celular da vítima com 500 pedidos de aprovação de login de madrugada até que o usuário, irritado e sonolento, clique em "Aprovar" apenas para fazer o celular parar de apitar.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_MFA]] é a **Regra das Duas Chaves de um Silo Nuclear**. Nenhum general possui o poder de girar uma chave e lançar um míssil sozinho. É exigido que duas pessoas diferentes (fatores independentes), portando chaves físicas distintas, girem as fechaduras em painéis separados exatamente no mesmo milissegundo. O vazamento de uma chave (a Senha) não inicia a ignição.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação em servidores [[OS_Linux|Linux]] para proteger o acesso [[Rede_SSH|SSH]] ([[Cyber_Malware_Backdoor|Backdoor]]) exige a instalação do módulo PAM (Pluggable Authentication Module) do Google Authenticator.
```bash
# Instala o gerador de TOTP (Time-Based One-Time Password)
sudo apt install libpam-google-authenticator

# No arquivo /etc/pam.d/sshd, adicionamos a obrigatoriedade da verificação do token logo após a senha:
auth required pam_google_authenticator.so
````

5. História do Conteúdo

Surgiu no mundo corporativo financeiro através dos antigos _Tokens_ físicos da RSA SecurID nos anos 90 (aqueles chaveirinhos de banco que trocavam o número a cada 60 segundos). Era caro e restrito a executivos. Com a popularização dos smartphones, empresas como Google e Microsoft virtualizaram o hardware do token para dentro de aplicativos, democratizando o controle de [[Cyber_IAM|identidade]] e tornando-o o pilar fundamental da filosofia [[Cyber_Zero_Trust]].