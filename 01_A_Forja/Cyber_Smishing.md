---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Cyber_Smishing

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Smishing (SMS Phishing) é a variação letal do Phishing executada exclusivamente através de mensagens de texto (SMS) ou aplicativos de mensageria móvel.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Em vez de entupir caixas de e-mail, o criminoso envia mensagens curtas com links encurtados (bit.ly) fingindo ser alertas de bancos, pacotes retidos nos correios ou aprovações de crédito ([[Cyber_Phishing]]).
- **O Problema que Resolve:** Para o atacante, contorna todos os [[Rede_Firewall|firewalls corporativos]] e filtros de e-mail institucionais ([[Cyber_Engenharia_Social_Spam|Anti-Spam]]), enviando o ataque diretamente para o dispositivo físico pessoal da vítima, que geralmente está fora da malha de proteção da TI da empresa.
- **Visão Sênior (Vulnerabilidades/Escala):** A psicologia humana julga o SMS como um canal mais íntimo e autêntico que o e-mail. Além disso, a tela pequena do celular dificulta a auditoria visual da URL maliciosa. A vulnerabilidade corporativa extrema ocorre quando um funcionário usa o celular pessoal para acessar o ambiente de trabalho (BYOD) e clica em um Smishing, comprometendo a rede inteira.

#### 3. As Sinapses (Conexões Livres)
O [[Cyber_Smishing]] é o **estelionatário que não envia cartas, ele bate na janela do seu carro**. Pelo fato do celular estar fisicamente no seu bolso e tremer, o senso de urgência exigido pela [[Cyber_Engenharia_Social]] é exponencialmente maior do que um e-mail parado na caixa de entrada. Quando você recebe um aviso sonoro dizendo "Sua conta bancária acaba de ser travada, clique aqui", a adrenalina impede o pensamento crítico.

#### 4. Pragmatismo Aplicado (Código/Implementação)
Não há terminal para mitigar isso do lado do usuário, mas no nível corporativo, usa-se sistemas de MDM (Mobile Device Management) como o [[Ferramenta_Microsoft_Intune]] para bloquear a abertura de domínios desconhecidos nos aparelhos móveis da empresa.
```json
// Política de MDM injetada no aparelho móvel impedindo cliques oriundos de mensageiros não controlados
{
  "RestrictionPolicy": {
    "AllowSMSLinks": false,
    "ForceBrowserSafeBrowsing": true
  }
}
````

5. História do Conteúdo

A ascensão do Smishing acompanhou diretamente o boom dos smartphones e dos pacotes de SMS ilimitados na última década. Ele se aproveita do fato de que o número de telefone se tornou a chave de autenticação universal para aplicativos da vida moderna, desde WhatsApp até bancos.