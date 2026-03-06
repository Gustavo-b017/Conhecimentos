---
tags:
  - afinidade/alta
  - status/4_evergreen
  - tipo/conceito
  - contexto/dev/infra
---

### Cyber_Immutable_Infrastructure

#### 1. O Axioma (A Definição Rígida)
**O que é:** Infraestrutura Imutável é o paradigma operacional restritivo onde os servidores e instâncias de produção, uma vez implantados, nunca são atualizados ou modificados *in-loco*; se houver a necessidade de aplicar um patch ou alterar uma regra, o servidor atual é executado (destruído) e um novo servidor integralmente configurado é provisionado do zero para substituí-lo.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Abandona conexões via [[Rede_SSH|SSH]]. O código da infraestrutura é escrito declarativamente em ferramentas como *Terraform* ou compactado num manifesto *Docker*. Esse "molde" passa por varreduras defensivas ([[DevSecOps_IaC_Scanning]]). Se aprovado, a nuvem despeja a imagem na produção. Para atualizar o Linux da v1.0 para v1.1, você mata a v1.0 e sobe a nova forma de silicone.
*   **O Problema que Resolve:** O inferno do *Configuration Drift* (Desvio de Configuração) e os *Snowflake Servers*. Servidores "Flocos de Neve" são aqueles nos quais, durante 5 anos, analistas diferentes entraram de madrugada para digitar pequenos comandos paliativos não documentados. Se esse servidor morrer, a empresa nunca conseguirá refazê-lo. A imutabilidade garante que 100% da verdade da produção esteja escrita matematicamente em código versionado (Git).
*   **Visão Sênior (Vulnerabilidades/Escala):** O pesadelo da *Gestão de Estado*. Servidores só podem ser imutáveis e efêmeros se forem *[[Rede_Stateless|Stateless]]* (sem memória residente). Você não pode aplicar infraestrutura imutável num servidor de Banco de Dados sem um profundo desacoplamento do disco lógico (Volume persistente) da capacidade de computação (CPU/RAM). Matar a máquina exige que o dado financeiro do cliente esteja salvo em um "balde de armazenamento" físico que sobrevive à morte da VM.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O modelo antigo de servidores era criar **Animais de Estimação (Pets)**. Você dá um nome para o servidor (SRV-Mestre-Alpha), cuida dele, se ele ficar doente (Vírus/Desatualização) você leva ao veterinário (Faz login SSH e roda atualizações manuais), e se ele morre, você chora (A empresa para). O modelo de [[Cyber_Immutable_Infrastructure]] trata os servidores como **Gado de Abate (Cattle)** num sistema industrializado. Eles não têm nomes, têm códigos de barras (Container-ID). Se a Vaca_347 ficar doente, você não gasta dinheiro em remédio e tempo diagnosticando: você atira na Vaca_347 com uma marreta pneumática, aciona a impressora 3D e gera a Vaca_348 fisicamente idêntica em 2 segundos. Frio, sem emoção e inabalável.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O conceito imutável executado nativamente pelo Orquestrador do Kubernetes (K8s). Em vez de entrar no container e baixar a versão nova do Nginx, você altera o manifesto no bloco de código (IaC) e diz à esteira: destrua o velho, crie o novo:
```yaml
# A alteração da imagem atesta a imutabilidade; o node antigo será vaporizado.
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
      - name: meu-app-blindado
        image: nginx:1.21.0 # Mudei para 1.22.0. Destrua o atual e suba este.
````

5. História do Conteúdo

Conceituada em 2013 por Chad Fowler, a premissa encontrou fertilidade massiva com o estouro global do mercado de Cloud e a popularização brutal do Docker. Administradores exaustos da guerra contra malwares persistentes perceberam que, em vez de comprar antivírus reativos e complexos para tentar desinfetar um servidor, era computacionalmente mais viável e seguro "reiniciar o mundo a partir de um estado limpo e perfeito" diariamente (ou a cada submissão de código), extinguindo o oxigênio para qualquer atacante que tentasse se fixar ali (Pós-Exploração).