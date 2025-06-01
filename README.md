# 🛡️ Auto Backup Script

Script de respaldo automático y manual de carpetas, con barra de progreso, ejecución en segundo plano y cancelación interactiva. Compatible con **Windows**, **Linux** y **macOS**.

---

## 🚀 Funcionalidades

✅ Respaldo **manual** o **automático** cada N minutos  
✅ Opción de **ejecutar en segundo plano** para liberar la terminal  
✅ Comando `stop` para cancelar el respaldo automático  
✅ Elección de **carpeta de origen** y **destino**  
✅ Crea carpeta destino si no existe  
✅ Compatible con rutas de **Windows o Linux**  
✅ Barra de progreso visual con `tqdm`  
✅ Registro de actividad en `backup.log`  
✅ Control de cancelación con la tecla `q`  

---

## 📦 Requisitos

- Python 3.7 o superior
- Biblioteca `tqdm`

Instalación:
```bash
pip install tqdm
```
🧪 Cómo usar

python auto_backup.py

-Sigue las instrucciones en pantalla:  
-Elige si deseas respaldo automático o manual.  
-Especifica la carpeta de origen.  
-Elige usar una carpeta existente o crear una nueva para los respaldos.  
-Si usas modo automático, puedes:  
  Ejecutarlo en segundo plano.  
  Escribir stop en cualquier momento para cancelarlo.  
    
Registro de actividad  

Todas las operaciones se registran en el archivo:

    backup.log

Incluye:  
-Fecha y hora de cada respaldo  
-Archivos respaldados  
-Errores si los hubo

⚠️ Notas  
-En Linux o macOS, si se desea crear carpetas fuera del directorio del usuario (/), puede requerir permisos (sudo).  
-El script se puede mejorar fácilmente para programarse con cron o el programador de tareas de Windows si se desea automatizar aún más.


👨‍💻 Autor  
Bryan Sandoya  
Ingeniero en Electrónica y Comunicaciones  
Magister en Tecnologías de la Información y Seguridad


