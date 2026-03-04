---
tags:
  - tipo/conceito
  - contexto/dev/infra
  - afinidade/media
  - status/4_evergreen
---

# Rede_VPN

## 1. O Axioma (A Definição Rígida)
> **O que é:** A VPN (Virtual Private Network) é a tecnologia que cria um túnel criptografado sobre uma rede pública (Internet), permitindo que dados trafeguem com confidencialidade e integridade como se estivessem em um cabo privado.

## 2. A Desconstrução (Mecânica e Pontos de Falha)
* **Como Funciona:** Encapsulamento. Pega o pacote original (IP Privado), criptografa, coloca dentro de um novo pacote (IP Público) e envia. No destino, desencapsula. Protocolos comuns: IPsec, WireGuard, OpenVPN.
* **O Problema que Resolve:** Trabalho remoto e interconexão de filiais (Site-to-Site) sem pagar por linhas dedicadas caríssimas (MPLS).
* **Visão Sênior (Vulnerabilidades/Escala):** VPN não é bala de prata. Se o endpoint (notebook do usuário) estiver infectado com um [[Cyber_Malware_Worm]], a VPN serve como um tubo expresso para o vírus entrar na rede corporativa, pulando o Firewall de borda.

## 3. As Sinapses (Conexões Livres e Interdisciplinares)
A VPN é um **Carro Forte Blindado**. A estrada é perigosa (Internet), cheia de bandidos. Você coloca seu dinheiro (Dados) dentro do carro forte. Os bandidos veem o carro passando, mas não conseguem ver o que tem dentro nem roubar.

## 4. Pragmatismo Aplicado (Código e Implementação)
Subir uma interface WireGuard (Moderno, rápido e simples).
```bash
# Linux: Subir interface wg0
wg-quick up wg0
```

# Audita a conexão estabelecida, o Handshake cifrado e a quantidade de bytes encapsulados 
wg show
````

5. História do Conteúdo

Em 1996, o protocolo original de VPN (PPTP) foi desenvolvido por um consórcio liderado pela Microsoft para atender a uma necessidade estrita: executivos precisavam viajar pelo mundo e acessar a intranet segura da empresa discando pela internet incipiente. O que nasceu estritamente como um elo B2B de grandes megacorporações subverteu-se no século 21. Hoje, as VPNs são escudos para consumidores escaparem de manipulação de provedores (ISPs), garantirem o sigilo em redes não-confiáveis e para civis driblarem severas ferramentas de censura geopolítica global.
## 5. História do Conteúdo
Evoluiu do PPTP (inseguro) para o IPsec (complexo) e agora para o WireGuard (simples e performático).