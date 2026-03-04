---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

# Rede_VLAN

## 1. O Axioma (A Definição Rígida)
> **O que é:** A VLAN (Virtual LAN - 802.1Q) é a técnica de segmentação lógica que permite criar múltiplas redes isoladas dentro da mesma infraestrutura física de switches, separando domínios de broadcast.

## 2. A Desconstrução (Mecânica e Pontos de Falha)
* **Como Funciona:** O switch insere uma "Tag" (etiqueta) de 4 bytes no quadro Ethernet. Portas configuradas na VLAN 10 só falam com portas na VLAN 10.
* **O Problema que Resolve:** Segurança e Performance. Impede que o tráfego da rede de Visitantes acesse o Servidor Financeiro, e impede que um broadcast storm derrube a rede inteira.
* **Visão Sênior (Vulnerabilidades/Escala):** VLAN Hopping é um ataque onde o hacker engana o switch para pular de uma VLAN para outra. A mitigação exige desativar a negociação automática de trunk (DTP). VLANs são essenciais para conter [[Cyber_Malware_Worm]].

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
VLANs são **Paredes de Drywall** em um galpão aberto ([[Rede_Topologias]]). Fisicamente, todos estão no mesmo prédio (Switch), mas o pessoal do RH não consegue ouvir os gritos do pessoal de TI porque construímos uma parede acústica (Tag 802.1Q) entre eles. Para passar de uma sala para outra, é obrigatório passar pela porta com segurança (O Roteador/Firewall).

## 4. Pragmatismo Aplicado (Código e Implementação)
Configuração clássica em Switch Cisco (Criação e Atribuição).
```bash
# Criar a VLAN 10 para Dados
vlan 10
 name DADOS_TI
# Atribuir porta ao quarto isolado
interface Gi0/1
 switchport mode access
 switchport access vlan 10
```

# Informar que a porta física X pertence APENAS àquela parede lógica
Switch(config)# interface gigabitEthernet 0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
````

5. História do Conteúdo

No início dos anos 90, os cabos eram caros e mover um funcionário de departamento exigia que o técnico fosse até o armário do servidor e trocasse fisicamente os cabos de porta (um pesadelo logístico). W. David Sincoskie, um engenheiro de redes, concebeu a ideia da VLAN justamente para solucionar essa dor operacional: "E se a gente pudesse mudar a rede de um funcionário apenas digitando um comando de software no switch, sem ter que tocar em cabos físicos?". O que nasceu por preguiça logística, tornou-se hoje o padrão-ouro inegociável de segmentação e higiene cibernética.
## 5. História do Conteúdo
Surgiu quando as redes Ethernet cresceram demais e o tráfego de broadcast (gritos da rede) começou a consumir 30% da banda, paralisando CPUs.