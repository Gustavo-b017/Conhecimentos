---
tags:
  - tipo/moc
  - contexto/dev/cyber/ataque
  - status/4_evergreen
  - afinidade/alta
---

### MOC: A Anatomia do Ataque (Ameaças, Vetores e Destruição)

#### 1. O Vetor (Objetivo deste Mapa)
**Porquê esta junção?** Este mapa organiza exclusivamente a engenharia da destruição e da espionagem. Ele consolida as táticas, ferramentas e comportamentos utilizados por adversários para explorar o elo humano e as falhas matemáticas de uma infraestrutura.

#### 2. A Narrativa de Conexão (A Sinapse)
Nenhum ataque cibernético sênior começa com ferramentas barulhentas. Antes de tocar no alvo, o adversário estuda o [[Cyber_Risco]] e mapeia a [[Cyber_Vulnerabilidade]] utilizando técnicas passivas de inteligência, como o [[Cyber_OSINT]]. A [[Cyber_Ameaca]] não tenta arrombar a porta da frente; ela busca a janela destrancada.

Com a planta do castelo em mãos, o invasor percebe que quebrar a criptografia do banco de dados é custoso. Em vez de atacar o código, ele ataca a psicologia humana usando a [[Cyber_Engenharia_Social]]. Ele pode disparar campanhas massivas de lixo não solicitado via [[Cyber_Engenharia_Social_Spam]] ou espalhar pânico falso com um [[Cyber_Engenharia_Social_Hoax]]. Porém, a lâmina letal e direcionada é o [[Cyber_Phishing]] (por e-mail), que evolui para a intimidade do SMS com o [[Cyber_Smishing]] ou para a extorsão telefônica vocal via [[Cyber_Vishing]]. Hoje, o vishing tornou-se indistinguível da realidade através da clonagem de voz gerada por IA com [[Cyber_Deepfake]], frequentemente treinada por algoritmos de [[Cyber_GANs]].

Se o usuário morder a isca, a entrega (Delivery) é feita. A carga primária geralmente é um [[Cyber_Malware_Trojan]], que finge ser algo útil, mas abre a porta do castelo por dentro. Uma vez no sistema, se a intenção for o caos logístico, solta-se um [[Cyber_Malware_Worm]], que se multiplica sozinho pelos dutos de ar-condicionado da rede. Se a intenção for a monetização brutal, o invasor implanta o [[Cyber_Malware_Ransomware]], trancando toda a empresa num cofre criptográfico. Mas, se o objetivo for a espionagem estatal, o silêncio é a regra: o invasor instala um [[Cyber_Malware_Rootkit]] para cegar o antivírus, permitindo que um [[Cyber_Malware_Spyware]] e um [[Cyber_Malware_Keylogger]] roubem senhas secretamente por meses.

Mas e se o elo humano não falhar? Então o ataque foca na infraestrutura de rede. O atacante pode espelhar a porta de um roteador para ler o tráfego em texto claro através do [[Cyber_Eavesdropping]]. Pode envenenar tabelas locais com [[Cyber_Spoofing]] e interceptar conversas ativas via [[Cyber_Man_In_The_Middle]]. Se ele quiser apenas destruir a disponibilidade, ele inunda a memória do servidor forjando as leis do TCP com um [[Cyber_Ataque_DDoS_SYN_Flood]], coordena uma botnet global ([[Cyber_Ataque_DDoS]]) através de geladeiras e câmeras mal configuradas ([[Cyber_IoT_Security]]), ou simplesmente encerra conexões alheias ejetando um [[Cyber_Ataque_TCP_RST]].

No nível da aplicação (Camada 7), a parede é burlada de outras formas. Formulários mal sanitizados sofrem [[Cyber_Ataque_SQL_Injection]] para extrair o banco, ou [[Cyber_Ataque_XSS]] para roubar sessões de outros clientes. Se a conexão for blindada por criptografia, o atacante rebaixa as defesas usando o [[Cyber_Ataque_POODLE]] ou o [[Cyber_Ataque_BEAST]]. Se ele não conseguir invadir a sua empresa de jeito nenhum, ele invade a empresa pequena que fabrica o software que você usa, aniquilando a sua segurança através de um [[Cyber_Ataque_Supply_Chain]]. E para aquilo que é matematicamente inquebrável hoje, ele rouba e guarda, usando a tática do [[Cyber_Ataque_HNDL]] apostando na obsolescência do futuro.

#### 3. O Índice Técnico (Acesso Rápido)

**I. A Fundação do Dano**
* [[Cyber_Ameaca]] (A causa)
* [[Cyber_Vulnerabilidade]] (A fraqueza)
* [[Cyber_Risco]] (O impacto percentual)
* [[Cyber_OSINT]] (O reconhecimento silencioso)

**II. O Vetor Humano (Engenharia Social)**
* [[Cyber_Engenharia_Social]] (A raiz da manipulação)
* [[Cyber_Phishing]] (A isca visual/e-mail)
* [[Cyber_Smishing]] (O ataque na mão/SMS)
* [[Cyber_Vishing]] (A pressão no ouvido/Voz)
* [[Cyber_Deepfake]] & [[Cyber_GANs]] (A automação da mentira)
* [[Cyber_Engenharia_Social_Hoax]] (O boato destrutivo)
* [[Cyber_Engenharia_Social_Spam]] (O vetor estatístico)

**III. O Arsenal de Software (Malwares)**
* [[Cyber_Malware_Trojan]] (O cavalo de infiltração)
* [[Cyber_Malware_Virus]] (O parasita dependente)
* [[Cyber_Malware_Worm]] (O viajante autônomo)
* [[Cyber_Malware_Ransomware]] (A extorsão financeira)
* [[Cyber_Malware_Rootkit]] (O manto da invisibilidade)
* [[Cyber_Malware_Spyware]] (A vigilância contínua)
* [[Cyber_Malware_Keylogger]] (O grampo no teclado)

**IV. Sabotagem de Infraestrutura e Rede**
* [[Cyber_Ataque_DDoS]] (A inundação bruta)
* [[Cyber_Ataque_DDoS_SYN_Flood]] (A exaustão de memória TCP)
* [[Cyber_Ataque_TCP_RST]] (O divórcio forçado)
* [[Cyber_Spoofing]] (O roubo de identidade de máquina)
* [[Cyber_Eavesdropping]] (A escuta da fibra)
* [[Cyber_Man_In_The_Middle]] (A interceptação ativa)
* [[Cyber_IoT_Security]] (O recrutamento de zumbis)

**V. Quebra de Aplicação e Criptografia**
* [[Cyber_Ataque_Supply_Chain]] (O envenenamento da fonte)
* [[Cyber_Ataque_SQL_Injection]] (A destruição do banco)
* [[Cyber_Ataque_XSS]] (O sequestro do cliente)
* [[Cyber_Ataque_POODLE]] & [[Cyber_Ataque_BEAST]] (A quebra dos cadeados antigos)
* [[Cyber_Ataque_HNDL]] (O roubo temporal)

#### 4. Pontas Soltas (O que falta mapear?)
* [ ] Mapear as vulnerabilidades de "Zero-Day" e o ciclo de vida do desenvolvimento de Exploits.
* [ ] Criar a dissecação de ataques físicos (Rubber Ducky, BadUSB).
* [ ] Entender a fundo os Ataques de Amplificação de DNS e NTP.

#### 5. O Paralelo Absurdo (Interdisciplinaridade)
Se um ataque a uma infraestrutura cibernética fosse a sabotagem de um restaurante com Estrela Michelin de um rival: 
O **SQL Injection** seria entrar escondido na cozinha e trocar o sal por veneno de rato nas panelas do Chef. 
O **Ransomware** seria trocar as fechaduras do restaurante de madrugada e exigir um pix para devolver a chave antes do almoço começar. 
O **Supply Chain Attack** seria o rival ir até a fazenda que vende os tomates orgânicos para o restaurante e envenenar a plantação inteira na raiz. Qual deles exige menos esforço técnico e causa mais dano colateral?