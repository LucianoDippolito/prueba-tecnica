import json
from google import genai
from src.config import GOOGLE_API_KEY

def procesar_receta(texto: str) -> dict:
    with open("src/prompts/receta_prompt.txt", "r", encoding="utf-8") as archivo:
        prompt = archivo.read()

    prompt = prompt.replace("{{TEXTO_PDF}}", texto)
    
    cliente = genai.Client(api_key=GOOGLE_API_KEY)
    respuesta = cliente.models.generate_content(
        model = "gemini-2.5-flash",
        contents = prompt
    )
    return json.loads(respuesta.text)