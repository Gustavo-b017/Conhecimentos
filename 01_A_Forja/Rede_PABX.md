---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/3_incubadora
---

### Rede_PABX

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Private Branch Exchange (PABX) é a central telefônica privada de uma organização responsável por fornecer, rotear e gerenciar a comunicação interna entre dezenas de ramais de funcionários, compartilhando um número reduzido de linhas externas de operadoras telefônicas.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Em um ambiente PABX, um funcionário pode discar "205" para falar com o colega da mesa ao lado sem que a chamada chegue à rede da operadora externa (PSTN). Se ele precisar fazer uma ligação para o mundo exterior, o PABX "aluga" momentaneamente uma das linhas de rua ligadas ao prédio para discar o número.
- **O Problema que Resolve:** Economia de escala insana. Uma empresa com 1.000 funcionários precisaria pagar 1.000 fiações diretas à operadora. O PABX permite que a empresa compre apenas 30 linhas externas, partindo da probabilidade estatística de que os 1.000 funcionários nunca farão ligações para clientes fora do prédio simultaneamente. 
- **Visão Sênior (Vulnerabilidades/Escala):** O hardware físico do PABX evoluiu para o IP-PBX (baseado em software de roteamento pela internet, como o *Asterisk* e protocolos SIP). Se o PABX virtual for exposto na WAN sem restrição do Firewall, hackers forçam a autenticação do SIP e invadem a central. O resultado mais rápido é o *Toll Fraud*, onde invasores usam o PABX da empresa de madrugada para discar para números *premium* na África, gerando contas telefônicas astronômicas no dia seguinte, ou disfarçam a origem para aplicar o *Vishing* usando a identidade da sua organização.

#### 3. As Sinapses (Conexões Livres)
A arquitetura do PABX é idêntica ao conceito do **Roteador com função NAT (Network Address Translation)**. O NAT pega 500 computadores na rede privada e os oculta na rua sob um único número de IP público. O PABX faz isso para a voz: ele abriga 500 ramais privados sob o "guarda-chuva" de um único número principal de identificação. Quando um funcionário liga da sua mesa particular para fora, a pessoa na outra ponta só enxerga o telefone principal da recepção da corporação.

#### 4. Pragmatismo Aplicado (Código/Implementação)
*(Equipamentos de infraestrutura como sistemas Asterisk possuem uma programação pesada baseada no arquivo `extensions.conf` no Linux, ditando as regras estritas de dialplan (quem pode ligar para onde).*
```conf
# Restrição de segurança clássica em PABX (Asterisk)
# A regra diz que funcionários apenas podem fazer ligações internas locais. Proíbe expressamente chamadas internacionais (prevenção de Toll Fraud).
[ramais-internos]
exten => _2XX,1,Dial(SIP/${EXTEN})
exten => _00X.,1,Hangup() ; Se tentar discar padrão internacional (00), derrube a ligação instantaneamente.
````

5. História do Conteúdo

Antes de sua existência, grandes empresas dependiam de "telefonistas" humanas conectando cabos manualmente num quadro central dentro do prédio. A automação eletromecânica do PABX dominou a segunda metade do século 20, até que as fiações de cobre fossem completamente substituídas por computadores convertendo a voz em pacotes digitais (VoIP), migrando o trabalho dos engenheiros de telefonia para o escopo puramente de TI.