from lector_pdf import leer_pdf
from procesador_ia import procesar_receta
import json

def main():
    ruta_pdf = "recetas/1.pdf"
    texto = leer_pdf(ruta_pdf)
    resultado = procesar_receta(texto)
    print(json.dumps(resultado, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()