import fitz


def leer_pdf(ruta_pdf: str) -> str:
    texto = ""

    with fitz.open(ruta_pdf) as pdf:
        for pagina in pdf:
            texto += pagina.get_text() + "\n"

    return texto