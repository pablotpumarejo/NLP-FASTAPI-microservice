# 🔌 RESTful API: NLP Sentiment Analysis Microservice

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)
![NLP](https://img.shields.io/badge/AI-VADER%20Sentiment-orange.svg)
![JSON](https://img.shields.io/badge/Data-JSON-lightgrey.svg)

## 📌 Visión General
Este proyecto transforma un modelo de Inteligencia Artificial de Procesamiento de Lenguaje Natural (NLP) en un microservicio web completamente funcional. Expone un *endpoint* RESTful que permite a aplicaciones de terceros (Frontend, Mobile, o Dashboards) enviar texto crudo y recibir un análisis de sentimiento en tiempo real.

El objetivo de negocio es desacoplar la lógica analítica de los procesos locales, creando un servicio centralizado de IA que cualquier departamento de la empresa pueda consumir para evaluar la experiencia del cliente (CX).

## 🚀 Arquitectura del Microservicio

* **1. Framework Asíncrono (`FastAPI`):** Despliegue de un servidor web local de alto rendimiento preparado para manejar múltiples peticiones concurrentes.
* **2. Modelado de Datos (`Pydantic`):** Validación estricta de los datos de entrada (Request Body) garantizando que la API solo procese la estructura JSON correcta, evitando caídas del servidor por datos corruptos.
* **3. Pipeline de IA Integrado:** * Recepción del texto en español.
  * Traducción al vuelo mediante `deep-translator`.
  * Evaluación de polaridad matemática con `vaderSentiment`.
* **4. Estandarización de Salida:** Retorno de un objeto JSON estructurado con el estatus de la petición, el texto original, el veredicto cualitativo y el *score* cuantitativo.

## 🛠️ Swagger UI & Documentación Automática
El proyecto incluye documentación interactiva generada automáticamente bajo el estándar OpenAPI (Swagger), permitiendo a los equipos de desarrollo probar los *endpoints* directamente desde el navegador sin necesidad de escribir código cliente adicional.

## 💡 Impacto de Negocio
Eleva el análisis de datos de un entorno puramente descriptivo (reportes estáticos) a un entorno operativo en tiempo real. Este tipo de arquitectura es la base tecnológica de plataformas de servicio al cliente como Zendesk o sistemas de triage de tickets.
