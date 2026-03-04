---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Rede_HSRP
#### 1. O Axioma (A Definição Rígida)
**O que é:** O Hot Standby Router Protocol (HSRP) é um protocolo proprietário da Cisco de redundância de primeiro salto (FHRP) que agrupa dois ou mais roteadores físicos para que operem sob um único endereço IP e MAC virtual, garantindo alta disponibilidade.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Você tem o Roteador A (Ativo) e o Roteador B (Standby). Ambos configuram uma "Identidade Fantasma" (IP Virtual). Todos os PCs da empresa configuram esse IP Virtual como seu Gateway Padrão. O Roteador A processa todo o tráfego. Se o A queimar e parar de enviar mensagens de vida (Hellos), o Roteador B assume instantaneamente o IP Virtual e continua o serviço.
*   **O Problema que Resolve:** O Ponto Único de Falha (SPOF) do Gateway. Se a sua rede tem apenas um roteador apontando para a internet, quando ele morre, todos os PCs perdem a conexão até a TI intervir. O HSRP automatiza o failover.
*   **Visão Sênior (Vulnerabilidades/Escala):** O HSRP clássico é de modelo *Ativo/Passivo*. Isso significa que se você comprou dois roteadores de US$ 10.000, um deles vai passar 99% do tempo sem fazer absolutamente nada, apenas esperando o outro morrer. Isso é um desperdício monstruoso de capacidade (CAPEX). A mitigação tática envolve rodar múltiplas instâncias de HSRP (MHSRP) atreladas a diferentes [[Rede_VLAN]]s, forçando o Roteador B a ser ativo para o RH enquanto é standby para o Financeiro.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O protocolo HSRP é o **Sistema de Co-Pilotos de um Avião Comercial**. O avião (os PCs da rede) está sendo pilotado ativamente pelo Comandante (Roteador A). O Co-Piloto (Roteador B) está sentado ao lado, com as mãos milímetros acima do manche, monitorando a respiração do Comandante. O manche inteiro é o "IP Virtual". Se o Comandante sofrer um infarto fulminante, o Co-Piloto agarra o manche no mesmo segundo. Os passageiros na cabine (os pacotes de dados) sequer sentem uma turbulência.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação em portas de interface de rede dita o nível de prioridade (quem manda) e a permissão para tomar o poder de volta se o roteador principal reiniciar (Preempt):
```bash
interface GigabitEthernet0/1
 ip address 192.168.1.2 255.255.255.0
 standby 1 ip 192.168.1.1       # O IP Virtual Fantasma que os PCs vão usar
 standby 1 priority 110         # Prioridade maior vence a eleição
 standby 1 preempt              # Se eu voltar a viver, devolva meu cargo
````

5. História do Conteúdo

Criado pela Cisco em 1994, o HSRP foi a primeira resposta comercial à fragilidade dos gateways estáticos. Na época, se a placa de rede do servidor central fritasse, os administradores tinham que correr para centenas de máquinas Windows 95 e alterar manualmente a configuração de rede de cada uma delas. A criação da "Redundância de Primeiro Salto" permitiu o surgimento de Data Centers ininterruptos.