---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_SDA_SGT

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Software-Defined Access (SDA) alicerçado por Security Group Tags (SGT) é a fundação da microsegmentação de redes Zero Trust, substituindo a dependência de endereços IP estáticos por identidades criptográficas anexadas diretamente ao cabeçalho do pacote.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** O usuário se autentica na porta do switch (usando 802.1X/MAB). O servidor de políticas (como o Cisco ISE) devolve uma Tag de 16 bits (SGT) representando o seu nível de acesso (ex: Tag 10 = RH, Tag 20 = IoT). O Switch injeta essa Tag no protocolo de encapsulamento **VXLAN-GPO**. Quando o pacote tenta acessar o servidor de Finanças, o switch de destino (Egress) lê a Tag e aplica a SGACL (Security Group ACL) bloqueando ou permitindo o acesso, sem nunca olhar para o [[Rede_IP]].
*   **O Problema que Resolve:** O inferno de gestão e os buracos do perímetro de ACLs tradicionais. Antes, as regras de firewall de LAN eram baseadas na tabela IP. Se um funcionário do RH (IP 10.0.1.5) mudasse de prédio e pegasse outro IP, ele perdia seus acessos ou ganhava acessos indevidos. SGT resolve a mobilidade absoluta: a sua restrição viaja amarrada à sua identidade, independentemente do prédio físico ou switch em que você esteja .
*   **Visão Sênior (Vulnerabilidades/Escala):** Para funcionar ponta-a-ponta, a infraestrutura inteira precisa entender e propagar (Inline Tagging) a marcação no cabeçalho. Se os pacotes passarem por um equipamento de rede antigo ou não homologado que "limpa" (stripping) a marcação SGT, a identidade é perdida no meio do caminho. Para contornar, utiliza-se o protocolo legado SXP (SGT Exchange Protocol) para transportar a marcação via TCP fora de banda, aumentando a complexidade de manutenção.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O SDA com SGT transforma o controle de rede num **Sistema de Pulseiras V.I.P de um Festival de Música**. O controle arcaico de IP (ACLs tradicionais) era o segurança verificando a placa do carro que você chegou no evento para decidir em qual área você podia entrar (completamente ilógico, pois você pode ter vindo de táxi). O SGT é a Pulseira Colorida: assim que você entra (Autenticação 802.1X), o segurança amarra uma pulseira inviolável no seu braço. A partir daquele instante, não importa em qual palco (Switch) do festival você esteja caminhando; os seguranças locais olham a cor da pulseira e sabem instantaneamente se você pode acessar o camarote ou não.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação do enforcement (SGACL) muda completamente a sintaxe. Ao invés de `permit ip 192.168.0.0 10.0.0.0`, as regras tornam-se semânticas baseadas no dicionário de Tags:
```bash
# Aplicação de política estática de TrustSec diretamente na porta
interface GigabitEthernet1/0/1
 cts manual
 policy static sgt 10 trusted  # O usuário dessa porta é obrigatoriamente a Tag 10 (RH)
 propagate sgt

# A matriz de acesso SGACL que barra lateralidade:
# "Bloqueie o RH (Tag 10) de acessar Finanças (Tag 20) ou IoT (Tag 30)"
ipv4 access-list role-based DENY-RH
 10 deny sgt 10 dgt 20
 20 deny sgt 10 dgt 30
 30 permit ip
````

5. História do Conteúdo

Criado em resposta ao colapso do perímetro. Nas corporações, o advento da política BYOD (Bring Your Own Device) nos anos 2010 encheu a infraestrutura de dispositivos desconhecidos. As ACLs dos roteadores núcleo chegaram a ter dezenas de milhares de linhas impossíveis de debugar. A introdução do TrustSec pela Cisco, seguido pela evolução nativa do SD-Access, forçou o mercado a mover a decisão de segurança da "fronteira do prédio" para "o exato momento do plugar do cabo"