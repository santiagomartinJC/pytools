import os
import sys
# ejemplo de ejecucion: python count-files-in.py . .png .jpg .txt

def count_files_with_extensions(directory, extensions):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                count += 1
    return count

# Directorio actual
directory = sys.argv[1]

# Extensiones de archivo permitidas
# extensions = [".png", ".jpg"]
# obtener extensiones de archivo de la línea de comandos
extensions = sys.argv[2:] 

# Contar archivos con extensiones especificadas
total_files = count_files_with_extensions(directory, extensions)
print(f"Total de archivos con extensiones {extensions}: {total_files}")
