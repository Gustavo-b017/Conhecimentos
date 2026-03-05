---
tags:
  - tipo/conceito
  - contexto/dev/cyber/ataque
  - afinidade/alta
  - status/3_incubadora
---

### Cyber_Ataque_SQL_Injection

#### 1. O Axioma (A Definição Rígida)
**O que é:** A Injeção de SQL (SQLi) é uma [[Cyber_Vulnerabilidade|vulnerabilidade]] crítica da Camada de Aplicação onde um invasor manipula campos de entrada de um site para inserir comandos SQL maliciosos, forçando o banco de dados do servidor a executar ações não autorizadas.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
- **Como Funciona:** Ocorre quando o código de uma aplicação concatena textos digitados pelo usuário diretamente nas queries do [[DB_Banco_de_Dados|banco de dados]] sem sanitização prévia. O atacante usa aspas simples `'` para "escapar" do campo de texto e adiciona a sua própria lógica matemática (ex: `OR 1=1`) para enganar a autenticação.
- **O Problema que Causa:** O banco de dados obedece cegamente ao código injetado, permitindo que o invasor contorne o login, acesse informações sensíveis de outros usuários, altere registros ou até delete tabelas inteiras.
- **Visão Sênior (Vulnerabilidades/Escala):** Firewalls de rede estáticos ou com [[Cyber_Firewall_Stateful|inspeção de estado]] falham completamente contra este ataque, pois o payload malicioso trafega encapsulado por um pacote HTTP/[[Rede_HTTPS|HTTPS]] legítimo nas portas 80/443. A mitigação arquitetural sênior exige o bloqueio na borda através de um [[Cyber_Firewall_WAF|WAF]] e, principalmente, a restrição de permissões no banco de dados e o uso obrigatório de consultas parametrizadas (*Prepared Statements*) no código.

#### 3. As Sinapses (Conexões Livres)
A Injeção de SQL é como **entregar um cheque em branco assinado para um estranho preencher o nome dele, mas ele resolve escrever instruções para o caixa do banco roubar o cofre**. A aplicação (o caixa do banco) não percebe a diferença entre o que era um dado (o nome) e o que era um comando (a instrução de roubo), processando a folha de papel inteira de uma vez só.

#### 4. Pragmatismo Aplicado (Código/Implementação)
Exemplo prático de implementação segura (citado nos testes de penetração) usando Python com banco de dados SQLite, aplicando Consultas Parametrizadas. Ao usar o ponto de interrogação `?`, o sistema isola a entrada do usuário como "apenas texto", impedindo que ela seja interpretada como código SQL executável:
```python
import sqlite3
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()
# Implementação blindada contra injeção utilizando substituição segura
cursor.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
````

5. História do Conteúdo

Surgiu no final dos anos 1990 com a explosão de sites dinâmicos conectados a bancos de dados. Ironicamente, apesar de ser um dos ataques mais antigos, compreendidos e fáceis de consertar da história da computação, a injeção SQL continua figurando sistematicamente nas listas de vulnerabilidades do [[Cyber_OWASP_Top_10|OWASP Top 10]] devido à negligência crônica na cultura de _[[DevSecOps_Secure_Coding|Secure Coding]]_.