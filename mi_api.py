# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:37:33 2026

@author: pablo
"""

from fastapi import FastAPI
from pydantic import BaseModel
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator

print("🔌 Conectando los cables del servidor API...")

# 1. Inicializamos la Aplicación Web (El Servidor)
app = FastAPI(title="API de Analítica de Texto (CX)", description="Motor de IA para analizar comentarios en tiempo real")

# 2. Cargamos el cerebro de IA y el Traductor
analizador = SentimentIntensityAnalyzer()
traductor = GoogleTranslator(source='es', target='en')

# 3. Definimos la estructura de datos que vamos a recibir
class PeticionCliente(BaseModel):
    texto: str

# 4. CREAMOS EL ENCHUFE (El Endpoint)
@app.post("/analizar-sentimiento")
def analizar(peticion: PeticionCliente):
    try:
        # Traducimos
        texto_ingles = traductor.translate(peticion.texto)
        
        # Analizamos matemáticamente
        calificacion = analizador.polarity_scores(texto_ingles)
        puntaje = calificacion['compound']
        
        # Clasificamos
        if puntaje >= 0.05:
            veredicto = "🟢 Positivo"
        elif puntaje <= -0.05:
            veredicto = "🔴 Negativo"
        else:
            veredicto = "🟡 Neutral"
            
        # Devolvemos un archivo JSON (el estándar universal de internet)
        return {
            "estatus": "Exito",
            "comentario_recibido": peticion.texto,
            "veredicto_ia": veredicto,
            "score_matematico": puntaje
        }
    except Exception as e:
        return {"estatus": "Error", "detalle": str(e)}

print("✅ Servidor configurado. Listo para encenderse.")