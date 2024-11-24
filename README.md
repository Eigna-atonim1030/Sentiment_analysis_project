# Sentiment Analysis Project 🎯  
Análisis de sentimientos en redes sociales utilizando Python, Anaconda y técnicas de procesamiento de lenguaje natural (NLP).

## Tabla de Contenidos 📑
- [Descripción](#descripción)
- [Características](#características)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Pasos para Ejecutar el Proyecto](#pasos-para-ejecutar-el-proyecto)
- [Ejemplo de Resultados](#ejemplo-de-resultados)
- [Tecnologías Usadas](#tecnologías-usadas)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Descripción 📝
Este proyecto realiza un análisis de sentimientos basado en tweets extraídos de Twitter. Utilizando técnicas de procesamiento de lenguaje natural, clasifica los sentimientos en categorías como **positivo**, **negativo** o **neutral**. Es ideal para entender cómo los usuarios perciben ciertos temas o tendencias en redes sociales.

---

## Características ✨
- Extracción de datos desde Twitter mediante su API.
- Limpieza y preprocesamiento de texto.
- Clasificación de sentimientos en tiempo real.
- Visualización gráfica de los resultados.
- Manejo automático del límite de solicitudes en la API de Twitter.

---

## Requisitos Previos 🛠️
Antes de comenzar, asegúrate de tener:
1. **Python 3.9 o superior** instalado.
2. **Anaconda** configurado en tu sistema.
3. Credenciales de la API de Twitter:
   - Crea una cuenta en [Twitter Developer](https://developer.twitter.com/) y genera las claves necesarias.
4. Dependencias como `tweepy`, `textblob`, y `matplotlib`.

---

## Instalación ⚙️
Sigue estos pasos para configurar el entorno y las dependencias:

1. **Clona este repositorio:**
   ```bash
   git clone https://github.com/Eigna-atonim1030/Sentiment_analysis_project.git
2. **Comandos que debes ejecutar:**
   Navega al directorio del proyecto:
   cd Sentiment_analysis_project
Crea y activa un entorno virtual:
   conda create -n sentiment_analysis_env python=3.9
   conda activate sentiment_analysis_env
Instala las dependencias necesarias:
   pip install -r requirements.txt
Configura las credenciales de Twitter:
   API_KEY = "123"
   API_SECRET = "123"
   ACCESS_TOKEN = "123"
   ACCESS_TOKEN_SECRET = "123"
Pasos para Ejecutar el Proyecto 🚀
Abrir Anaconda Prompt
Abre Anaconda Prompt desde el menú de inicio de Windows.

2. Activar el entorno
Escribe el siguiente comando para activar tu entorno virtual:
   conda activate sentiment_analysis_env
Esto activará el entorno donde configuraste todas las dependencias necesarias.

3. Navegar a tu carpeta de proyecto
Cambia el directorio a la carpeta donde se encuentra tu archivo twitter_search.py. Por ejemplo:
   cd C:\Users\HP\Documents\sentiment_analysis_project
Asegúrate de que esta sea la ubicación correcta de tu proyecto.

4. Ejecutar el script
Dentro de la carpeta del proyecto, ejecuta el siguiente comando:
   python twitter_search.py
   
El script buscará tweets relacionados con el término "tecnología" y clasificará los resultados por sentimiento (positivo, negativo, neutral).
Nota: Si el script alcanza el límite de solicitudes de la API de Twitter, pausará automáticamente durante 15 minutos antes de continuar. Esto es debido a las limitaciones de la versión gratuita de la API de Twitter.

Tecnologías Usadas 🛠️
Python 3.9
Anaconda: Gestión de entornos y dependencias.
Tweepy: Extracción de datos desde Twitter.
NLTK y TextBlob: Preprocesamiento y análisis de texto.
Matplotlib: Visualización gráfica.

