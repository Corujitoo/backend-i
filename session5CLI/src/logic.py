def salvar_no_arquivo(texto: str):
    """Apenas abre o arquivo e escreve a linha."""
    with open("conta.json", "a", encoding="utf-8") as arquivo:
        arquivo.write(texto + "\n")