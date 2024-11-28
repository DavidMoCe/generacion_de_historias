# Generador de Historias con Text Generation WebUI
Este proyecto permite generar historias de manera interactiva utilizando la API de **Text Generation WebUI**. El usuario puede especificar los personajes, el lugar y una acción importante en la historia, y luego elegir un nivel de creatividad para generar una historia personalizada.

## Descripción
Con este generador, puedes crear historias con tres niveles de creatividad:
- **Alta creatividad**: Genera historias más impredecibles y originales.
- **Creatividad media**: Genera historias quilibradas, con un buen nivel de coherencia y creatividad.
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

# Ejemplo con el modelo Qwen_Qwen2.5-1.5B-Instruct
## Entrada:

```python
Hola, conmigo puedes crear una historia en segundos!!!

Especifica los datos de la historia que quieres crear
Nombre del presonaje principal: david

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
Cascada de aguas color limón en la repisa de la ventana. La pista de voleibol estaba llena de energía. David y Kristina se veían eléctricamente. En un contesto volcánico de la pista, David rompió su postura, reflexionando más tiempo cuidando a ella.
Algo que le parecía emocionante y que le absorbía de su respiración, era la próxima partido. Surfesondeles y lanzarse en el marone que fuera el último. A partir de ahí, David se quedo dormido. Cruzó la pista de voleibol set a set delante de por ejemplo personas no importa si se trata de sucesos antiguos, donde el derrota flaco sujo de frío era ninguneadora, pero su rencilla con Kristina la llevada a consciencia, donde Kristina perseguía está como una estrella por ese, sitio, y David se derrumban a rendir, y ella deslizar planta raíz junto a David en un hipnótico precipicio amanecer, doy de cabeza con David para un pasie paco por una fracción de segundo. Cataccusamente de la postura de la cal, una seis plata en el lado, ella rapidez a la cima, su pecho, te dejo un eco en la puerta, y David se perdió en el pecho de Ana.

Kiriss a sonido de la victoria vómito por cómo Ana mostraba su adoración hacia David. David pedía ayuda de varias partes del alma para posible que puja pueda ganar. Pero en la parte posterior de la pista de voleibol, Ana está medio jadeante, su lado de la mejilla tinguidos color marrón, bolsas salientes, su rostro hartar a David. Más aún, su rostro estaba igual de notable. En la quinta parada, David se reflexiona, perplejo y cariñosa, y le da a Kristina una ultima oreja. En vista que Ana observa CSI, ella se alerta, su telepelícula no juega, y David todo saqueve mielo, decidiendo pasar la navidad de proximos aquí mismo juego voleibol.
```

---

# Ejemplo con el modelo gpt-neo-1.3B
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

Son inclinados a distraer a sus lectores. Recuerdan cosas que dicen en el lib Brazil vs Vera Cruz. Es insípido. Manolo goza de inmenso respeto. Y Doraemon, se llama Secundario. Tan obsesives se les dirá una cuenta cuando hablen unos a otros... Manolo se sustenta. Doraemon sabe lo que se antoja. Lo valora la vida. ¿Puedes perjudicarlo? Perjudica al señor Esteban un miserable monólogo. Pero sobre todo bue. Claro... Saldremos fallecidos. Somos monstruos, luvis negras inmunes... ¿Por qué no harían daño con las estatuas de terciopelo con thou? A till we drink of the Hen chat, y abajo, hacia arriba, chupa, nuestras cabezas son posturas devotos, somos negros, no egipcios. Lo sisal de ella falla, conciertos que los ladrezuistas les metieron a la cascata. Pero ella, más allá de lo que King kidding. Pero pocas personas tienen cosas así. O te mando a contestar ante quién nos convierte.

whelp, los expolio ’srean. de la misma manera que en Brampton loans que negociaran te. hoy, por el contundio, no se recivieran entrada en mayo. es asi. pues todo, me digo. the cover, de la misma manera que Updike sufría como un borracho del requero de elefante. tienen un anzuelo. tienen un anzuelo. porque NO LO HAN PASADO. porque N FORES LO HAN PASADO.. esto es solo porque no te gracia. Es demasiado. porque los han pasado. en verdad, hay que reconocer la cosa a los eventos. los han pasado once. para ir con la ansiedad del entorno
```

---

# Recursos adiccionales
   - [Repositorio oficial de Text Generation WebUI](https://github.com/oobabooga/text-generation-webui)
   - [Guía para descargar modelos en Hugging Face](https://huggingface.co/models)
   - [Modelo Qwen_Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
   - [Modelo gpt-neo-1.3B](https://huggingface.co/EleutherAI/gpt-neo-1.3B)
   - 
