---
tags:
  - tipo/conceito
  - contexto/dev/arquitetura
  - afinidade/media
  - status/3_incubadora
---
### Arquitetura_Ponto_a_Ponto

#### 1. O Axioma (A Definição Rígida)
**O que é:** A integração Ponto a Ponto é o modelo de acoplamento direto primitivo (década de 90) onde sistemas distintos se comunicam sem nenhum middleware central, operando através de "scripts ad hoc" para transferir arquivos físicos ou injetar dados diretamente no banco alheio.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O Sistema A gera um arquivo (ex: EDI, CSV ou TXT) e transfere via rede (usualmente [[Rede_FTP]] ou SFTP) em rotinas agendadas de madrugada para o Sistema B, ou recebe acesso direto de escrita na tabela de banco de dados do parceiro [1].
- **O Problema que Resolve:** Na era anterior aos protocolos de web service modernos, era a única maneira viável e rápida de fazer dois computadores heterogêneos (ex: Mainframe IBM e um Servidor Unix) trocarem informações comerciais.
- **Visão Sênior (Vulnerabilidades/Escala):** Em um ecossistema com dezenas de aplicações, gera a inescalável "Arquitetura Espaguete". A resiliência é nula. Se a aplicação destino mudar o nome de uma coluna no banco de dados ou a ordem do CSV, a integração quebra silenciosamente, destruindo a consistência dos dados empresariais.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A integração Ponto a Ponto é como **puxar encanamentos clandestinos diretamente da caixa d'água do seu vizinho** em vez de usar o sistema central da prefeitura. Funciona rápido e é barato no curto prazo. Porém, se a rua tiver 50 vizinhos cruzando canos uns com os outros, vira uma teia incompreensível. Se um cano estourar na calçada, ninguém sabe de quem é a água que está vazando, e consertar exige quebrar o asfalto do bairro inteiro.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A implementação do horror do legado. Um script de integração ponto a ponto em *Bash* que extrai do banco local e despacha o arquivo diretamente para o IP do sistema de faturamento via FTP:
```bash
#!/bin/bash
# Anti-padrão total: Acoplamento e ausência de observabilidade
mysql -e "SELECT * FROM produtos INTO OUTFILE '/tmp/produtos.csv'"
ftp -inv 192.168.1.50 <<EOF
user admin_rh senha_super_secreta
cd /dados/faturamento
put /tmp/produtos.csv
bye
EOF
````

5. História do Conteúdo

Antes do boom da Internet e da padronização do [[DB_XML|XML]]/[[Front_JSON|JSON]], os sistemas corporativos operavam como feudos isolados e surdos. A única "língua universal" possível na década de 1980 e início dos anos 90 era o texto plano separado por vírgulas. A dor extrema de gerenciar a quebra constante dessas integrações noturnas forçou o mercado a inventar, anos depois, os middlewares e o modelo [[Arquitetura_SOA|SOA]].