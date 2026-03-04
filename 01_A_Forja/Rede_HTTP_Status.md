---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/alta
  - status/4_evergreen
---

### Rede_HTTP_Status

#### 1. O Axioma (A Definição Rígida)
**O que é:** Os Status Codes do HTTP são semáforos numéricos de 3 dígitos inseridos no cabeçalho das respostas da Camada de Aplicação, responsáveis por informar programaticamente ao cliente o exato resultado da sua requisição, agrupados em 5 famílias de comportamento.

#### 2. A Desconstrução (Mecânica e Pontos de Falha)
*   **Como Funciona:** Dividem-se em classes. **2xx** (Sucesso). **3xx** (Redirecionamento/Cache). **4xx** (Erro do Cliente - você mandou errado). **5xx** (Erro do Servidor - o nosso código quebrou).
*   **O Problema que Resolve:** Permite que sistemas autônomos tomem decisões sem intervenção humana. Se o celular tenta baixar uma foto e recebe `404 Not Found`, ele para de tentar. Se recebe `503 Service Unavailable`, ele engatilha o algoritmo de [[Arquitetura_Retry]] para tentar de novo daqui a 5 segundos.
*   **Visão Sênior (Vulnerabilidades/Escala):** O crime mais grotesco no design de APIs é mentir no Status. Retornar `200 OK` quando uma transação falhou, mas colocar o erro dentro do JSON (`{"status": "erro"}`) quebra a internet inteira (Cache, Proxies, Gateways). O erro sênior de validação lógica (ex: "CPF inválido") **não deve** retornar `400 Bad Request` (que é para sintaxe quebrada) e muito menos `500 Internal Server Error` (que aciona os pagers de emergência da infraestrutura durante a madrugada), o correto é devolver `422 Unprocessable Entity` (Sintaxe correta, mas violação de regra de negócio).

#### 3. As Sinapses (Conexões Livres e Interdisciplinares)
Os Status HTTP são as **Luzes do Painel do Carro**.
*   **2xx (Luz Verde/Apagada):** O motor está normal.
*   **3xx (Seta de Conversão):** O GPS recalculou a rota e você foi desviado.
*   **4xx (Luz da Reserva de Combustível):** O carro está apitando porque VOCÊ, o motorista (Cliente), esqueceu de abastecer ou não tem a chave da porta (401/403). O mecânico não pode fazer nada.
*   **5xx (Luz Vermelha do Motor/Fogo):** O motor fundiu. A culpa é do fabricante (Servidor). O motorista não tem como resolver, apenas esperar o conserto.

#### 4. Pragmatismo Aplicado (Código e Implementação)
As regras de bolso mapeadas na cartilha da FIAP para um design maduro:
```text
Criação (POST): 201 Created (Sempre enviar o header "Location" com a URI do novo recurso)
Deletar (DELETE): 204 No Content (Deletou com sucesso, não devolva um JSON de volta, poupe banda)
Falta de Login: 401 Unauthorized (Quem é você?)
Falta de Permissão: 403 Forbidden (Eu sei quem é você, mas você não é o Gerente para fazer isso)
Erro de Domínio (Negócio): 422 Unprocessable Entity (Ex: Saldo insuficiente para compra)
````

5. História do Conteúdo

Criados no alvorecer da Web (HTTP/1.0) por Tim Berners-Lee no CERN. Ele não tirou esses números do zero; ele roubou a estrutura lógica dos códigos numéricos do protocolo [[Rede_FTP]], que já existia na década anterior. Hoje, a correta aplicação dos status (especialmente no nível 2 do Modelo de Maturidade de Richardson) é a prova definitiva que separa o "Programador de Código Funcional" do "Arquiteto de Software Web".