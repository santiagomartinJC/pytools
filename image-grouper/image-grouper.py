import os
import shutil
import datetime
import sys

#example of use: python image-grouper.py ./source ./destination 10
#where:
#  10 is the group size
#   ./source is the source directory
#   ./destination is the destination directory

def group_images(source_dir, dest_dir, group_size):
    # Crear directorio de salida con fecha y hora actual
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_directory = os.path.join(dest_dir, f"split-group-{current_time}")
    os.makedirs(output_directory, exist_ok=True)

    count = 0
    group_count = 1
    current_group_directory = os.path.join(output_directory, f"group-{group_count}")
    os.makedirs(current_group_directory, exist_ok=True)

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith((".jpg", ".png")):
                source_path = os.path.join(root, file)
                relative_path = os.path.relpath(source_path, source_dir)
                output_path = os.path.join(current_group_directory, relative_path)

                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                shutil.copy2(source_path, output_path)

                count += 1
                if count >= group_size:
                    group_count += 1
                    current_group_directory = os.path.join(output_directory, f"group-{group_count}")
                    os.makedirs(current_group_directory, exist_ok=True)
                    count = 0

    print(f"Se agruparon las imágenes en: {output_directory}")


#add __main__ to the script to make it executable 
#as a standalone program 
#(without the need to import it from another script)
if __name__ == "__main__":
    
    # Verificar que se hayan especificado los argumentos de línea de comandos
    if len(sys.argv) < 4:
        print("Especificar directorio de origen, directorio de destino y tamaño máximo del grupo de imágenes.")
        # mostrar como usar el script
        print("Ejemplo de uso: python image-grouper.py ./source ./destination 10")
        # terminar el script
        sys.exit(1)
    # Verificar que el directorio de origen exista
    if not os.path.exists(sys.argv[1]):
        print("El directorio de origen no existe.")
        sys.exit(2)


    # Directorio de origen y destino a partir de los argumentos de línea de comandos
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2]

    # Tamaño máximo del grupo de imágenes convertido a entero a partir de los argumentos de línea de comandos
    group_size = int(sys.argv[3])

    # Ejecutar la función para agrupar las imágenes
    group_images(source_directory, destination_directory, group_size)
