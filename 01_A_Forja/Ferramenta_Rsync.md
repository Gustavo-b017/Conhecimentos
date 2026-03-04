---
tags:
  - tipo/ferramenta
  - contexto/dev/infra
  - afinidade/alta
  - status/3_incubadora
---

### Ferramenta_Rsync

#### 1. O Axioma (A Definição Rígida)
**O que é:** O `rsync` (Remote Sync) é um utilitário de linha de comando para sistemas baseados em Unix, rápido e extraordinariamente versátil, utilizado para a cópia e sincronização de arquivos e diretórios locais ou remotos.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente de comandos de cópia burros (como `cp`), o `rsync` utiliza um algoritmo de transferência delta. Ele inspeciona a origem e o destino e transfere apenas os blocos de dados que foram modificados, em vez de reescrever o arquivo inteiro. 
* **O Problema que Resolve:** No gerenciamento de cópias de segurança (Backups), copiar 1 Terabyte de dados todo dia pela rede exauriria a banda e o tempo. O `rsync` resolve isso sincronizando apenas as alterações diárias em segundos.
*   **Visão Sênior (Vulnerabilidades/Escala):** O `rsync` é um executor cego. Se a máquina principal sofrer um ataque de [[Cyber_Malware_Ransomware]] e os arquivos forem criptografados, o `rsync` verá isso como "arquivos modificados" e imediatamente sincronizará os arquivos destruídos por cima do seu backup limpo, arruinando sua redundância se você não possuir versionamento ou *snapshots* isolados.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
O `rsync` atua como um **Editor de Livros Paranóico**. Se o autor alterar apenas uma vírgula na página 45 de um livro de 1.000 páginas, o comando tradicional imprimiria as 1.000 páginas novamente e jogaria a cópia velha no lixo. O `rsync` olha as 1.000 páginas, diz "só a 45 mudou", recorta o pedaço exato da página 45 com um estilete, cola na cópia de backup e encerra o trabalho.

#### 4. Pragmatismo Aplicado (Código e Implementação)
O comando do laboratório exato demonstrado na infraestrutura da FIAP para espelhar diretórios, mantendo os atributos originais dos arquivos (a *flag* `-a` para *archive* e `-v` para *verbose*, mostrando o que está acontecendo):
```bash
# Sincroniza o conteúdo exato da pasta origem para a pasta destino
rsync -av /home/seu_usuario/origem/ /home/seu_usuario/destino/
```

#### 5. História do Conteúdo

Desenvolvido em 1996 por Andrew Tridgell e Paul Mackerras, o `rsync` tornou-se a espinha dorsal de quase todos os sistemas de espelhamento e backup em nuvem do planeta. Qualquer ferramenta moderna de backup incremental no Linux roda silenciosamente o motor matemático do `rsync` por trás de sua interface gráfica.