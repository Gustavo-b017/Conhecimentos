---
tags:
  - afinidade/alta
  - status/3_incubadora
  - tipo/conceito
  - contexto/dev/cyber/cloud
---

### Cyber_CWPP

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Cloud Workload Protection Platform (CWPP) é a tecnologia armada de observabilidade e bloqueio que desce até o núcleo do Sistema Operacional (Runtime) para defender ativamente os "motores" da nuvem (Máquinas Virtuais, Contêineres, Kubernetes e Serverless) contra execuções anômalas e injeções de malware.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Enquanto o [[Cyber_CSPM]] olha a "casca" da nuvem, o CWPP entra na máquina. Ele mapeia os processos em execução na Memória RAM. Arquiteturas sêniores abandonaram o uso de pesados "Agentes de Antivírus" tradicionais e passaram a usar a tecnologia **eBPF (Extended Berkeley Packet Filter)** diretamente no Kernel do [[OS_Linux|Linux]], capturando *Syscalls* (chamadas do sistema) no milissegundo em que ocorrem.
*   **O Problema que Resolve:** Mata a ameaça avançada da Pós-Exploração. Se o invasor pular a borda do site via [[Cyber_Ataque_SSRF]] e tentar usar o código de um contêiner que deveria apenas renderizar imagens para invocar um Shell Interativo (bash) e minerar Bitcoin, o CWPP lê o desvio de comportamento microscópico do processo e destrói o contêiner instantaneamente.
*   **Visão Sênior (Vulnerabilidades/Escala):** O "Performance Overhead" (Gargalo de CPU). Qualquer software que audita cada batimento cardíaco da CPU (Syscalls) drena a energia da máquina. CWPPs mal otimizados chegam a consumir 30% da CPU do servidor apenas para rodar a segurança, destruindo o [[Gov_SLA|SLA]] de latência da aplicação e enfurecendo as equipes de arquitetura de alta performance (HFT / Streaming).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Se o [[Cyber_CSPM]] é o Inspetor Predial que olha a fachada de fora, o [[Cyber_CWPP]] são os **Glóbulos Brancos (Sistema Imunológico) circulando dentro da corrente sanguínea do prédio**. Eles não se importam com a pintura externa. Eles estão fluindo pelas artérias (Kernel Linux). Se um vírus (Malware Fileless ou Injeção de Memória) tentar se disfarçar e invadir o fígado (Banco de Dados), os macrófagos do CWPP engolfam e devoram o processo alienígena no exato momento da anomalia celular, estancando a infecção no microscópio.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação do estado da arte do CWPP moderno utiliza a ferramenta open-source *Falco* (da Sysdig) operando via eBPF. Uma regra de contenção que grita no painel se alguém abrir um terminal de comando no meio de um servidor de produção puro:
```yaml
# Regra do Falco identificando Container Escape ou Terminal Ilegal
rule: Terminal shell in container
desc: A shell was used as the entrypoint/exec point of a container
condition: spawned_process and container and shell_procs
output: "Shell spawned in container (user=%user.name container_id=%container.id)"
priority: EMERGENCY
````

5. História do Conteúdo

A evolução foi forçada pela criação do [[Ferramenta_Docker|Docker]] e do Kubernetes. No mundo físico antigo, a empresa instalava um Antivírus pesado no Windows Server e ele ficava rodando. Nos clusters modernos, a "Máquina" (Contêiner) dura apenas 5 minutos de vida. Antivírus legados não conseguiam instalar e atualizar vacinas tão rápido. O CWPP foi criado para abstrair a proteção: a segurança não fica mais "instalada" no sistema, ela envelopa o orquestrador e injeta imunidade dinâmica, não importa quão rápida seja a criação e morte das células.