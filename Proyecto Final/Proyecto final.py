from pip._vendor import requests
import pandas as pd
from IPython.display import display


API_Key = 'fa22ce807a3a6f2cd28dded3f82ce820'
ciudad = input("Ingrese el nombre de la ciudad: ")

direccion_url = f"https://api.openweathermap.org/data/2.5/weather?appid={API_Key}&q={ciudad}"

datos1 = requests.get(direccion_url)

if datos1.status_code == 200:
    datos_de_clima = datos1.json()

    
    datos_clima_simplificados = {
        'Ciudad': datos_de_clima['name'],
        'Coordenasdas': datos_de_clima['coord'],
        'País': datos_de_clima['sys']['country'],
        'Velocidad del viento': datos_de_clima['wind']['speed'],
        'Temperatura (°C)': datos_de_clima['main']['temp'] - 273.15, # Convertir de Kelvin a Celsius
        'Humedad (%)': datos_de_clima['main']['humidity'],
        'Descripción': datos_de_clima['weather'][0]['description'],
    }

    # Crear DataFrame
    df = pd.DataFrame([datos_clima_simplificados])
    display(df)
    print(df.shape)
else:
    print(f"Error: {datos1.status_code}")
    print(datos1.text)