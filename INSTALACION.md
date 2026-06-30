# Lector de Recetas Médicas

API desarrollada en Python que permite recibir una receta médica digital en formato PDF, extraer su contenido y devolver la información estructurada en formato JSON utilizando IA (Google Gemini).

---

# Tecnologías utilizadas

- Python 3.12
- FastAPI
- PyMuPDF
- Google Gemini
- python-dotenv

---

# Instalación

1- Clonar el repositorio.

2- Instalar las dependencias:

```bash
pip install -r requirements.txt
```

---

# Configuración

Crear un archivo `.env` con la siguiente variable:

```env
GOOGLE_API_KEY= **TU_API_KEY**
```

---

# Ejecutar la API

Desde la carpeta del proyecto ejecutar:

```bash
uvicorn src.api:app --reload
```

La aplicación va a estar disponible en:

```
http://127.0.0.1:8000
```

La documentación interactiva de FastAPI esta en:

```
http://127.0.0.1:8000/docs
```

---

# Uso

1. Abrir la documentación de FastAPI (`/docs`).
2. Seleccionar el endpoint **POST /procesar-receta**.
3. Presionar **Try it out**.
4. Seleccionar un archivo PDF.
5. Ejecutar la petición.
6. La API va a devolver la información extraída en formato JSON.

---


# Estructura

```
lector_recetas
    recetas
        1.pdf
        2.pdf
    src
        prompts
            receta-prompt.txt
        api.py
        config.py
        lector_pdf.py
        procesador_ia.py
    .env
    .gitignore
    INSTALACION.md
    README.md
    requirements.txt
    SOLUCION.md
```