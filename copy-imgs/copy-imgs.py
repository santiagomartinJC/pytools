import os
import sys
import shutil
import datetime

def copy_imgs(source_dir, destination_dir):
    # Generar un nombre de carpeta único basado en la fecha y hora actual
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    dest_folder = os.path.join(destination_dir, "img-copy-" + timestamp)
    
    # Crear la carpeta de destino si no existe
    os.makedirs(dest_folder, exist_ok=True)
    
    # Recorrer todos los archivos y carpetas dentro del directorio fuente
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Verificar si el archivo es una imagen (png, jpg)
            if file.lower().endswith(('.png', '.jpg')):
                # Construir la ruta de origen y destino para cada imagen
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_folder, os.path.relpath(src_path, source_dir))
                
                # Crear la estructura de carpetas de destino si no existe
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                
                # Copiar la imagen al destino
                shutil.copy(src_path, dest_path)
                print(f"Copiando {src_path} a {dest_path}")
    
    print("Copia de imágenes completada.")


# Obtener los directorios de origen y destino de los argumentos de línea de comandos
source_dir = sys.argv[1]
destination_dir = sys.argv[2]

# Llamar a la función para copiar las imágenes
copy_imgs(source_dir, destination_dir)


