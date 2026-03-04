---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/4_evergreen
---

### Cyber_Zero_Trust

#### 1. O Axioma (A Definição Rígida)
**O que é:** Zero Trust (Confiança Zero) é a arquitetura e filosofia de segurança que abole o conceito de "rede interna confiável", exigindo que absolutamente todo usuário, dispositivo e aplicativo seja autenticado, autorizado e validado continuamente antes de receber acesso a qualquer recurso.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Opera sob três pilares: **Verifique Explicitamente** (sempre exija [[Cyber_MFA]] e cheque a saúde do PC), **Use o Menor Privilégio** ([[Cyber_IAM]] restrito a Just-In-Time) e **Assuma a Violação** (assuma que o hacker já está na rede, logo, use micro-segmentação para impedi-lo de se mover).
*   **O Problema que Resolve:** Assassina a vulnerabilidade de Movimentação Lateral. No modelo antigo (Perímetro), se um [[Cyber_Malware_Trojan]] passasse pelo [[Rede_Firewall|Firewall]], ele confiava cegamente no IP local e infectava tudo. No Zero Trust, o IP não vale nada. A rede exige a "identidade" do dispositivo a cada novo clique.
*   **Visão Sênior (Vulnerabilidades/Escala):** Zero Trust não é um software que você compra numa caixa, é uma reestruturação cultural brutal. A maior falha é o atrito (Friction) com os sistemas legados. Máquinas industriais (IoT) antigas ou sistemas de contabilidade de 1998 não suportam tokens MFA modernos ou criptografia mútua. Tentar impor Zero Trust num chão de fábrica desatualizado paralisa a produção.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O modelo antigo de redes ([[Cyber_VPN_Mecanica|VPN]]/Firewall) era o **Castelo Medieval com um Fosso**. Era muito difícil atravessar o fosso, mas se você nadasse por baixo e entrasse no pátio, você podia entrar no quarto do rei porque ninguém mais pedia sua identidade lá dentro. 
O [[Cyber_Zero_Trust]] é um **Prédio de Segurança Máxima com crachás biométricos em TODAS as portas**. Passar pela porta da frente não te dá o direito de abrir a porta do banheiro, nem a porta do elevador, nem a porta da sala. Você tem que provar quem é a cada metro quadrado que avança.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação moderna (como no [[Cyber_IAM|Microsoft Entra ID]] - Conditional Access) baseia-se em código declarativo de postura (Posture Check). A porta só abre se a equação for verdadeira:
```json
// Regra de Acesso Zero Trust: O usuário tem a senha, tem o MFA, mas o acesso será NEGADO se o antivírus do PC estiver desatualizado.
{
  "conditions": {
    "deviceState": {
      "includeStates": ["Compliant", "Managed"]
    },
    "riskLevel": ["low"]
  },
  "grantControls": {
    "operator": "AND",
    "builtInControls": ["mfa"]
  }
}
````

5. História do Conteúdo

Criado em 2010 por John Kindervag, analista da Forrester Research. Na época, a indústria riu dele, chamando o conceito de inviável e paranoico. Uma década depois, com o apagamento das fronteiras corporativas devido à nuvem (AWS/Azure) e ao trabalho remoto pandêmico, o governo dos Estados Unidos emitiu uma Ordem Executiva (Memorando 14028) obrigando que todas as agências federais adotassem a arquitetura Zero Trust como padrão único de sobrevivência cibernética.