import os
import shutil
import hashlib
from pathlib import Path

# Configurações de Diretórios
DIR_ORIGEM = Path("./")
DIR_DESTINO = Path("CEREBRO_MASTER")

# Estrutura do Novo Sistema
ESTRUTURA_MASTER = {
    "00_Inbox": DIR_DESTINO / "00_Inbox",
    "01_Projetos_e_Diarios": DIR_DESTINO / "01_Projetos_e_Diarios",
    "02_Engenharia_Software": DIR_DESTINO / "02_Engenharia_Software",
    "03_Idiomas": DIR_DESTINO / "03_Idiomas",
    "04_Filosofia_e_Estrategia": DIR_DESTINO / "04_Filosofia_e_Estrategia",
    "05_Recursos_Vida": DIR_DESTINO / "05_Recursos_Vida", # Gastronomia, Viagens, Finanças
    "06_Zettelkasten": DIR_DESTINO / "06_Zettelkasten",
    "99_Arquivo_Morto": DIR_DESTINO / "99_Arquivo_Morto",
    "Seguranca_Isolada": DIR_DESTINO / "Seguranca_Isolada" # Para PII e Faturas
}

def calcular_hash(caminho_arquivo):
    """Gera um hash SHA-256 do CONTEÚDO do arquivo para achar duplicados exatos."""
    hasher = hashlib.sha256()
    try:
        with open(caminho_arquivo, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception:
        return None

def determinar_destino(nome_arquivo):
    """Roteamento inteligente baseado nos prefixos dos teus ficheiros."""
    nome = nome_arquivo.lower()
    
    # 1. Arquivo Morto (Baixo ROI)
    mortos = ['cantada_', 'tatica_', 'conversa_', 'date_', 'leitura_', 'pergunta_', 'arte_seducao']
    if any(m in nome for m in mortos): return ESTRUTURA_MASTER["99_Arquivo_Morto"]
    
    # 2. Engenharia e Tech
    tech = ['java_', 'react_', 'db_', 'cyber_', 'algoritmo_', 'linux_', 'redes_', 'fiap_']
    if any(t in nome for t in tech): return ESTRUTURA_MASTER["02_Engenharia_Software"]
    
    # 3. Idiomas
    idiomas = ['aula_', 'vocab_', 'regra_', 'tempo_', 'conceito_', 'ingles', 'mandarim']
    if any(i in nome for i in idiomas): return ESTRUTURA_MASTER["03_Idiomas"]
    
    # 4. Filosofia e Mindset
    filosofia = ['mindset_', 'filosofia_', 'estrategia_', 'poema_', 'livro_']
    if any(f in nome for f in filosofia): return ESTRUTURA_MASTER["04_Filosofia_e_Estrategia"]
    
    # 5. Recursos de Vida
    vida = ['financas_', 'caldo_', 'carne_', 'doce_', 'drink_', 'entrada_', 'mar_', 'massa_', 'molho_', 'risoto_', 'local_', 'dica_', 'banho_', 'controle_', 'lista_']
    if any(v in nome for v in vida): return ESTRUTURA_MASTER["05_Recursos_Vida"]
    
    # 6. Projetos e Registros Diários
    projetos = ['diario', 'projeto_', 'metas_', 'carreira_', 'cv_']
    if any(p in nome for p in projetos): return ESTRUTURA_MASTER["01_Projetos_e_Diarios"]
    
    # 7. Dados Sensíveis / PII (Isolamento)
    if 'fatura' in nome or 'passwords' in nome: return ESTRUTURA_MASTER["Seguranca_Isolada"]

    # Padrão: Caixa de Entrada para revisão manual
    return ESTRUTURA_MASTER["00_Inbox"]

def executar_migracao_mestra():
    print("[*] A criar ambiente CEREBRO_MASTER...")
    for pasta in ESTRUTURA_MASTER.values():
        pasta.mkdir(parents=True, exist_ok=True)

    hashes_processados = set()
    arquivos_copiados = 0
    duplicados_ignorados = 0

    print("[*] A iniciar varredura e deduplicação...")
    for raiz, _, arquivos in os.walk(DIR_ORIGEM):
        for arquivo in arquivos:
            # Ignorar arquivos de sistema
            if arquivo.startswith('.'): continue
            
            caminho_completo = Path(raiz) / arquivo
            file_hash = calcular_hash(caminho_completo)
            
            if not file_hash: continue # Ignora se não conseguir ler

            # Deduplicação Mágica
            if file_hash in hashes_processados:
                duplicados_ignorados += 1
                continue
            
            # Se for novo/único, processar
            hashes_processados.add(file_hash)
            pasta_destino = determinar_destino(arquivo)
            
            # Garantir que não há colisão de nomes com arquivos de conteúdos diferentes
            destino_final = pasta_destino / arquivo
            contador = 1
            while destino_final.exists():
                nome_sem_ext = destino_final.stem
                extensao = destino_final.suffix
                destino_final = pasta_destino / f"{nome_sem_ext}_{contador}{extensao}"
                contador += 1
                
            shutil.copy2(caminho_completo, destino_final)
            arquivos_copiados += 1

    print("\n--- RELATÓRIO DE MIGRAÇÃO ---")
    print(f"Arquivos Únicos Salvos: {arquivos_copiados}")
    print(f"Duplicados Eliminados com Sucesso: {duplicados_ignorados}")
    print("-----------------------------\n")
    print("[+] SUCESSO. O teu novo sistema está em 'CEREBRO_MASTER'.")
    print("[!] O teu diretório 'Conhecimentos' original não foi tocado. Podes apagá-lo quando te sentires seguro.")

if __name__ == "__main__":
    if not DIR_ORIGEM.exists():
        print(f"Erro: A pasta '{DIR_ORIGEM}' não foi encontrada.")
    else:
        executar_migracao_mestra()