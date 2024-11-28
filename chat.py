import requests
import json

url = "http://127.0.0.1:5000/v1/completions"
headers = {"Content-Type": "application/json"}

# Funcion para crear la historia
def datos_historia():
    print("\nEspecifica los datos de la historia que quieres crear")
    personaje_principal = input("Nombre del presonaje principal: ")
    personaje_secundario = input("\nNombre del personaje secundario: ")
    lugar_historia = input("\n¿En qué lugar se desarrolla esta grandiosa historia? O no, quien sabe...: ")
    accion_importante = input("\nAcción importante que ocurre en la historia: ")

    return personaje_principal, personaje_secundario, lugar_historia, accion_importante

# Funcion para seleccionar la creatividad
def nivel_creatividad():
    print("\nSelecciona el nivel de creatividad:")
    print("a) Creatividad alta")
    print("b) Creatividad media")
    print("c) Creatividad baja")
    
    nivel = input("\nElige una opción :").strip().lower()
    if nivel == "a":
        return 1.5
    elif nivel == "b":
        return 1.0
    elif nivel == "c":
        return 0.5
    else:
        print("Opción inválida. Se usará creatividad media por defecto.")
        return 1.0


def crear_historia(prompt, creatividad):
    body = {
        "prompt": prompt,
        "max_tokens": 512,
        "temperature": creatividad 
    }
    try:
        response = requests.post(url=url, headers=headers, json=body)
        if response.status_code == 200:
            historia = response.json()["choices"][0]["text"]
            return historia.strip()
        else:
            print("Error en la solicitud:", response.status_code, response.text)
            return None

    except requests.exceptions.RequestException as e:
        print("Error en la solicitud:", e)
        return None


print("Hola, conmigo puedes crear una historia en segundos!!!")
while True:
    # Obtener detalles de la historia
    personaje_principal, personaje_secundario, lugar, accion_importante = datos_historia()

    # Seleccionar creatividad
    creatividad = nivel_creatividad()

    # Crear el prompt
    prompt = (
        f"Escribe una historia emocionante donde {personaje_principal} sea el personaje principal y {personaje_secundario} el secundario. La historia ocurre en {lugar}, y en algún momento, ocurre lo siguiente: {accion_importante}. Usa un estilo detallado y creativo."
    )

    print("\nGenerando historia...\n")
    historia = crear_historia(prompt, creatividad)
    print(historia)
    # Preguntar si se quiere generar otra historia
    continuar = input("\n¿Quieres generar otra historia? (s/n): ").strip().lower()
    if continuar != "s":
        print("¡Espero que te hayan gustado las historias! O...no, me da igual")
        break
