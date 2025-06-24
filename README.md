# Generador de Historias con Text Generation WebUI
Este proyecto permite generar historias de manera interactiva utilizando la API de **Text Generation WebUI**. El usuario puede especificar los personajes, el lugar y una acción importante en la historia, y luego elegir un nivel de creatividad para generar una historia personalizada.

## Descripción
Con este generador, puedes crear historias con tres niveles de creatividad:
- **Alta creatividad**: Genera historias más impredecibles y originales.
- **Creatividad media**: Genera historias equilibradas, con un buen nivel de coherencia y creatividad.
- **Baja creatividad**: Genera historias más predecibles y formales.

Este proyecto consta de dos partes principales:

1. **Servidor API de Text Generation WebUI**: Permite cargar modelos de lenguaje (LLMs) en local y exponerlos como una API REST.
2. **Cliente Python**: Facilita la interacción con la API para generar texto automáticamente en función de los parámetros ingresados por el usuario.

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado **Python 3.x**: Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

---

## **Instalación**

### 1. Instalar el servidor de Text Generation WebUI

1. **Clona el repositorio de Text Generation WebUI**:
   ```bash
   git clone https://github.com/oobabooga/text-generation-webui
   cd text-generation-webui
   ```
   
2. Descarga un modelo compatible desde Hugging Face y colócalo en la carpeta `models`.

  Ejemplo de modelos:

  - **Llama 2 7B**
  - **GPT Neo 1.3B**
  - **Mistral 7B Instruct**

 3. Inicia el servidor de la API:
  ```bash
  start_windows.bat --api --model Qwen_Qwen2.5-1.5B-Instruct --cpu
  ```
4. Verifica que la API esté disponible en `http://127.0.0.1:5000/docs`.

5. Comprueba que el cliente web que esté disponible en `http://127.0.0.1:7860/`

---

### 2. Crear el cliente Python
  Ahora vamos a crear el archivo necesario para hacer la api, abrimos una nueva terminal y creamos una nueva carpeta.

  Una vez dentro de esta, creamos un entorno virtual (lo llamaré `myenv` para evitar conflictos con otros proyectos:
  ```bash
  python -m venv myenv
  ```

  Después lo activaremos con el comando `.\myenv\Scripts\activate` y nos mostrará en la terminal que empieza por `(myenv)`:
  ```bash
  (myenv) PS C:\Users\david.moreno.cerezo\Documents\prueba_api_gtwui>
  ```

  Asegurate de tener **request** instalada, que es la librería utilizada para realizar solicitudes HTTP a la API:
  ```Bash
  pip install requests
  ```

### 3. Configura el script `.py` cliente para apuntar a la URL de la API (normalmente, http://127.0.0.1:5000), en mi caso apuntará a `http://127.0.0.1:5000/v1/completions`.

---

# Uso de la api

## Ejecución del script

  1. Ejecuta el programa estando dentro del entorno virtual:
     ```bash
     chat.py
     ````
  2. Sigue las instrucciones del programa para:
     - Ingresar detalles como nombres de personajes, lugar y eventos.
     - Seleccionar el nivel de creatividad (alta, media o baja).
     - Generar historias basadas en los datos proporcionados.

---

# Ejemplo 1 con el modelo Qwen_Qwen2.5-1.5B-Instruct
## Entrada:

```python
Hola, conmigo puedes crear una historia en segundos!!!

Especifica los datos de la historia que quieres crear
Nombre del personaje principal: david

Nombre del personaje secundario: cristina

¿En qué lugar se desarrolla esta grandiosa historia? O no, quien sabe...: en una pista de volley

Acción importante que ocurre en la historia: se hacen novios

Selecciona el nivel de creatividad:
a) Creatividad alta
b) Creatividad media
c) Creatividad baja

Elige una opción :b
```
## Salida:
```python
Generando historia...

Ana Itzayán
Cascada de aguas color limón en la repisa de la ventana. La pista de voleibol estaba llena de energía.
David y Kristina se veían eléctricamente. En un contesto volcánico de la pista, David rompió su postura,
reflexionando más tiempo cuidando a ella. Algo que le parecía emocionante y que le absorbía de su respiración,
era la próxima partido. Surfesondeles y lanzarse en el marone que fuera el último. A partir de ahí, David se
quedo dormido. Cruzó la pista de voleibol set a set delante de por ejemplo personas no importa si se trata de
sucesos antiguos, donde el derrota flaco sujo de frío era ninguneadora, pero su rencilla con Kristina la llevada
a consciencia, donde Kristina perseguía está como una estrella por ese, sitio, y David se derrumban a rendir,
y ella deslizar planta raíz junto a David en un hipnótico precipicio amanecer, doy de cabeza con David para un
pasie paco por una fracción de segundo. Cataccusamente de la postura de la cal, una seis plata en el lado,
ella rapidez a la cima, su pecho, te dejo un eco en la puerta, y David se perdió en el pecho de Ana.

Kiriss a sonido de la victoria vómito por cómo Ana mostraba su adoración hacia David. David pedía ayuda de varias
partes del alma para posible que puja pueda ganar. Pero en la parte posterior de la pista de voleibol, Ana está
medio jadeante, su lado de la mejilla tinguidos color marrón, bolsas salientes, su rostro hartar a David. Más aún,
su rostro estaba igual de notable. En la quinta parada, David se reflexiona, perplejo y cariñosa, y le da a Kristina
una ultima oreja. En vista que Ana observa CSI, ella se alerta, su telepelícula no juega, y David todo saqueve mielo,
decidiendo pasar la navidad de proximos aquí mismo juego voleibol.
```

---

# Ejemplo 2 con el modelo Qwen_Qwen2.5-1.5B-Instruct
## Entrada:
![Captura de pantalla 2024-11-29 125556](https://github.com/user-attachments/assets/4aa9a95a-2f98-4ae7-9729-3fc4a6001a1c)

## Salida:
![Captura de pantalla 2024-11-29 125658](https://github.com/user-attachments/assets/ea7f0b35-a9fd-4c43-95ec-56811909c66b)

---

# Ejemplo 3 con el modelo Qwen_Qwen2.5-1.5B-Instruct
## Entrada:
![Captura de pantalla 2024-11-29 131616](https://github.com/user-attachments/assets/241258a2-1431-4398-828d-e7d927fac177)

## Salida:
![Captura de pantalla 2024-11-29 132143](https://github.com/user-attachments/assets/3d041902-d9c8-4836-887d-cb3707670770)

---

# Ejemplo 1 con el modelo gpt-neo-1.3B
## Entrada:
```python
Hola, conmigo puedes crear una historia en segundos!!!

Especifica los datos de la historia que quieres crear
Nombre del presonaje principal: Manolo

Nombre del personaje secundario: Doraemon

¿En qué lugar se desarrolla esta grandiosa historia? O no, quien sabe...: una isla flotante

Acción importante que ocurre en la historia: Crean una civilizacion

Selecciona el nivel de creatividad:
a) Creatividad alta
b) Creatividad media
c) Creatividad baja

Elige una opción :b
```

## Salida:
```python
Generando historia...

Son inclinados a distraer a sus lectores. Recuerdan cosas que dicen en el lib Brazil vs Vera Cruz. Es insípido.
Manolo goza de inmenso respeto. Y Doraemon, se llama Secundario. Tan obsesives se les dirá una cuenta cuando hablen
unos a otros... Manolo se sustenta. Doraemon sabe lo que se antoja. Lo valora la vida. ¿Puedes perjudicarlo?
Perjudica al señor Esteban un miserable monólogo. Pero sobre todo bue. Claro... Saldremos fallecidos. Somos
monstruos, luvis negras inmunes... ¿Por qué no harían daño con las estatuas de terciopelo con thou? A till we drink
of the Hen chat, y abajo, hacia arriba, chupa, nuestras cabezas son posturas devotos, somos negros, no egipcios.
Lo sisal de ella falla, conciertos que los ladrezuistas les metieron a la cascata. Pero ella, más allá de lo que
King kidding. Pero pocas personas tienen cosas así. O te mando a contestar ante quién nos convierte.

whelp, los expolio ’srean. de la misma manera que en Brampton loans que negociaran te. hoy, por el contundio,
no se recivieran entrada en mayo. es asi. pues todo, me digo. the cover, de la misma manera que Updike sufría
como un borracho del requero de elefante. tienen un anzuelo. tienen un anzuelo. porque NO LO HAN PASADO.
porque N FORES LO HAN PASADO.. esto es solo porque no te gracia. Es demasiado. porque los han pasado. en verdad,
hay que reconocer la cosa a los eventos. los han pasado once. para ir con la ansiedad del entorno
```

---

# Ejemplo 2 con el modelo gpt-neo-1.3B
## Entrada:

![Captura de pantalla 2024-11-29 134140](https://github.com/user-attachments/assets/8fde752d-dc9a-4c4f-87e9-222d6efc8907)

## Salida:

![Captura de pantalla 2024-11-29 134154](https://github.com/user-attachments/assets/804ccf2e-17a0-4ae0-90a4-1a7ea177e5d9)

---

# Ejemplo 3 con el modelo gpt-neo-1.3B
## Entrada:
![Captura de pantalla 2024-11-29 140204](https://github.com/user-attachments/assets/c74bdfa4-220d-4862-857b-faeeeabcd239)

## Salida:
![Captura de pantalla 2024-11-29 140215](https://github.com/user-attachments/assets/2d64d696-c542-496a-b26d-ea5acbe8a7c3)

---

# Conclusión
El modelo que mejor a trabajado y a dado mejores historias a sido `Qwen_Qwen2.5-1.5B-Instruct`, aunque en el modo `Creatividad alta` los dos modelos han tabajado de una manera no muy buena. En el modo `Creatividad media` ambos han sacado una historia decente teniendo en cuenta que no son modelos muy potentes.
En el modo que si a sobre salido el modelo `Qwen_Qwen2.5-1.5B-Instruct` a sido en el de `Creatividad baja` sacando una historia bastante buena en comparación con las pruebas anteriores.

He elegido estos modelos porque no pesan mucho, no necesitan unos requisitos altos y con los recursos tengo disponible en mi ordenador han sido posibles ejecutarlos sin problema, ya que probé con otros y por falta de recursos no llegaban a ejecutarse.

---

# Recursos utilizados
   - [Repositorio oficial de Text Generation WebUI](https://github.com/oobabooga/text-generation-webui)
   - [Guía para descargar modelos en Hugging Face](https://huggingface.co/models)
   - [Modelo Qwen_Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
   - [Modelo gpt-neo-1.3B](https://huggingface.co/EleutherAI/gpt-neo-1.3B)

# 📜 Licencia
Este proyecto está licenciado bajo la licencia **CC BY-NC 4.0**. Consulta el archivo [`LICENSE`](https://github.com/DavidMoCe/asistencia/blob/main/LICENSE.txt) para más detalles.

# ❤️ Créditos
Desarrollado por **David Moreno Cerezo**.
