---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

### Rede_SAN
#### 1. O Axioma (A Definição Rígida)
**O que é:** A Storage Area Network (SAN) é uma rede paralela, de altíssima velocidade e baixíssima latência, isolada da rede corporativa principal, dedicada exclusivamente a interligar servidores de processamento a gigantescos pools de discos de armazenamento no nível de blocos de dados.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Em vez do servidor guardar arquivos no próprio "HD interno" (DAS - Direct Attached Storage), ele é conectado a um Switch de SAN por cabos ópticos usando protocolos alienígenas ao TCP/IP, como o **Fibre Channel (FC)**. O servidor requisita dados à SAN como se o disco de 50 Terabytes estivesse espetado na própria placa-mãe dele.
*   **O Problema que Resolve:** O limite de escalabilidade e o tráfego pesado. Se um banco de dados tentar ler terabytes de arquivos usando a mesma rede [[Rede_LAN]] onde os funcionários estão assistindo vídeos e baixando planilhas, a rede inteira vai asfixiar. A SAN tira o tráfego pesado dos dados do caminho dos usuários comuns.
*   **Visão Sênior (Vulnerabilidades/Escala):** Arquiteturas SAN tradicionais baseadas em Fibre Channel são um "bicho de 7 cabeças". Elas usam cabos específicos, placas HBA caras, switches caros e exigem engenheiros ultra-especializados. O custo de manter esse isolamento forçou as empresas modernas a migrarem para o padrão **iSCSI** ou FCoE (Fibre Channel over Ethernet), que são "gambiarras" geniais para jogar o tráfego da SAN por dentro da LAN comum usando a inteligência de Virtualização.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Usar uma SAN é como gerenciar a **Logística de Bebidas de um Estádio de Futebol gigante**. Se o fornecedor trouxesse os barris de chopp carregando-os pelas escadas e cadeiras da arquibancada enquanto a torcida (Tráfego da LAN) tenta assistir ao jogo, haveria o caos. Em vez disso, os engenheiros constroem um sistema de tubulação subterrânea pressurizada de aço dedicado exclusivamente para transportar o líquido dos tanques direto para as torneiras. A torcida não vê, mas o serviço é contínuo e sem atrito.

#### 4. Pragmatismo Aplicado (Código e Implementação)
Trabalhar com SAN não envolve comandos tradicionais de IP (ping ou ssh), mas sim a configuração pesada de *Zoning* (zonas de visibilidade) nos switches Fibre Channel. Você precisa declarar explicitamente no painel do switch SAN que o Ponto A (Placa HBA do Servidor) tem permissão física de enxergar o Ponto B (LUN de Disco do Storage Array), usando identificadores WWN em vez de IPs ou MACs.
```text
# Exemplo do identificador global WWN de uma placa de SAN:
10:00:00:00:c9:22:fc:01
````

5. História do Conteúdo

Criada na virada da década de 1990 para 2000. Com a explosão do e-commerce e dos grandes bancos de dados relacionais Oracle, as empresas perceberam que entupir um servidor com dezenas de discos rígidos mecânicos gerava calor extremo e limitava a capacidade. A SAN inventou a "externalização da inteligência de armazenamento", permitindo que os administradores criassem datacenters onde os servidores de processamento ficassem em uma sala, e os discos rígidos de toda a empresa ficassem blindados, replicados e gelados em um galpão separado.