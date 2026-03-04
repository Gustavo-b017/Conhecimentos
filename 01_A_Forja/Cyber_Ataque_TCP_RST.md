---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/media
  - status/3_incubadora
---

### Cyber_Ataque_TCP_RST
#### 1. O Axioma (A Definição Rígida)
**O que é:** Um ataque de interrupção forçada onde o invasor emite pacotes forjados contendo a flag RST (Reset) para quebrar abruptamente uma sessão de rede já estabelecida entre dois nós legítimos.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente do [[Cyber_Ataque_DDoS_SYN_Flood|SYN Flood]] que busca exaustão, o invasor aqui escuta o tráfego ou adivinha os números de sequência e forja um pacote RST passando-se por uma das partes da comunicação. Quando o alvo recebe o pacote, a pilha [[Rede_TCP|TCP]] obedece cegamente a regra da [[Rede_TCP_Flags_e_Header|flag RST]] e encerra a conexão, fazendo com que a aplicação caia e tente se reconectar em loop.
*   **O Problema que Causa:** Causa negação de serviço focada e cirúrgica. Se um usuário estiver assistindo a um streaming de vídeo, o ataque corta o fluxo de dados na origem, forçando a interface gráfica a travar na tentativa inútil de restabelecer o link.
*   **Visão Sênior (Vulnerabilidades/Escala):** É uma técnica letal por não consumir muita banda do atacante (basta um único pacote bem calculado para destruir a sessão). É frequentemente abusada por governos autoritários e sistemas de censura (como o Grande Firewall da China) para derrubar conexões HTTP não encriptadas para sites proibidos no momento exato em que a palavra proibida trafega na rede, atuando como um [[Cyber_IPS]] maligno.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O [[Cyber_Ataque_TCP_RST]] é o **falsário entregando uma carta de divórcio imediato**. O marido e a mulher estão conversando via correios. O invasor rouba a estética do envelope e manda uma carta para a mulher assinada em nome do marido dizendo: "Acabou, não me procure mais" (flag Reset da [[Rede_TCP_Flags_e_Header]]). A mulher destrói a comunicação imediatamente. Quando o verdadeiro marido tenta mandar a próxima mensagem, a mulher rejeita o pacote. A comunicação morre por estrita obediência burocrática à mentira.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Disparo laboratorial do ataque injetando flags de reset usando a ferramenta de testes `netwox` (módulo 78).
```bash
# Executa o netwox instruindo a injeção contínua de pacotes RST na rede para quebrar conexões ativas
netwox 78
````

5. História do Conteúdo

A flag RST nunca foi concebida como uma arma. Os pais do TCP a criaram como um disjuntor de emergência: se um computador reiniciasse sozinho e outro tentasse conversar com ele, o que reiniciou mandava um "RST" avisando que havia perdido a memória da conversa. O ataque é apenas a subversão letal da ferramenta de limpeza original.