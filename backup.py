import os
import shutil
import time
import threading
import signal
import sys
from tqdm import tqdm

detener_evento = threading.Event()

def log(message):
    with open("backup.log", "a") as log_file:
        log_file.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")

def cancelar_si_q(entrada):
    if entrada.lower() == "q":
        print("⛔ Operación cancelada por el usuario.")
        log("El usuario canceló el proceso.")
        sys.exit()

def choose_interval():
    respuesta = input("¿Deseas hacer respaldos automáticos? (s/n o 'q' para salir): ").strip().lower()
    cancelar_si_q(respuesta)
    if respuesta == "s":
        while True:
            entrada = input("¿Cada cuántos minutos deseas hacer el respaldo? ('q' para salir): ")
            cancelar_si_q(entrada)
            try:
                intervalo = int(entrada)
                return intervalo * 60
            except ValueError:
                print("Por favor, ingresa un número válido.")
    return None

def get_folder_path(prompt):
    while True:
        path = input(prompt + " ('q' para salir): ").strip('"')
        cancelar_si_q(path)
        if os.path.isdir(path):
            return path
        print("La carpeta no existe. Intenta de nuevo.")

def create_or_choose_backup_folder():
    usar_existente = input("¿Deseas usar una carpeta de destino existente? (s/n o 'q' para salir): ").strip().lower()
    cancelar_si_q(usar_existente)
    if usar_existente == "s":
        return get_folder_path("Ingresa la ruta de la carpeta destino")
    else:
        while True:
            disco = input("¿En qué disco deseas crear la carpeta? (ej. D o 'q' para salir): ").upper()
            cancelar_si_q(disco)
            nombre = input("Nombre para la nueva carpeta: ('q' para salir): ")
            cancelar_si_q(nombre)
            nueva_ruta = f"{disco}:/Respaldo_{nombre}"
            try:
                os.makedirs(nueva_ruta, exist_ok=True)
                print(f"📁 Carpeta creada en {nueva_ruta}")
                return nueva_ruta
            except Exception as e:
                print(f"⚠️ Error al crear la carpeta: {e}")

def copy_with_progress(source, destination):
    files = [f for f in os.listdir(source) if os.path.isfile(os.path.join(source, f))]
    total = len(files)
    with tqdm(total=total, desc="Respaldo en progreso", unit="archivo") as pbar:
        for file in files:
            if detener_evento.is_set():
                print("⛔ Respaldo cancelado.")
                break
            src_file = os.path.join(source, file)
            dst_file = os.path.join(destination, file)
            try:
                shutil.copy2(src_file, dst_file)
                log(f"Copiado: {file}")
            except Exception as e:
                log(f"Error copiando {file}: {e}")
            pbar.update(1)

def ejecutar_respaldo(origen, destino):
    print("\n🚀 Iniciando respaldo...")
    copy_with_progress(origen, destino)
    print("✅ Respaldo completado.\n")

def respaldo_automatico(origen, destino, intervalo):
    try:
        while not detener_evento.is_set():
            ejecutar_respaldo(origen, destino)
            for _ in range(intervalo):
                if detener_evento.is_set():
                    break
                time.sleep(1)
    except Exception as e:
        log(f"Error en respaldo automático: {e}")

def monitor_entrada_usuario():
    while not detener_evento.is_set():
        comando = input("> Escribe 'stop' para detener el respaldo automático: ").strip().lower()
        if comando == "stop":
            detener_evento.set()
            print("⛔ Respaldo automático detenido por el usuario.")
            log("Respaldo automático detenido por comando 'stop'.")
            break

def main():
    print("🛡️ Script de Respaldo Automático")
    print("Presiona 'q' en cualquier momento para salir.\n")

    intervalo = choose_interval()
    origen = get_folder_path("Ingresa la ruta de la carpeta origen")
    destino = create_or_choose_backup_folder()

    if intervalo:
        segundo_plano = input("¿Deseas ejecutar el respaldo automático en segundo plano? (s/n): ").strip().lower()
        if segundo_plano == "s":
            print("\n🔁 Respaldo automático iniciado en segundo plano. Escribe 'stop' para detener.")
            log("Inicio de respaldo automático en segundo plano.")
            thread_respaldo = threading.Thread(target=respaldo_automatico, args=(origen, destino, intervalo))
            thread_respaldo.start()

            # Escucha comandos del usuario mientras el respaldo corre
            monitor_entrada_usuario()

            thread_respaldo.join()
        else:
            print(f"\n🔁 Respaldo automático cada {intervalo // 60} minutos. Presiona Ctrl + C para detener.")
            log("Inicio de respaldo automático en primer plano.")
            respaldo_automatico(origen, destino, intervalo)
    else:
        ejecutar_respaldo(origen, destino)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, lambda sig, frame: detener_evento.set())
    main()

