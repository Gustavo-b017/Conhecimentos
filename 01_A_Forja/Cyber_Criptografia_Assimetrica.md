---
tags:
  - tipo/conceito
  - contexto/dev/cyber
  - afinidade/alta
  - status/4_evergreen
---

### Cyber_Criptografia_Assimetrica
#### 1. O Axioma (A Definição Rígida)
**O que é:** A criptografia assimétrica (ou de Chave Pública) é um algoritmo matemático de sentido único que utiliza um par de chaves inseparáveis — uma Pública (para criptografar dados) e uma Privada (para descriptografar) — permitindo a troca segura de segredos em canais de rede totalmente inseguros.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Diferente da [[Cyber_Criptografia_Simetrica|criptografia simétrica]] (onde uma senha única tranca e destranca o arquivo), aqui a matemática é baseada na fatoração de números primos gigantescos (algoritmo RSA) ou Curvas Elípticas (ECC). Eu publico a minha Chave Pública para o mundo inteiro. Qualquer pessoa pode usar essa chave para trancar uma mensagem para mim, mas **somente a minha Chave Privada** tem o poder físico/matemático de destrancar.
*   **O Problema que Resolve:** Resolve a "Falha da Troca de Chaves". Como duas máquinas que nunca se viram na vida podem criar e usar uma senha secreta para conversar na internet (via [[Rede_TLS]]) sem que um espião ([[Cyber_Eavesdropping]] ou [[Cyber_Man_In_The_Middle]]) roube a senha no caminho? A matemática assimétrica permite a troca de confiança no meio da praça pública.
*   **Visão Sênior (Vulnerabilidades/Escala):** Algoritmos assimétricos são de 100 a 1.000 vezes mais pesados para a CPU do que o [[Cyber_AES_256]]. Por isso, na prática, nunca usamos criptografia assimétrica para cifrar grandes arquivos de dados; nós a usamos **apenas para trafegar a chave simétrica temporária** no início da conexão (Handshake) e depois usamos a chave simétrica para a troca real de dados em alta velocidade. Ameaça futura: A computação quântica (via Algoritmo de Shor) promete quebrar o RSA em minutos (o ataque [[Cyber_Ataque_HNDL]]), o que destruiria todo o e-commerce mundial instantaneamente se a transição para Pós-Quântica (PQC) não for feita.

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
A [[Cyber_Criptografia_Assimetrica]] é a **Caixa de Correio dos Estados Unidos**. A fenda da caixa (A Chave Pública) é exposta na rua e não tem dono; o seu vizinho, o carteiro ou o Papa podem colocar uma carta lá dentro. No entanto, uma vez que a carta cai na caixa, ninguém no planeta consegue pegá-la de volta pela fenda (função matemática *Trapdoor*). Apenas o carteiro oficial possui a Chave do Cadeado da Porta Inferior (A Chave Privada) que abre o cofre para retirar as correspondências.

#### 4. Pragmatismo Aplicado (Código e Implementação)
A fundação de todo acesso remoto seguro em nuvem. A geração clássica de um par de chaves assimétricas usando o terminal Linux para poder se logar via [[Rede_SSH|SSH]] num servidor [[Cloud_AWS|AWS]] sem nunca trafegar senhas em texto puro:
```bash
# Gera o par de chaves usando o moderno e elíptico algoritmo ed25519
ssh-keygen -t ed25519 -C "admin@minhaempresa.com"

# Isso cria dois arquivos:
# id_ed25519 (Sua Chave Privada - Fica blindada no seu notebook. NUNCA COMPARTILHE)
# id_ed25519.pub (Sua Chave Pública - Você cola no servidor AWS, GitHub ou manda por email)
````

5. História do Conteúdo

Até 1976, toda a criptografia do mundo era simétrica (como a máquina Enigma nazista). Se um exército quisesse se comunicar com segurança com um general no exterior, um espião precisava viajar até o país destino carregando uma maleta algemada ao pulso com um caderno de códigos (a chave). A inovação histórica ocorreu quando Whitfield Diffie e Martin Hellman publicaram seu artigo ("New Directions in Cryptography"), provando matematicamente pela primeira vez na história humana que você poderia mandar um cadeado aberto por correio para um estranho, ele trancaria o segredo, e mandaria de volta, extinguindo a necessidade dos espiões das maletas.