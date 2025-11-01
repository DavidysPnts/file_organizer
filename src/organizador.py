# Futuras melhorias:
# - Usar 'mimetypes' ou 'python-magic' para identificar arquivos pelo conteúdo, dando mais precisão ao código.
# - Implementar sistema de logs para registrar as movimentações.

import os
import shutil

def obter_pasta_alvo():

    # Solicita ao usuário o caminho de uma pasta e valida se ela existe.
    # Retorna o caminho absoluto da pasta.

    while True:
        entrada = input("Digite o caminho da pasta que deseja organizar: ").strip()

        entrada = os.path.expanduser(entrada)
        entrada = os.path.normpath(entrada)
        entrada_abs = os.path.abspath(entrada)

        if os.path.isdir(entrada_abs):
            return entrada_abs
        else:
            print("Caminho inválido. Certifique-se de digitar uma PASTA existente.\n")

def definir_categorias():
    
    # Retorna um dicionário com as categorias e suas extensões associadas.
    # A classificação é feita apenas com base na extensão do arquivo.
    
    return {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
        "Documentos": [".pdf", ".docx", ".txt", ".xls", ".xlsx", ".pptx"],
        "Músicas": [".mp3", ".wav", ".ogg", ".flac", ".m4a", ".aac", ".wma"],
        "Vídeos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".mpeg", ".mpg"],
        "Outros": []
    }

def criar_pastas_categorias(pasta_alvo, categorias):
    
    # Cria dentro da pasta alvo as subpastas correspondentes as categorias.
    # Retorna um dicionário com o caminho absoluto de cada categoria.
    
    mapeamento = {}
    for categoria in categorias:
        caminho_categoria = os.path.join(pasta_alvo, categoria)
        os.makedirs(caminho_categoria, exist_ok=True)
        mapeamento[categoria] = caminho_categoria
    return mapeamento

def achar_categoria_por_extensao(ext, categorias):
    
    # Dada uma extensão de arquivo, retorna a categoria correspondente.
    # Se a extensão não for encontrada, retorna 'Outros'.
    
    ext = ext.lower()
    for categoria, exts in categorias.items():
        if ext in exts:
            return categoria
    return "Outros"

def gerar_nome_unico(destino):
    
    # Gera um nome único caso já exista um arquivo com o mesmo nome no destino.
    
    base, ext = os.path.splitext(destino)
    contador = 1
    novo = destino
    while os.path.exists(novo):
        novo = f"{base}_{contador}{ext}"
        contador += 1
    return novo

def mover_arquivo(arquivo_caminho, pasta_alvo, categorias, mapeamento_pastas):
    
    # Move um arquivo individual para a subpasta correta com base em sua extensão.
    
    if not os.path.isfile(arquivo_caminho):
        return

    nome_arquivo = os.path.basename(arquivo_caminho)
    _, ext = os.path.splitext(nome_arquivo)
    categoria = achar_categoria_por_extensao(ext, categorias)
    destino_dir = mapeamento_pastas.get(categoria, mapeamento_pastas["Outros"])

    destino = os.path.join(destino_dir, nome_arquivo)
    destino = gerar_nome_unico(destino)

    try:
        shutil.move(arquivo_caminho, destino)
        print(f"{nome_arquivo} → {categoria}/")
    except Exception as e:
        print(f"Erro ao mover {nome_arquivo}: {e}")

def processar_pasta(pasta_alvo, categorias):
    
    # Percorre todos os arquivos da pasta e move cada um para a subpasta correspondente.
    
    mapeamento_pastas = criar_pastas_categorias(pasta_alvo, categorias)

    for entrada in os.listdir(pasta_alvo):
        caminho_entrada = os.path.join(pasta_alvo, entrada)

        # Ignora as próprias pastas de categoria
        if os.path.isdir(caminho_entrada) and entrada in categorias:
            continue

        mover_arquivo(caminho_entrada, pasta_alvo, categorias, mapeamento_pastas)

def main():
    print("=== Organizador de Arquivos ===\n")

    pasta_alvo = obter_pasta_alvo()
    categorias = definir_categorias()
    processar_pasta(pasta_alvo, categorias)

    print("\nOrganização concluída com sucesso!")

if __name__ == "__main__":
    main()