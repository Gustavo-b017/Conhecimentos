import os
import shutil
import hashlib
from pathlib import Path
from typing import Optional, Set, Dict

# 1. ARQUITETURA DE CAMINHOS SEGUROS
# DIR_ORIGEM pega exatamente a pasta onde este script está salvo (Conhecimentos)
DIR_ORIGEM: Path = Path(__file__).parent.resolve()

# DIR_DESTINO cria uma pasta limpa um nível acima (dentro de Documents/Obsidian/)
DIR_DESTINO: Path = DIR_ORIGEM.parent / "Segundo_Cerebro_Hibrido"

# Estrutura do Novo Sistema Híbrido com anotação de tipo explícita
ESTRUTURA: Dict[str, Path] = {
    # ECOSSISTEMA 1: A ZONA DE PENSAMENTO (O Caos Conectivo)
    "00_Captura": DIR_DESTINO / "00_Captura_e_Caos",
    "01_Forja": DIR_DESTINO / "01_A_Forja",
    "02_Constelacoes": DIR_DESTINO / "02_Constelacoes",
    "03_Ancoras": DIR_DESTINO / "03_Ancoras_Temporais",
    
    # ECOSSISTEMA 2: A ZONA UTILITÁRIA (A Ordem Absoluta)
    "04_Gastro_Tecnicas": DIR_DESTINO / "04_Bases_Utilitarias" / "04.1_Gastronomia" / "00_Tecnicas_e_Bases",
    "04_Gastro_Entradas": DIR_DESTINO / "04_Bases_Utilitarias" / "04.1_Gastronomia" / "01_Entradas_e_Aperitivos",
    "04_Gastro_Principais": DIR_DESTINO / "04_Bases_Utilitarias" / "04.1_Gastronomia" / "02_Pratos_Principais",
    "04_Gastro_Sobremesas": DIR_DESTINO / "04_Bases_Utilitarias" / "04.1_Gastronomia" / "03_Sobremesas",
    "04_Gastro_Bebidas": DIR_DESTINO / "04_Bases_Utilitarias" / "04.1_Gastronomia" / "04_Mixologia_e_Bebidas",
    "04_Gastro_Menus": DIR_DESTINO / "04_Bases_Utilitarias" / "04.1_Gastronomia" / "99_Menus_Completos",
    "04_Logistica": DIR_DESTINO / "04_Bases_Utilitarias" / "04.2_Logistica_e_Viagens",
    "04_Idiomas": DIR_DESTINO / "04_Bases_Utilitarias" / "04.3_Idiomas_e_Linguistica",
    "04_Projetos": DIR_DESTINO / "04_Bases_Utilitarias" / "04.4_Projetos_e_Carreira",
    
    # LIXO / ISOLAMENTO
    "99_Arquivo_Morto": DIR_DESTINO / "99_Arquivo_Morto",
    "Seguranca": DIR_DESTINO / "Seguranca_Isolada"
}

def calcular_hash(caminho_arquivo: Path) -> Optional[str]:
    """Gera o hash do arquivo para garantir que não copiamos duplicados reais."""
    hasher = hashlib.sha256()
    try:
        with open(caminho_arquivo, 'rb') as f:
            buf: bytes = f.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception:
        return None

def determinar_destino(nome_arquivo: str, caminho_relativo: Path) -> Path:
    """Roteador Lógico Híbrido."""
    nome: str = nome_arquivo.lower()
    caminho_str: str = str(caminho_relativo).lower()
    
    # Ignorar o próprio script
    if nome == "refatorar_cerebro.py" or nome == "arquitetura_hibrida.py":
        return ESTRUTURA["04_Projetos"]

    # 1. Manter Arquivo Morto e Dados Sensíveis isolados
    if "arquivo_morto" in caminho_str or "seducao" in nome or "cantada_" in nome or "tatica_" in nome or "conversa_" in nome or "abordagem_" in nome:
        return ESTRUTURA["99_Arquivo_Morto"]
    if "passwords" in nome or "fatura" in nome:
        return ESTRUTURA["Seguranca"]

    # 2. Ancoras Temporais (Diários)
    if "diario" in nome or "2025-" in nome or "2026-" in nome:
        return ESTRUTURA["03_Ancoras"]
        
    # 3. Constelações (MOCs e Arquitetura)
    if "moc_" in nome or "arquitetura" in nome:
        return ESTRUTURA["02_Constelacoes"]

    # 4. Zona Utilitária: Idiomas (A Sintaxe e Manuais)
    idiomas = ['aula_', 'vocab_', 'regra_', 'tempo_', 'conceito_', 'vocubulario']
    if any(i in nome for i in idiomas): return ESTRUTURA["04_Idiomas"]

    # 5. Zona Utilitária: Projetos e Carreira
    projetos = ['projeto_', 'metas_', 'carreira_', 'cv_']
    if any(p in nome for p in projetos): return ESTRUTURA["04_Projetos"]

    # 6. Zona Utilitária: Logística e Viagens
    logistica = ['local_', 'dica_', 'financas_', 'lista_']
    if any(l in nome for l in logistica): return ESTRUTURA["04_Logistica"]

    # 7. Zona Utilitária: Gastronomia (Milimetricamente Organizada)
    if any(x in nome for x in ['tecnica_', 'molho_', 'caldo_']): return ESTRUTURA["04_Gastro_Tecnicas"]
    if 'entrada_' in nome: return ESTRUTURA["04_Gastro_Entradas"]
    if any(x in nome for x in ['carne_', 'massa_', 'mar_', 'risoto_']): return ESTRUTURA["04_Gastro_Principais"]
    if 'doce_' in nome: return ESTRUTURA["04_Gastro_Sobremesas"]
    if 'drink_' in nome: return ESTRUTURA["04_Gastro_Bebidas"]
    if 'menu_' in nome: return ESTRUTURA["04_Gastro_Menus"]

    # 8. A FORJA (O núcleo da Superdotação - Tudo o resto que gera conexões)
    forja_tags = ['filosofia_', 'estrategia_', 'mindset_', 'poema_', 'java_', 'react_', 'redes_', 'db_', 'cyber_', 'fiap_', 'algoritmo_', 'linux_', 'sindrome_', 'controle_', 'banho_']
    if any(f in nome for f in forja_tags): return ESTRUTURA["01_Forja"]

    # 9. Fallback (Tudo o que for novo ou não reconhecido)
    return ESTRUTURA["00_Captura"]

def executar_implementacao_hibrida() -> None:
    if not DIR_ORIGEM.exists():
        print(f"[!] Erro: A pasta '{DIR_ORIGEM}' não foi encontrada.")
        return

    print(f"[*] A ler dados de: {DIR_ORIGEM}")
    print(f"[*] A construir a Arquitetura Híbrida em: {DIR_DESTINO}")
    
    for pasta in ESTRUTURA.values():
        pasta.mkdir(parents=True, exist_ok=True)
        
    # Copiar as configurações do Obsidian se existirem
    obsidian_origem: Path = DIR_ORIGEM / ".obsidian"
    obsidian_destino: Path = DIR_DESTINO / ".obsidian"
    if obsidian_origem.exists() and not obsidian_destino.exists():
        shutil.copytree(obsidian_origem, obsidian_destino)

    hashes_processados: Set[str] = set()
    arquivos_movidos: int = 0

    for raiz, _, arquivos in os.walk(DIR_ORIGEM):
        # Impedir que o script leia as pastas que ele próprio criou se houver resquícios do teu run anterior
        caminho_raiz = Path(raiz)
        if ".obsidian" in caminho_raiz.parts or "Segundo_Cerebro_Hibrido" in caminho_raiz.parts: 
            continue
            
        for arquivo in arquivos:
            if arquivo.startswith('.'): continue
            
            caminho_completo: Path = caminho_raiz / arquivo
            file_hash: Optional[str] = calcular_hash(caminho_completo)
            
            if not file_hash or file_hash in hashes_processados:
                continue 
            
            hashes_processados.add(file_hash)
            
            caminho_relativo: Path = caminho_completo.relative_to(DIR_ORIGEM)
            pasta_destino: Path = determinar_destino(arquivo, caminho_relativo)
            
            destino_final: Path = pasta_destino / arquivo
            
            # Tratamento de Colisões
            contador: int = 1
            while destino_final.exists():
                destino_final = pasta_destino / f"{destino_final.stem}_{contador}{destino_final.suffix}"
                contador += 1
                
            shutil.copy2(caminho_completo, destino_final)
            arquivos_movidos += 1

    print("\n--- RELATÓRIO DE INFRAESTRUTURA ---")
    print(f"Total de Notas Processadas e Enraizadas: {arquivos_movidos}")
    print("O teu Ecossistema Híbrido está operacional e seguro.")
    print(f"Abra o Obsidian e selecione a pasta: {DIR_DESTINO}")
    print("-----------------------------------\n")

if __name__ == "__main__":
    executar_implementacao_hibrida()