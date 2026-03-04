---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

### Rede_LAN
#### 1. O Axioma (A Definição Rígida)
**O que é:** A Local Area Network (LAN) é uma rede de computadores restrita a uma área geográfica pequena e delimitada (um prédio, um escritório ou uma casa), caracterizada por altíssima velocidade, baixa latência e propriedade privada da infraestrutura.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Utiliza tecnologias de Camada 1 e 2 (Cabos Ethernet de cobre e Switches) para interligar os dispositivos finais. Quando é totalmente sem fio (via Wi-Fi), recebe o agregado lógico de **WLAN** (Wireless Local Area Network).
*   **O Problema que Resolve:** Permite o compartilhamento de recursos locais pesados (arquivos em servidores, impressoras) sem a necessidade de enviar esses dados para a internet pública, economizando banda e garantindo velocidade bruta (1 Gbps a 100 Gbps).
*   **Visão Sênior (Vulnerabilidades/Escala):** O maior risco de uma LAN é o perímetro interno. Se um atacante pluga um cabo na parede do escritório, ele está na LAN. Em redes grandes, o excesso de máquinas na mesma LAN gera "Broadcast Storms" (tempestades de gritos na rede que travam o Switch), forçando a adoção obrigatória de [[Rede_VLAN]] para segmentar o caos.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A LAN é a sua **Casa e o seu Quintal**. Você comprou os móveis (Switches), você decide quem tem a chave da porta (Wi-Fi Password) e, lá dentro, as pessoas podem correr em alta velocidade de um quarto para o outro sem pagar pedágio. Na culinária, é a cozinha do restaurante: a comunicação entre o Chef e o sub-chef é instantânea, não precisa de um despachante. Se a sua casa usa apenas roteadores Wi-Fi sem cabos, você está operando essencialmente uma WLAN.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Para descobrir a sua configuração de LAN atual e o gateway (a porta de saída para a WAN):
**No Windows:**
```powershell
ipconfig
# Olhe para a seção "Ethernet adapter" ou "Wireless LAN adapter". O seu IP privado (ex: 192.168.x.x) pertence à LAN.
````

5. História do Conteúdo

A LAN nasceu na década de 1970, nos laboratórios da Xerox PARC, com a invenção da Ethernet. Antes disso, os computadores eram "ilhas" ou usavam links seriais lentíssimos. A motivação inicial não foi conectar computadores entre si, mas sim resolver um problema logístico muito específico e caro: permitir que dezenas de computadores caríssimos na mesma sala conseguissem enviar documentos para a recém-inventada (e única) impressora a laser do laboratório.