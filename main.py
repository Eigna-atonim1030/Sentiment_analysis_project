import tweepy

# Tus claves de la API de Twitter
API_KEY = "RyqyHKugkdj8HRhH4uj0P0jde"
API_SECRET = "VG7x3ErEOyHHGkeHVjsTxBmjwYVAXEiIyIbelaY0iMfO9zyIcp"
ACCESS_TOKEN = "1859763089887145984-yOct34HHEXES2WxGPFbiovx9F1ldwS"
ACCESS_TOKEN_SECRET = "eJed6DLmC4ANrZ89Nd91Mkcvxrw9vli1r9vIn1qQzApsh"

# Autenticación con la API de Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Prueba de conexión
try:
    api.verify_credentials()
    print("¡Autenticación exitosa!")
except Exception as e:
    print(f"Error durante la autenticación: {e}")