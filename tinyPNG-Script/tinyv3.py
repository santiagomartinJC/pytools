import os
import glob
import datetime
import requests
import sys

# API key es brindada por un argumento de línea de comandos -t o --token
#
# Ejemplo de ejecución: python tinyv3.py . .png .jpg -t m1bwd28QvJC4pmXMLyv6hm9CRr9yk2Vm
#
# Obtener el token de la línea de comandos o muestra mensaje de error
if "-t" in sys.argv or "--token" in sys.argv:
    try:
        api_key = sys.argv[sys.argv.index("-t") + 1]
    except ValueError:
        api_key = sys.argv[sys.argv.index("--token") + 1]

#agregar excepcion si alguno de los argumentos no es valido o falta
else:
    print("Para ejecutar el script es necesario agregar un token de autenticación.")
    sys.exit()

# argv 1 = directorio fuente
# argv 2 = directorio de salida
# argv -t = token de autenticacion
if len(sys.argv) < 4:
    print("Especificar directorio de origen y directorio de destino.")
    # mostrar como usar el script
    print("Ejemplo de uso: python tinyv3.py ./source ./destination -t API_KEY")
    # terminar el script
    sys.exit(1)

# Directorio fuente
directory = sys.argv[1]
# Directorio de salida
#output_directory = sys.argv[2] + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
output_directory = sys.argv[2]


# Contador de archivos
count = 0
# Crear directorio de salida con fecha y hora actual
if not os.path.exists(output_directory):
    os.mkdir(output_directory)
# Extensiones de archivo permitidas
allowed_extensions = (".png", ".jpg")

# Enviar archivos
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.lower().endswith(allowed_extensions):
            count += 1
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            output_path = os.path.join(output_directory, relative_path)
            print(f"Checking...archivo {count}: {file_path}")
            
            if not os.path.exists(output_path):
                print(f"Enviando archivo {count}: {file_path}")

                with open(file_path, "rb") as f:
                    response = requests.post(
                        "https://api.tinify.com/shrink",
                        auth=("api", api_key),
                        headers={"Content-Type": "image/png"},
                        data=f,
                    )
                
                print(response.json())
                
                # Obtener el campo "url" del JSON de respuesta
                output_url = response.json()["output"]["url"]
                print(f"Descargando archivo optimizado: {output_url}")
                
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                with open(output_path, "wb") as f:
                    response = requests.get(output_url, auth=("api", api_key))
                    f.write(response.content)
                
                print("")

print(
    f"¡Todos los archivos se han enviado y descargado con éxito en el directorio {output_directory}!"
)