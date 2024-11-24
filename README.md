# 🎯 Sentiment Analysis Project

Un proyecto para analizar sentimientos en redes sociales utilizando Python, Anaconda y procesamiento de lenguaje natural (NLP).

## 📑 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características](#-características)
- [Requisitos Previos](#️-requisitos-previos)
- [Instalación](#️-instalación)
- [Pasos para Ejecutar el Proyecto](#-pasos-para-ejecutar-el-proyecto)
- [Tecnologías Usadas](#️-tecnologías-usadas)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

## 📝 Descripción

El proyecto **Sentiment Analysis Project** permite analizar los sentimientos de los tweets extraídos de Twitter, clasificándolos como **positivos**, **negativos** o **neutrales**. Este proyecto es ideal para entender la percepción del público sobre temas específicos o tendencias en redes sociales.

## ✨ Características

- Extracción de datos en tiempo real desde la API de Twitter
- Limpieza y preprocesamiento del texto
- Clasificación de sentimientos
- Visualización gráfica de los resultados
- Manejo automático de límites de solicitudes de la API de Twitter

## 🛠️ Requisitos Previos

Asegúrate de tener lo siguiente instalado y configurado antes de comenzar:

1. **Python 3.9 o superior**
2. **Anaconda**
3. Una cuenta en [Twitter Developer](https://developer.twitter.com/) con acceso a las claves de API:
   - API Key
   - API Secret
   - Access Token
   - Access Token Secret
4. Dependencias necesarias:
   - `tweepy`
   - `textblob`
   - `matplotlib`

## ⚙️ Instalación

Sigue los pasos a continuación para configurar el entorno y preparar el proyecto:

### 1. Clonar el repositorio:
```bash
git clone https://github.com/Eigna-atonim1030/Sentiment_analysis_project.git
```

### 2. Navegar al directorio del proyecto:
```bash
cd Sentiment_analysis_project
```

### 3. Crear y activar un entorno virtual:
```bash
conda create -n sentiment_analysis_env python=3.9
conda activate sentiment_analysis_env
```

### 4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 5. Configurar las credenciales de Twitter:

Crea un archivo `.env` en la raíz del proyecto y añade las credenciales de la API:
```env
API_KEY=tu_api_key
API_SECRET=tu_api_secret
ACCESS_TOKEN=tu_access_token
ACCESS_TOKEN_SECRET=tu_access_token_secret
```

## 🚀 Pasos para Ejecutar el Proyecto

Sigue estas instrucciones para ejecutar el proyecto:

### 1. Abrir Anaconda Prompt
Abre Anaconda Prompt desde el menú de inicio de Windows.

### 2. Activar el entorno:
```bash
conda activate sentiment_analysis_env
```

### 3. Navegar a tu carpeta de proyecto
```bash
cd C:\Users\HP\Documents\sentiment_analysis_project
```

### 4. Ejecutar el script:
```bash
python twitter_search.py
```

El script buscará tweets relacionados con el término "tecnología" y los clasificará como positivos, negativos o neutrales.

**Nota**: Si la API alcanza su límite de solicitudes, el script pausará automáticamente durante 15 minutos antes de continuar.

## 🛠️ Tecnologías Usadas

- Python 3.9
- Anaconda: Gestión de entornos y dependencias
- Tweepy: Extracción de datos desde Twitter
- NLTK y TextBlob: Preprocesamiento y análisis de texto
- Matplotlib: Visualización gráfica de los resultados

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, lea las directrices de contribución antes de enviar un pull request.

## 📜 Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.
