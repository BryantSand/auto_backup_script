import os
import shutil
from datetime import datetime

# Configuración
origen = "test_folder"
destino = "respaldo"

# Crear carpeta de respaldo si no existe
if not os.path.exists(destino):
    os.makedirs(destino)

# Crear subcarpeta con timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
destino_final = os.path.join(destino, f"respaldo_{timestamp}")
os.makedirs(destino_final)

# Copiar archivos
for archivo in os.listdir(origen):
    ruta_archivo = os.path.join(origen, archivo)
    if os.path.isfile(ruta_archivo):
        shutil.copy2(ruta_archivo, destino_final)

print(f"Respaldo completado en {destino_final}")
