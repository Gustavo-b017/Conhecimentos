---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/media
  - status/3_incubadora
---

### Cyber_Eavesdropping

#### 1. O Axioma (A Definição Rígida)
**O que é:** O Eavesdropping é um ataque cibernético de inteligência onde o invasor intercepta e escuta de forma puramente passiva as transmissões de rede não criptografadas para coletar informações confidenciais, senhas e dados bancários.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** O atacante conecta sua placa de rede em modo promíscuo em uma rede [[Rede_WLAN_e_WiFi]] aberta ou adultera um cabo de fibra/[[Rede_Switch|switch]] (espelhamento de porta) em redes metropolitanas (MAN). Ele acopla uma ferramenta de captura (sniffer) como o [[Ferramenta_Wireshark]] e começa a ler silenciosamente todos os bits que cruzam o espaço aéreo ou o fio.
- **O Problema que Resolve:** Para o atacante, resolve o problema de roubo de credenciais sem disparar alarmes, servindo de fundação técnica em metodologias de OSINT aplicadas a infraestruturas locais.
- **Visão Sênior (Vulnerabilidades/Escala):** A genialidade e o terror desse ataque é que ele **não altera o tráfego**. Sistemas de Prevenção ([[Cyber_IPS]]) são majoritariamente cegos a ele, pois não há queda de latência nem injeção de malware. Se o dado não for rigorosamente blindado com [[Cyber_AES_256|Cyber_Criptografia]] ([[Cyber_Criptografia]]) na fonte, a rede inteira é comprometida de forma invisível.

#### 3. As Sinapses (Conexões Livres)
O [[Cyber_Eavesdropping]] é o equivalente tático de encostar **um copo de vidro na parede para ouvir a reunião do quarto vizinho**. Você não arromba a porta ([[Rede_Firewall|Firewall]]), você não participa da reunião (Interação) e você não altera o assunto. Você apenas anota cada palavra no seu caderno. O pior cenário ocorre quando funcionários acessam a infraestrutura da empresa sentados na praça de alimentação via "[[Rede_WLAN_e_WiFi|Wi-Fi]] Livre". Eles estão gritando senhas corporativas numa sala cheia de pessoas usando copos de vidro.

#### 4. Pragmatismo Aplicado (Código/Implementação)
Comando clássico de um analista forense (ou atacante) via `tcpdump` para escutar pacotes brutos flutuando na rede sem permissão direta, focado na busca ingênua de senhas não encriptadas em texto claro:
```bash
# Farejar tráfego na placa eth0 procurando portas inseguras (FTP/HTTP) e guardando em arquivo
sudo tcpdump -i eth0 -w escuta_secreta.pcap port 21 or port 80
````

5. História do Conteúdo

A palavra (literalmente "ouvir do beiral do telhado") vem da espionagem civil da idade média. No mundo da rede de computadores, o ataque nasceu pela ingenuidade absoluta dos antigos Hubs Ethernet ([[Rede_Hardware]]), que replicavam o tráfego para todas as portas elétricas. Na época, bastava plugar o cabo na parede do prédio para ler o e-mail do CEO.