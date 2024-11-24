import tweepy
import re
import time
from textblob import TextBlob  # Importar TextBlob para el análisis de sentimientos

# api_key = "RyqyHKugkdj8HRhH4uj0P0jde"
# api_secret = "VG7x3ErEOyHHGkeHVjsTxBmjwYVAXEiIyIbelaY0iMfO9zyIcp"
# bearer_token = "AAAAAAAAAAAAAAAAAAAAANVwxAEAAAAAKMCobdPIHT%2F7t3yCNIegF0Dm%2F5E%3DXSMAcSsqbRuJvlwaw2VkVKudrhi7jwoS5BTFFrEF550eSEysGb"

api_key = "5JSnxSpa7kKXqVjyrYjcvoqml"
api_secret = "an4kjcGZekNDM7LLSPWQP5CiMOaA9DcsBfmQOTzcbO9jbOX65p"
bearer_token = "AAAAAAAAAAAAAAAAAAAAALCfxAEAAAAAl2fT1S5GFByrDzJVp8YAp5oHA38%3D91o2neLHubSRnlgB6iQqzNaLzJhPawRu7HKmuEp0cfgT9J7DM6"

# Autenticación con Bearer Token
client = tweepy.Client(bearer_token)

# Función para analizar el sentimiento de un texto
def analizar_sentimiento(texto):
    analisis = TextBlob(texto)
    polaridad = analisis.sentiment.polarity
    if polaridad > 0:
        return "Positivo"
    elif polaridad < 0:
        return "Negativo"
    else:
        return "Neutral"

# Función principal para buscar y analizar tweets
def buscar_tweets(query, max_results=10, max_solicitudes=3):
    solicitudes_realizadas = 0
    try:
        while solicitudes_realizadas < max_solicitudes:
            print(f"Realizando solicitud {solicitudes_realizadas + 1} de {max_solicitudes}...")
            response = client.search_recent_tweets(query=query, max_results=max_results)

            if response.data:
                for tweet in response.data:
                    texto_original = tweet.text  # Obtén el texto original del tweet
                    sentimiento = analizar_sentimiento(texto_original)
                    print(f"Tweet original: {texto_original}\nSentimiento: {sentimiento}\n")
                solicitudes_realizadas += 1
                time.sleep(15)  # Pausar 15 segundos entre solicitudes
            else:
                print("No se encontraron tweets.")
                break
    except tweepy.TooManyRequests:
        print("Límite alcanzado. Pausando 15 minutos...")
        time.sleep(900)  # Pausa de 15 minutos
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Ejecutar la búsqueda
if __name__ == "__main__":
    buscar_tweets(query="tecnologia", max_results=10, max_solicitudes=2)