**1. Pilar de Defesa em Nuvem e Infraestrutura (Cloud Security)**

- **Cyber_CNAPP:** Plataforma unificada nativa de nuvem que extirpa o uso de silos de segurança, integrando a visibilidade preventiva de IaC, monitoramento de postura (CSPM) e defesa de runtime (CWPP) no mesmo console.
- **Cyber_CSPM:** Motor de auditoria contínua e automatizada que caça _Misconfigurations_ (o maior vetor de ataque da nuvem) comparando o ambiente de produção contra as regras rigorosas do CIS e PCI-DSS.
- **Cyber_CWPP:** O escudo de proteção em execução (runtime) que atua internamente nas cargas de trabalho vulneráveis, protegendo Máquinas Virtuais, orquestradores de contêineres e funções lambdas/serverless contra malware e movimentação lateral.
- **Cyber_CIEM:** A ferramenta de "Zero Trust de Identidade" na nuvem. Destrói o "Permission Creep" descobrindo identidades humanas ou de máquinas (APIs) que possuem privilégios abusivos herdados não utilizados.
- **Cyber_DSPM:** Gerenciamento cirúrgico da postura de dados focado em caçar onde residem as chaves, PIIs (dados confidenciais) e informações em texto claro esquecidos em buckets não criptografados da rede para blindá-los.
- **Cyber_KSPM:** Gestão de Postura focada exclusivamente na letal complexidade do Kubernetes, escaneando contêineres antes do deploy para garantir que não existam bibliotecas que facilitem o _Container Escape_.
- **Cyber_CDR:** (Cloud Detection and Response) O motor reativo guiado por IA que correlaciona logs do CloudTrail ou Azure Monitor para estancar ataques ativos, como sequestros de instância e exfiltrações.
- **Cyber_Cloud_Misconfiguration:** A vulnerabilidade máxima da modernidade. Desvios e falhas humanas grotescas onde um desenvolvedor abre as portas de rede globalmente (ex: 0.0.0.0/0) e não implementa criptografia no repouso do disco.
- **Cyber_Configuration_Drift:** O desvio silencioso entre a segurança teórica forjada no código de provisionamento (Terraform) e o caos real após a engenharia fazer gambiarras manuais não documentadas no console de produção.
- **Cyber_Ghost_Resources:** A expansão morta da superfície de ataque gerada pela manutenção desleixada de IPs flutuantes antigos, gateways desatrelados e servidores zumbis esquecidos pelo pipeline de limpeza do CI/CD.
- **Cyber_IMDSv1_vs_v2:** O Serviço de Metadados da Instância EC2. O modelo antigo (v1) usa requisições burras GET permitindo ataques mortais de extração. A adoção sênior exige imposição rígida da (v2), blindada com "Tokens de Sessão" (PUT) intransponíveis à distância.
- **DevSecOps_IaC_Scanning:** Análise Estática de "Infraestrutura como Código" bloqueando e comentando comitês no GitHub antes que o programador consiga submeter arquiteturas malfeitas e expostas ao ambiente.
- **Cyber_Network_ACL_Cloud:** A aplicação de regras burras de _Stateless Packet Filter_ em nível de Sub-rede nas instâncias de nuvem. Atua como barreira bruta que ignora contextos, mitigando tráfego antes que atinjam as _Security Groups_ stateful.
- **Cyber_Over_Privileged_IAM:** A herança tóxica de nuvens subgerenciadas onde o atacante compromete uma conta de serviço banal apenas para descobrir que o analista sênior concedeu-lhe a propriedade "FullAdmin" no sistema principal.
- **Cyber_Immutable_Infrastructure:** A filosofia arquitetural militar em TI onde você "não corrige" servidores doentes. Se uma máquina necessita um patch, você a assassina integralmente e invoca um servidor novo a partir do zero a partir do código validado no repositório.

**2. Pilar de DevSecOps e AppSec (Segurança de Aplicação)**

- **DevSecOps_SAST:** Teste da "Caixa-Branca" operado em pipelines focado em extrair falhas de segurança estruturais e padrões obsoletos de código enquanto o sistema sequer roda.
- **DevSecOps_DAST:** Teste cego da "Caixa-Preta" que simula as ferramentas de um invasor web bombardeando a aplicação com pacotes nocivos para medir como a borda da arquitetura responde à ameaça sob stress.
- **DevSecOps_IAST:** A genialidade da "Caixa-Cinza" que embutindo sensores nativos junto do DAST correlaciona requisições falhas no frontend com a linha de erro cirúrgica da linguagem backend.
- **DevSecOps_RASP:** Auto-imunidade ativa onde a aplicação tem um "antivírus de execução de fluxo" inserido nela em produção, bloqueando injeções maliciosas detectando as intenções anômalas e as strings formatadas na memória base.
- **DevSecOps_Secrets_Scanning:** O vigilante implacável de pipeline atuando contra o maior erro corporativo: a codificação em texto puro (_Hardcoded_) de chaves mestras e tokens em repositórios da nuvem pública.
- **Cyber_HashiCorp_Vault:** A infraestrutura de cofre sênior adotada pelo mundo como núcleo blindado e orquestrador criptográfico, que aniquila o gerenciamento ingênuo de credenciais.
- **Cyber_Dynamic_Secrets:** O estado da arte do cofre do Vault. A aniquilação permanente das senhas estáticas. O cofre cria a credencial do Banco de Dados no milissegundo do pedido e autodestrói o uso 5 minutos depois (TTL curtos), assassinando movimentações laterais duradouras.
- **Cyber_Transit_Secrets:** Arquitetura sênior onde programadores param de programar encriptação nos seus aplicativos. O código joga os CPFs no Vault, o Vault encripta nativamente as chaves sem nunca deixá-las sair e devolve o hash protegido que o código finaliza salvando no Banco de Dados.
- **Cyber_Secret_Zero_Paradox:** A problemática de "Galinha e o Ovo". Se um microsserviço precisa de um login altamente seguro do Vault para obter um segredo do Vault, onde ele armazena, em segurança, a senha necessária inicial de acesso ao cofre?
- **DevSecOps_Secure_Coding:** A disciplina que transfere a responsabilidade da proteção para o desenvolvedor ao impor a parametrização compulsória de variáveis impedindo as injeções da Família OWASP.
- **Cyber_SBOM:** A fatura de declaração de risco. Relatório explícito que desmembra todas as bibliotecas de código de terceiros utilizadas na composição do produto, crucial para mitigar ameaças como o ataque _Supply Chain_.
- **Cyber_Code_Injection:** A exploração severa do compilador interpretativo de um servidor executando cegamente _inputs_ da rua achando que são as próprias variáveis internas ou funções de avaliação (`eval()`).
- **Cyber_Mismatch_Context_XSS:** Quando o programador acerta ao higienizar a injeção JSON mas erra ao usar decodificadores mal modelados que quebram o Unicode diretamente na API final, invocando a ressurreição da carga XSS no _Dom Document_.
- **Cyber_Authentication_Coercion:** Enganar a vulnerabilidade da infraestrutura forçando serviços do próprio servidor (como MS-EFSRPC) a solicitar protocolos ou credenciais falsificadas entregando, de bandeja, as provas dos hashes à máquina do cibercriminoso.
- **Cyber_Vulnerability_Chaining:** O amadurecimento estratégico da arquitetura de explorações onde falhas triviais (consideradas de baixo risco sozinhas) são combinadas para abrir uma janela tática permitindo acesso ilimitado.

**3. Pilar de SOC, Caça a Ameaças e Defesa (Blue Team)**

- **Cyber_EDR:** Observabilidade letal local atuando como a "Caixa-Preta" do avião. Ele lê a injeção comportamental na memória e nos arquivos temporários sem focar em _hashes_ puros de vírus obsoletos.
- **Cyber_XDR:** Unificação total e expansão tática da malha do EDR puxando os vestígios dos firewalls, _gateways_ de e-mail e nuvem gerando visão unificada para matar o _Dwell Time_ dos ataques avançados.
- **Cyber_SOAR:** A orquestração das ferramentas e o fim do esgotamento humano do Blue Team ao executar manuais contendo automações (Playbooks) isolando roteadores assim que regras de violações comportamentais no SIEM despontarem.
- **Cyber_Threat_Hunting:** Paradigma militar de antecipação. Em vez do exército aguardar o disparo de alarmes reagindo pacificamente, analistas seniores partem do princípio ("Assuma a Violação") em que patrulham falhas ativamente à margem da rede usando grafos e dados.
- **Cyber_Regra_Sigma:** Criação de lógicas modulares descritas em formatações _agnósticas_. É o "Esperanto" tático da comunidade permitindo caçar malwares indiferente das estruturas proprietárias pagas do Splunk e Sentinel.
- **Cyber_Regra_YARA:** Assinaturas táticas flexíveis focadas no código puro do atacante para varrer memórias e arquivos ocultos do SO localizando pedaços microscópicos baseados em hexa.
- **Cyber_Honeypot:** Estratégia máxima de inteligência por Decepção. Uma máquina que brilha na rede de propósito emulando credenciais e falhas atraindo predadores de varredura ativa entregando alertas de altíssima certeza com zero ruído estático.
- **Cyber_Honeytoken:** Armadilhas lógicas implantadas de propósito nos repositórios GIT da engenharia ou no próprio cofre digital contendo chaves da "AWS Falsas". Sua existência gera pânico no criminoso, que tenta conectá-la entregando seu ID original no ato.
- **Cyber_Active_Directory_Canaries:** Elementos e identidades falsificadas do AD com monitoramento estrito em log 4662 desenhadas contra robôs enumerações furtivos; ler seus atributos detona um alarme vermelho imediato.
- **Cyber_Memory_Pattern_Analysis:** Defesa violenta em detecção que desmembra a integridade analítica processando a leitura em RAM versus as cópias legadas no disco rígido caçando as almas do _Hollowing_.
- **Cyber_API_Call_Monitoring:** Caça cirúrgica sobre como o Windows invoca memória. O registro e alerta em comandos perigosos das bibliotecas como `VirtualAllocEx()` ou `SetThreadContext()` avisam sobre as explorações silenciosas da rede.
- **Cyber_DEP_e_ASLR:** Os escudos basilares dos Sistemas Operacionais que estragam matematicamente as injecões ao proteger execução local aleatória em "Data Execution Prevention" e randomizar lógicas fundamentais nos endereços.
- **Cyber_PPL:** (Protected Process Light) Política defensiva mandatória em Windows modernos trancando acessos abertos as bibliotecas chaves que abrigam os processos operacionais sensíveis de dumping da credencial LSA.
- **Cyber_Windows_Credential_Guard:** Proteções ancoradas na arquitetura militar isolando ativamente a memória (Virtualização), para blindar tickets ou NTLM mesmo quando a superfície do Windows inteira está envenenada.
- **Cyber_Indicators_of_Compromise_IoC:** Artefatos reativos baseados em IP, Hash e registros descobertos em _post-mortem_ que servem meramente como "Placas de Procura-se", sendo facilmente burlados por mutação pelas _APTs_.

**4. Pilar Ofensivo - Aplicações e Sistema Operacional (Red Team)**

- **Cyber_Ataque_SSRF:** O "assassinato da borda perimetral". Você falsifica o endereço URL entregue em _webhooks_ ou imagens instruindo a máquina interna a pedir por você informações diretas dentro de roteadores ou serviços imunes da rede restrita (_Metadata IMDS_).
- **Cyber_Ataque_XXE:** Uma falha grotesca em compiladores da linguagem XML (Entities) em configurações brandas executando comandos letais que furtam chaves ocultas nos confins do sistema local (_Local File Inclusion - LFI_).
- **Cyber_Ataque_XSS_Reflected:** A exploração não persistente, mas imediata enviando a vítima _links_ engatilhando as execuções letais retornadas através de um código burro e inseguro manipulado no carregamento.
- **Cyber_Ataque_XSS_Stored:** Um ataque epidêmico de longa latência infectando nativamente e permanentemente o sistema do site, executando _JavaScripts_ que drenam cookies para todo o fluxo inocente e futuro dos novos perfis.
- **Cyber_Ataque_Billion_Laughs:** Expansão algorítmica fatal contida na família do XXE visando indisponibilizar serviços em DOS abusando intensamente e consumindo as alocações da CPU/RAM através das reações recursivas.
- **Cyber_Ataque_DLL_Hijacking:** Enganar as instâncias sistêmicas na hora em que rodam. As vulnerabilidades exploram processos confiáveis do SO localizando extensões _DLL_ que na verdade forjaram ordens maliciosas de carga prévia.
- **Cyber_Ataque_Unquoted_Service_Path:** Abuso puramente técnico explorando lacunas com falhas no _Path_ de espaço no _Windows Service_ plantando arquivos malignos forçando que escaladas para contas "SYSTEM" atropelem hierarquias.
- **Cyber_Process_Injection:** Infiltração microscópica sem destruir bibliotecas, fundindo as execuções e comportamentos furtivos mascarando táticas num programa perfeitamente benigno de alta autoridade na vigilância da empresa.
- **Cyber_Process_Hollowing:** A evolução sênior de injeções (T1055.012). Arranca e despovoa completamente a imagem do disco legítima no _Kernel_ de execução suspenso realocando os corpos de malwares nas almas originais vazias.
- **Cyber_Process_Herpaderping:** Um malabarismo absurdo das permissões temporárias das manipulações do formato em disco: executa a transação de "A" real como arquivo mas a mascara retroativamente e reverte após abrir os canais ilícitos.
- **Cyber_Process_Doppelganging:** Manipuladores obscuros e esquecidos dos _Logs Transacionais_ NTFS mascarando infecções invisíveis dentro dos espaços limpos criando o _sandbox_ isolado da proteção estática de detecção.
- **Cyber_APC_Injection:** Engajamento do malware baseado na mecânica "Asynchronous Procedure Call". Ele enfileira sub-repticiamente o código furtivo nos arquivos dormentes do computador e aguarda pacientemente o despertar de uso inato das rotinas da vítima.
- **Cyber_UAC_Bypass:** A traição tática contornando o _Prompt_ visual Administrativo abusando intencionalmente diretórios privilegiados de Auto-Elevação (AutoElevated) com injeção em bibliotecas de registro COM isoladas ou Variáveis (Windir).
- **Cyber_Phantom_DLL_Loading:** Uma variante do DLL Hijacking onde invasores alimentam os buracos dos defeitos (bugs de desenvolvedores de Windows) plantando DLL malfeitas exatas nos campos onde o compilador jura encontrar um elemento morto.
- **Cyber_Reflective_DLL_Injection:** Abuso complexo de exploração do nível da memória RAM ignorando explicitamente que registros sejam alocados em sistema ou disco duro; o próprio malware contêm mecanismos primitivos de autocompilação no SO.

**5. Pilar Ofensivo - Active Directory e Movimentação Lateral**

- **Cyber_Ataque_Kerberoasting:** Roubo indireto letal onde adversários extraem as _Tickets TGS_ de contas baseadas nos perfis associados (SPN). Extraído offline das visões da segurança o hash sofre fraturas criptográficas garantindo escalação de privilégio bruto.
- **Cyber_Ataque_Targeted_Kerberoasting:** Arquitetura predatória refinada forçando anomalias no sistema em que um atacante adultera e injeta perfis falsos nas contas vulneráveis das vítimas alteradas criando um vetor focado nas credenciais SPN recém plantadas.
- **Cyber_Ataque_AS_REP_Roasting:** A inépcia da segurança ignorando o _Kerberos Preauthentication_. Sem pedir verificação ou senhas as máquinas geram pacotes contendo o Hash da vítima diretamente enviada na rua no retorno _TGT_.
- **Cyber_Ataque_DCSync:** Assumir o poder administrativo (DS-Replication). Enganando os domínios via protocolos _DRS_ as ferramentas (Mimikatz) ordenam silenciosamente para que o Servidor replique o banco de senhas completo da arquitetura entregando todo o império.
- **Cyber_Ataque_Dump_NTDS_DIT:** O alvo central de desastre absoluto onde cópias do volume VSS Shadow sequestram as estruturas físicas completas que detém todas as credenciais base e configurações ativas e latentes da empresa operante.
- **Cyber_Ataque_Pass_The_Hash:** Roubo em que os atacantes não focam na decodificação do painel mas operam reutilizando o modelo de conversão do hash _NTLM_ coletado por rastros do _LSASS Memory_ transitando invisíveis entre redes segmentadas.
- **Cyber_Ataque_Pass_The_Ticket:** Usurpações onde apenas as autenticações atreladas as sessões duradouras criptográficas valem para infiltrar. Eles tomam identidades lícitas do Active Directory e rodam nos tickets até eles aspirarem o oxigênio restante.
- **Cyber_Ataque_Golden_Ticket:** Forjar o Ticket supremo de "Administrador Universal". Ao destruir o core `KRBTGT` os hackers abdicam as portas do AD em permissões ativas forjadas gerando acesso não identificáveis que se mantêm no controle global.
- **Cyber_Ataque_Silver_Ticket:** Estratégia microscópica furtiva enganadora que roubando senhas restritas de arquivos locais dos dispositivos paralelos gerando _Tickets TGS_ puramente ignorando contatar ou passar auditorias dos Domínios Centrais.
- **Cyber_Ataque_Golden_SAML:** Arquitetura do apocalipse da ponte das empresas em nuvem forjando as transações privadas assinando os _Tokens SAML_ no AD FS, criando logons invisíveis universais burlados da obrigação técnica da Multi-Fatores.
- **Cyber_Ataque_Entra_Connect_Compromise:** O ataque aos portões das malhas. Atacando conexões "Sync e Msol" que vinculam arquiteturas de solo com nuvens Azure para espalhar domínios cruzados das infraestruturas base e reescrever PTA autenticações e Passwords localizados.
- **Cyber_Ataque_ADCS_ESC1:** Concessão malfeita da infraestrutura de CA. Por conta do controle ridículo, contas de convidados pedem as chaves operando na máscara exigida da segurança afirmando ser "O Diretor", e o controlador engessa a resposta concedendo acesso em certificado.
- **Cyber_Ataque_ADCS_ESC4:** Veneno inserido via alteração _ACL_. O invasor enxerga os privilégios falhos no protocolo das configurações corrompidas reescrevendo ele maliciosamente abrindo buracos vulneráveis onde as máscaras subsequentes (ESC1) entram fáceis para gerar os passes mestres.
- **Cyber_Ataque_One_Way_Trust_Bypass:** Violações exploradas nas hierarquias entre Redes Confidenciais e Expostas ("Trusting"). Rompendo senhas _TDO_ em que não deviam existir acesso eles personificam cruzando lateralmente o ambiente ignorando protocolos isolantes de barreiras originais.
- **Cyber_Ataque_SID_History:** Tática mestre dissimuladora de injetar nas heranças em registros passados identidades (grupos _Admins_) que garantem atuações restritas. Eles habitam contornando a listagem visível do usuário agindo sobre rastros obscuros do histórico migratório de servidores Active.
- **Cyber_Ataque_Skeleton_Key:** Mutação letal algorítmica sobre a validação LSA. Adiciona chaves invisíveis aos controladores mestre mantendo os logons e validadores limpos operacionais mas simultaneamente deixando os acessos mestres na porta destrancados até as _RAMs_ esfriarem e apagarem de imediato.
  
  ----
  existente:
  
  Ofensiva: Ataques, Ameaças e Malwares (Red Team)

- **Cyber_Ameaca****:** Causa ativa e potencial de um incidente cibernético agindo sobre vulnerabilidades.
- **Cyber_Ataque_BEAST****:** Ataque criptoanalítico focado em quebrar o modo de encadeamento CBC no TLS 1.0/SSL 3.0.
- **Cyber_Ataque_DDoS****:** Inundação de recursos para causar interrupção total de um serviço (Negação de Serviço).
- **Cyber_Ataque_DDoS_SYN_Flood****:** Variação de DDoS que esgota a memória RAM travando o servidor com falsos inícios de conexão TCP.
- **Cyber_Ataque_HNDL****:** _Harvest Now, Decrypt Later_. Roubo de dados encriptados hoje para quebra quântica no futuro.
- **Cyber_Ataque_POODLE****:** Vulnerabilidade fatal de rebaixamento (downgrade) que força o alvo a usar o obsoleto SSL 3.0.
- **Cyber_Ataque_SQL_Injection****:** Inserção de comandos maliciosos no banco de dados através de falhas de sanitização web.
- **Cyber_Ataque_Supply_Chain****:** Contaminação da cadeia de suprimentos através de bibliotecas open-source e softwares de fornecedores.
- **Cyber_Ataque_TCP_RST****:** Interrupção forçada de comunicações usando a flag de "Reset" falsificada.
- **Cyber_Ataque_XSS****:** Injeção de código JavaScript malicioso executado no navegador da vítima.
- **Cyber_Deepfake****:** Mídia sintética (vídeo/áudio) forjada por IA para fraudar identidades.
- **Cyber_Eavesdropping****:** Escuta passiva e invisível de redes não criptografadas.
- **Cyber_Engenharia_Social****:** Manipulação de vieses psicológicos para forçar falhas humanas de segurança.
- **Cyber_Engenharia_Social_Hoax****:** Boatos sem vírus que operam como ataques de "negação de serviço humano" por pânico.
- **Cyber_Engenharia_Social_Spam****:** Envio massivo e cego de ameaças por e-mail/SMS.
- **Cyber_Malware_Backdoor****:** Instalação de porta dos fundos invisível para garantir acesso persistente ao invasor.
- **Cyber_Malware_Keylogger****:** Software ou hardware clandestino que grava e envia tudo que é digitado.
- **Cyber_Malware_Ransomware****:** Sequestro digital que paralisa dados com criptografia militar exigindo resgate.
- **Cyber_Malware_Rootkit****:** Malwares que operam no nível de Kernel para ocultar sua presença do antivírus.
- **Cyber_Malware_Spyware****:** Espiões focados em roubo de credenciais e navegação sem destruir a máquina.
- **Cyber_Malware_Trojan****:** Cavalo de Troia; pacote que o usuário instala achando ser legítimo.
- **Cyber_Malware_Virus****:** Parasita que necessita estar anexado a arquivos e exige o clique humano para funcionar.
- **Cyber_Malware_Worm****:** Verme autossuficiente que destrói redes propagando-se automaticamente.
- **Cyber_Man_In_The_Middle****:** Interceptação e manipulação ativa do tráfego posicionando-se entre duas partes.
- **Cyber_OSINT****:** Inteligência de Fontes Abertas; o reconhecimento cego que não toca a infraestrutura da vítima.
- **Cyber_Phishing****:** Comunicações fraudulentas forjadas que clonam a autoridade de entidades legítimas.
- **Cyber_Smishing****:** Variação de Phishing via SMS direto no celular pessoal do usuário.
- **Cyber_Spoofing****:** Falsificação matemática de endereços (IP/MAC) para burlar permissões baseadas em origem.
- **Cyber_Vishing****:** Sequestro cognitivo via telefone ou VoIP, clonando a voz de superiores e suporte técnico.
- **Cyber_Vulnerabilidade****:** Brecha passiva ou falha de código esperando ser explorada.

2. Defesa, Infraestrutura e Governança (Blue Team)

- **Cyber_Cloud_Security****:** Arquitetura do Modelo de Responsabilidade Compartilhada na proteção de instâncias AWS/Azure.
- **Cyber_DLP****:** Prevenção algorítmica de vazamento interno e exfiltração de dados sensíveis (Data Loss Prevention).
- **Cyber_Firewall_NGFW****:** A evolução do firewall que realiza Inspeção Profunda de Pacotes e quebra criptografia.
- **Cyber_Firewall_PacketFilter****:** O firewall rudimentar, cego e sem memória (Stateless).
- **Cyber_Firewall_Proxy****:** Ocultação do cliente forçando a refação da requisição por um intermediário.
- **Cyber_Firewall_Stateful****:** O firewall que acompanha o "estado" das comunicações na memória RAM.
- **Cyber_Firewall_WAF****:** Guarda-costas puro de Camada 7 (Web) para bloquear injeções SQL e XSS.
- **Cyber_Framework_CIS_Controls****:** Conjunto tático de 18 práticas de sobrevivência cibernética sem burocracia.
- **Cyber_Framework_MITRE_ATTACK****:** A enciclopédia mundial do comportamento ofensivo e das Táticas, Técnicas e Procedimentos (TTP).
- **Cyber_IAM****:** Gestão centralizada do ciclo de vida, autenticação e autorização de Identidades.
- **Cyber_IDS****:** Sistema investigativo e gerador de alarmes de rede (Passivo).
- **Cyber_IPS****:** Sistema armado de contenção em tempo real na rede (Ativo).
- **Cyber_Incident_Response****:** A engenharia metodológica forense para salvar a empresa do desastre (Modelo PICERL).
- **Cyber_ISO_27001****:** A norma jurídica e macro de processos para certificação em gestão de segurança.
- **Cyber_ISO_27002****:** A tradução técnica da 27001 com 93 controles recomendados de blindagem de rede.
- **Cyber_IoT_Security****:** A disciplina letal de defesa para dispositivos conectados de baixo poder computacional.
- **Cyber_MFA****:** Autenticação Multifator exigindo hardware físico ou token.
- **Cyber_Monitoramento_Continuo****:** O uso implacável de SIEM e UEBA para centralizar e caçar anomalias nos logs globais.
- **Cyber_PCI_DSS****:** Norma global obrigatória do setor de cartões de crédito.
- **Cyber_Pentest****:** Simulação de ameaça em que atacantes profissionais validam as defesas em ambiente controlado.
- **Cyber_Risco****:** O cruzamento matemático entre probabilidade da ameaça e impacto financeiro.
- **Cyber_RPO****:** Objetivo de Ponto de Recuperação (De quanto em quanto tempo o backup ocorre).
- **Cyber_RTO****:** Objetivo de Tempo de Recuperação (Quantas horas o negócio sobrevive inoperante).
- **Cyber_SASE****:** O roteamento SD-WAN unificado em arquitetura Zero Trust nativa na nuvem.
- **Cyber_SDA_SGT****:** Microsegmentação onde a Tag (Identity) viaja no pacote, destruindo a dependência de IPs dinâmicos.
- **Cyber_UAC****:** O controle nativo do Windows que exige confirmação explícita de elevação administrativa.
- **Cyber_VPN_Mecanica****:** A fundação do túnel cifrado tradicional de redes remotas.
- **Cyber_Zero_Trust****:** O paradigma absoluto onde a rede interna não existe; o bloqueio padrão com autenticação a cada requisição.

3. Matemática, Criptografia e Ferramentas (Core e Tática)

- **Cyber_AES_256****:** Algoritmo militar de criptografia simétrica. O cadeado inquebrável para dados em repouso.
- **Cyber_Criptografia_Assimetrica****:** A genialidade dos pares de chaves Públicas/Privadas para negociação sobre a internet aberta.
- **Cyber_GANs****:** As redes neurais de IA aplicadas a armas de desinformação (Geração Adversarial).
- **Cyber_Hashing****:** O moedor de dados matemático e irreversível que garante integridade absoluta de transações e senhas.
- **Cyber_WireGuard****:** A revolução de VPN em nível de Kernel Linux desbancando o obsoleto OpenVPN/IPsec.
- **Ferramenta_OWASP_ZAP****:** O scanner ativo focado na penetração da Camada 7.
- **Ferramenta_Wireshark** **(e seus sub-módulos):** O faro investigativo de tráfego, fragmentado perfeitamente nas notas de Endpoints, Flow Graph, IO Graphs, Packet Lengths e Protocol Hierarchy.