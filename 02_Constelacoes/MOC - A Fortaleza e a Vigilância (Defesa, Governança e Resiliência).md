---
tags:
  - tipo/moc
  - contexto/dev/cyber
  - status/4_evergreen
  - afinidade/alta
---

### MOC: A Fortaleza e a Vigilância (Defesa, Governança e Resiliência)

#### 1. O Vetor (Objetivo deste Mapa)
**Porquê esta junção?** Este mapa consolida a ótica do *Blue Team* (Defesa) e da Diretoria Executiva. Ele organiza as ferramentas, protocolos e filosofias usadas para erguer perímetros, auditar tráfego, garantir a confidencialidade matemática e, principalmente, provar juridicamente que a empresa sobrevive ao desastre.

#### 2. A Narrativa de Conexão (A Sinapse)
A defesa de uma infraestrutura começa com a negação do acesso. O limite do castelo é demarcado pelo [[Rede_Firewall]]. Nos primórdios, usávamos o básico [[Cyber_Firewall_PacketFilter]], que evoluiu para o inteligente [[Cyber_Firewall_Stateful]], capaz de lembrar quem iniciou a conversa. Para observar os invasores que escalam esse muro, instalamos o [[Cyber_IDS]] (um alarme passivo), mas para atirar neles em tempo real, precisamos do [[Cyber_IPS]] (a contenção ativa). Se o usuário legítimo estiver fora do castelo, ele entra por um túnel blindado: a [[Rede_VPN]], hoje modernizada por protocolos hiper-rápidos como o [[Cyber_WireGuard]].

Contudo, muros não protegem contra mensageiros espiões. É aqui que entra a matemática. Os dados em trânsito são envelopados pela [[Rede_TLS]] (substituta do falecido [[Rede_SSL]]) e selados com cifras inquebráveis como o [[Cyber_AES_256]]. Mas a criptografia protege o *dado*, não a *pessoa*. O novo perímetro deixou de ser a rede e passou a ser a Identidade: usamos o [[Cyber_IAM]] para ditar quem pode ver o quê, aplicamos o [[Cyber_MFA]] para matar o phishing e o [[Cyber_UAC_User_Account_Control]] para conter privilégios locais. Para impedir que o funcionário corrompido vaze os diamantes da empresa, impomos o [[Cyber_DLP]].

A evolução final dessa paranoia é o modelo [[Cyber_Zero_Trust]], que assume que o castelo já caiu e exige crachá a cada novo corredor, aliado à descentralização de borda em nuvem via [[Cyber_SASE]] e às práticas rigorosas da [[Cyber_Cloud_Security]]. E como gerenciar os dispositivos que estão nas casas dos funcionários? Usamos o [[Ferramenta_Microsoft_Intune]].

Mas a segurança não é baseada em fé; ela exige provas. O auditor testa as barricadas executando um [[Cyber_Pentest]] implacável. Ele procura portas abertas com o [[Rede_Nmap]] e injeta corrupção em aplicações web usando o [[Ferramenta_OWASP_ZAP]]. Quando a rede sangra, o analista forense abre o [[Ferramenta_Wireshark]]. Ele não lê o caos puro; ele usa o [[Ferramenta_Wireshark_Protocol_Hierarchy]] para ver o escopo, isola o IP culpado no [[Ferramenta_Wireshark_Endpoints]], acha vazamentos massivos pelo [[Ferramenta_Wireshark_Packet_Lengths]], vê o colapso físico nos [[Ferramenta_Wireshark_IO_Graphs]] e entende a briga desenhando um [[Ferramenta_Wireshark_Flow_Graph]]. O SOC automatiza isso tudo em tempo real através do [[Cyber_Monitoramento_Continuo]].

Por fim, não se defende no improviso. O arquiteto sênior segue a bíblia administrativa da [[Cyber_ISO_27001]] e aperta os parafusos recomendados pela [[Cyber_ISO_27002]] e pelos táticos [[Cyber_Framework_CIS_Controls]]. Ele estuda os movimentos do inimigo usando o [[Cyber_Framework_MITRE_ATTACK]]. E quando tudo falhar — porque a matemática garante que um dia falhará —, a sobrevivência da empresa será ditada exclusivamente pelos Backups sincronizados via [[Ferramenta_Rsync]] e pelo respeito milimétrico ao tempo de parada ([[Cyber_RTO]]) e à tolerância de perda de dados ([[Cyber_RPO]]).

#### 3. O Índice Técnico (Acesso Rápido)

**I. O Perímetro e o Controle de Fluxo**
* [[Rede_Firewall]] (A muralha base)
* [[Cyber_Firewall_PacketFilter]] (A catraca burra)
* [[Cyber_Firewall_Stateful]] (O guarda com memória)
* [[Cyber_IDS]] (O sensor de movimento)
* [[Cyber_IPS]] (A metralhadora automatizada)
* [[Rede_VPN]] & [[Cyber_WireGuard]] (Os túneis corporativos)

**II. Identidade, Confidencialidade e Criptografia**
* [[Rede_TLS]] & [[Rede_SSL]] (O túnel matemático)
* [[Cyber_AES_256]] (O cofre de nível militar)
* [[Cyber_IAM]] (A gestão de quem entra)
* [[Cyber_MFA]] (A regra das duas chaves)
* [[Cyber_UAC]] (A limitação de privilégios Windows)
* [[Cyber_DLP]] (O detector de metais na saída)

**III. Inspeção, Teste e Forense (As Ferramentas)**
* [[Cyber_Pentest]] (A invasão autorizada)
* [[Rede_Nmap]] (O mapeamento tático de portas)
* [[Ferramenta_OWASP_ZAP]] (O proxy de injeção Web)
* [[Ferramenta_Wireshark]] (O microscópio da rede)
    * [[Ferramenta_Wireshark_Protocol_Hierarchy]] (A visão macro)
    * [[Ferramenta_Wireshark_Endpoints]] (O rastreio do IP)
    * [[Ferramenta_Wireshark_Packet_Lengths]] (A anomalia de tamanho)
    * [[Ferramenta_Wireshark_IO_Graphs]] (O eletrocardiograma)
    * [[Ferramenta_Wireshark_Flow_Graph]] (O mapa de setas TCP)

**IV. Governança, Nuvem e Paranoia**
* [[Cyber_ISO_27001]] (A burocracia que salva a diretoria)
* [[Cyber_ISO_27002]] (O menu de controles práticos)
* [[Cyber_Framework_CIS_Controls]] (A lista de sobrevivência brutal)
* [[Cyber_Framework_MITRE_ATTACK]] (O playbook do inimigo)
* [[Cyber_Zero_Trust]] (O fim da confiança local)
* [[Cyber_SASE]] (A proteção empurrada para a borda)
* [[Cyber_Cloud_Security]] (A defesa do computador alheio)
* [[Ferramenta_Microsoft_Intune]] (A marionete corporativa remota)
* [[Cyber_Monitoramento_Continuo]] (O panóptico via SIEM)

**V. Sobrevivência e Continuidade (Disaster Recovery)**
* [[Ferramenta_Rsync]] (O algoritmo de cópia cirúrgica)
* [[Cyber_RTO]] (O oxigênio: quanto tempo até voltar)
* [[Cyber_RPO]] (O checkpoint: quanto dado posso perder)

#### 4. Pontas Soltas (O que falta mapear?)
* [ ] Diferenciar as operações táticas de Blue Team, Red Team e Purple Team.
* [ ] Mapear as ferramentas de orquestração de resposta (SOAR vs SIEM).
* [ ] Entender a fundo a arquitetura de Honeypots e Deception Technology (armadilhas).
* [ ] Estudar a assinatura criptográfica e PKI (Public Key Infrastructure).

#### 5. O Paralelo Absurdo (Interdisciplinaridade)
A Defesa Cibernética de um Data Center é idêntica à **Logística de Segurança de um Museu do Louvre**. 
O **Firewall** é a parede de vidro do museu. A **VPN** é a entrada exclusiva subterrânea para os curadores da arte. O **IAM e o MFA** garantem que quem abriu a porta não foi um visitante com uma cópia da chave, mas sim o Diretor usando sua digital e crachá. O **Wireshark** é a sala de vigilância com 50 telas monitorando se alguém correu onde deveria andar. A **ISO 27001** é a apólice de seguro contra incêndios e o **RTO/RPO** ditam quantos quadros os bombeiros precisam salvar em até 5 minutos se o museu pegar fogo, sob pena de falência.
```