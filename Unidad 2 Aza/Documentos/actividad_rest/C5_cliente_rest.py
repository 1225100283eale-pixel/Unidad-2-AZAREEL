import requests

def obtener_clima(latitud, longitud):
    url = "https://api.open-meteo.com/v1/forecast"

    parametros = {
        "latitude": latitud,
        "longitude": longitud,
        "current": "temperature_2m,wind_speed_10m"
    }

    r = requests.get(
        url,
        params=parametros,
        timeout=10
    )

    r.raise_for_status()

    return r.json()["current"]


# Tres ciudades
ciudades = {
    "Querétaro": (20.59, -100.39),
    "Ciudad de México": (19.43, -99.13),
    "Guanajuato": (21.02, -101.25)
}

print("CLIMA ACTUAL")
print("-" * 50)

for ciudad, coordenadas in ciudades.items():
    try:
        clima = obtener_clima(coordenadas[0], coordenadas[1])

        print(
            f"{ciudad}: "
            f"Temperatura = {clima['temperature_2m']} °C | "
            f"Viento = {clima['wind_speed_10m']} km/h"
        )

    except requests.exceptions.RequestException as e:
        print(f"{ciudad}: Error de conexión - {e}")
print("Edgar Azareel Loyola Espinola")