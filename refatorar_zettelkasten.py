import os
import re

# Adicionada a tipagem (filepath: str)
def process_file(filepath: str) -> None:
    # Dicionário implacável de correção de taxonomia
    context_mapping = {
        # Família de Ataques (Alvo da sua exceção)
        r"contexto/ataques_redes": "contexto/dev/cyber/ataque",
        r"contexto/ataques_endpoint": "contexto/dev/cyber/ataque",
        r"contexto/ataques_aplicacao": "contexto/dev/cyber/ataque",
        r"contexto/ataques_avancados": "contexto/dev/cyber/ataque",
        
        # Família de Segurança Geral e Governança
        r"contexto/cyber_security": "contexto/dev/cyber",
        r"contexto/governanca": "contexto/dev/cyber",
        r"contexto/auditoria_redes": "contexto/dev/cyber",
        r"contexto/seguranca_criptografia": "contexto/dev/cyber",
        r"contexto/seguranca_identidade": "contexto/dev/cyber",
        r"contexto/seguranca_nuvem": "contexto/dev/cyber"
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[ERRO] Não foi possível ler {filepath}: {e}")
        return

    original_content = content
    is_attack = False

    # 1. Aplicação da Taxonomia Correta no Frontmatter
    for old_context, new_context in context_mapping.items():
        if re.search(old_context, content):
            content = re.sub(old_context, new_context, content)

    # 2. Detecção de Anomalia (É um ataque?)
    # Verifica se a nota acabou de ser categorizada como ataque ou se o título tem a nomenclatura de malware/ataque
    if "contexto/dev/cyber/ataque" in content or "Cyber_Ataque" in content or "Cyber_Malware" in content:
        is_attack = True

    # 3. Ajuste Condicional da Chave da Forja
    if is_attack:
        # Para ataques, o padrão "Resolve" não faz sentido. Forçamos para "Causa".
        content = re.sub(r"\*\s+\*\*O Problema que Resolve:\*\*", "* **O Problema que Causa:**", content)
    else:
        # Para ferramentas e conceitos operacionais, forçamos o retorno para "Resolve" caso tenha sido alterado.
        content = re.sub(r"\*\s+\*\*O Problema que Causa:\*\*", "* **O Problema que Resolve:**", content)

    # 4. Gravação Cirúrgica (Apenas se houver mudança para poupar I/O de disco)
    if content != original_content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            tipo = "[ATAQUE]" if is_attack else "[CONCEITO/FERRAMENTA]"
            print(f"[CORRIGIDO] {tipo} - {filepath}")
        except Exception as e:
            print(f"[ERRO] Falha ao salvar {filepath}: {e}")

def main() -> None:
    print("Iniciando varredura da Forja...")
    modificados = 0
    # Substituída a variável 'dirs' por '_' para calar o linter
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                process_file(os.path.join(root, file))
                modificados += 1
    
    print(f"Varredura concluída. Forja higienizada e alinhada ao novo paradigma.")

if __name__ == "__main__":
    main()