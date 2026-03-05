---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Ataque_BEAST

#### 1. O Axioma (A Definição Rígida)
BEAST (Browser Exploit Against SSL/TLS) é um ataque criptoanalítico focado na [[Rede_Modelo_OSI|Camada de Apresentação]] que explora o encadeamento de cifras (CBC) no [[Rede_TLS|TLS 1.0]] e [[Rede_SSL|SSL 3.0]], permitindo que um hacker decifre tokens secretos e sequestre sessões da web em texto claro.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Em cifras que operam no modo CBC (Cipher Block Chaining), o próximo bloco de dado a ser encriptado depende matematicamente do bloco anterior (Initialization Vector - IV). No [[Rede_TLS|TLS 1.0]], esse encadeamento é previsível. O atacante injeta código no navegador do alvo (geralmente [[Lang_JavaScript|JavaScript]]), forçando a vítima a enviar milhares de requisições cegas e monitorando os blocos criptografados de saída. Ao adivinhar um byte e compará-lo com a previsão, ele decifra as letras do [[Rede_Cookie|cookie de sessão]], uma por uma.
- **O Problema que Causa:** Resulta na quebra de confidencialidade e no sequestro direto de contas criptografadas ([[Rede_HTTPS]]), mesmo que o invasor não tenha as [[Cyber_Criptografia_Assimetrica|chaves assimétricas]] mestre do servidor.
- **Visão Sênior (Vulnerabilidades/Escala):** Embora matematicamente letal, o ataque exige condições operacionais absurdas e barulhentas: o atacante tem que aplicar um [[Cyber_Man_In_The_Middle]] agressivo e forçar o envio de milhões de requisições simultâneas na máquina do usuário para decifrar poucos bytes. É mitigado permanentemente ao abandonar o [[Rede_TLS|TLS 1.0]] e usar TLS 1.2+ operando com modo de blocos GCM/AEAD ao invés de CBC.

#### 3. As Sinapses (Conexões Livres)
A mecânica do [[Cyber_Ataque_BEAST]] opera como o **Jogo da Forca com uma impressora infinita**. O hacker tem um texto em código estranho impresso no papel (a senha do alvo), mas sabe que o sistema usa os símbolos de cima para gerar os de baixo. Ele começa a obrigar a máquina da vítima a imprimir milhares de tentativas usando palavras aleatórias ("É A?", "É B?"). Quando o pedaço impresso gerado ficar visualmente igual ao pedaço codificado da senha real, ele sabe que adivinhou a letra correta. 

#### 4. Pragmatismo Aplicado (Código/Implementação)
O diagnóstico contra vulnerabilidades criptográficas legadas em navegadores e servidores muitas vezes não exige testes manuais exaustivos de IVs; usam-se auditorias focadas, como varreduras em portas externas via Nmap, para verificar o nível da criptografia oferecida pelo servidor:
```bash
# Usa script de Nmap para atestar a lista e a força das cifras e dos modos de encadeamento operantes no servidor. Se acusar CBC no TLS 1.0, o ambiente está exposto ao BEAST:
nmap --script ssl-enum-ciphers -p 443 www.alvo.com
````

5. História do Conteúdo

A falha fundamental do modo CBC já era amplamente teórica na academia e documentada em fóruns de criptografia desde 2002. Contudo, acreditava-se que seria impossível realizar um ataque silencioso desses na prática em uma rede dinâmica. Em 2011, os pesquisadores Thai Duong e Juliano Rizzo chocararm a indústria ao provarem em uma conferência de segurança que criaram um [[Lang_JavaScript|JavaScript]] injetável que explorava a vulnerabilidade em tempo real usando [[Lang_Java|Java]] applets e websockets, provando que o TLS 1.0 não era mais seguro.