import requests
import json

#http://192.168.1.200/wordpress/index.php/wp-json/wp/v2/posts
wp_url = "http://192.168.1.200/wordpress/index.php/"
wp_user = "test"
wp_pass = "test123456"
wp_api_url = "/wp-json/wp/v2"

def create_post(post_data):
    
    #Paso 1: Autenticar con WordPress REST API
    auth = requests.auth.HTTPBasicAuth(wp_user, wp_pass)

    #Paso 2: enviar un POST request para crear un nuevo artículo
    posts_url = f"{wp_url}{wp_api_url}/posts"
    try:

        response = requests.post(
            posts_url,
            data = json.dumps(post_data),
            headers = {"Content-Type": "application/json"},
            auth = auth
        )

    except Exception as e:
        response = None

    return response

#Armar el post data
titulo = "prueba publicando en WP a través de la API"
contenido = "<h1>este es un título de prueba</h1> <p>párrafo después del titulo</p>"

post_data = {
    'title': titulo,
    'content': contenido,
    'status': 'draft', #borrador
    'categories': [1], #esta es una lista con los ID's de las categorías
    'tags': [1], #esta es una lista con los ID's de las etiquetas
    'slug': 'prueba-publicando-en-wp-via-api', #esto es como se formará la URL de la entrada en WP
}

response = create_post(post_data)
print(response)