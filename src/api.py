from pydoc import text

from fastapi import FastAPI, File, UploadFile, HTTPException 
# UploadFile para recibir el PDF
# File indica a FastAPI que el parámetro es un archivo que se va a subir
# HTTPException para devolver errores prolijos
# Tempfile porque el usuario sube un archivo, pero leer_pdf() espera una ruta. Entonces lo guardamos temporalmente

import tempfile
import os

from src.lector_pdf import leer_pdf
from src.procesador_ia import procesar_receta

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API ON "}

@app.post("/procesar-receta")
async def procesar_receta_api(archivo: UploadFile = File(...)):
    #Validacion de que el archivo es un PDF
    if archivo.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="El archivo debe ser un PDF."
        )
    # Guardar PDF temporalmente
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        contenido = await archivo.read()
        temp.write(contenido)
        ruta_temporal = temp.name
    try:
        #Leer el PDF
        texto = leer_pdf(ruta_temporal)
        resultado = procesar_receta(texto)
        return resultado
    finally:
        # Eliminar el archivo temporal
        if os.path.exists(ruta_temporal):
            os.remove(ruta_temporal)