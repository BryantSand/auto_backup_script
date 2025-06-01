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
