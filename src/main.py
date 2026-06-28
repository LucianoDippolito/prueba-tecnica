from lector_pdf import leer_pdf

if __name__ == "__main__":
    ruta_pdf = "recetas/1.pdf"

    texto = leer_pdf(ruta_pdf)

    print(texto)