import threading
import time

numero = 0
def procesar_datos(origen, destino, delay=1):
    global numero
    """Función que simula un procesamiento de datos."""
    print(f"[Hilo] Procesando datos desde {origen} hacia {destino}...")
    #time.sleep(delay) cambio el sleep por un for pq cuando llega al sleep echa al proceso, quiero que le deje trabajando
    aux = 0
    for _ in range(10000):
        aux +=1

    numero += 200
    print(f"[Hilo] Procesamiento terminado. Número: {numero}")

if __name__ == "__main__":
    # args debe ser siempre una tupla (aunque sea de un solo elemento)
    argumentos_posicionales = ("servidor_A", "servidor_B")
    
    # kwargs se pasa como diccionario
    argumentos_con_nombre = {"delay": 2}

    hilo = threading.Thread(
        target=procesar_datos,
        args=argumentos_posicionales,
        kwargs=argumentos_con_nombre,
        name="HiloProcesamiento"
    )

    print("[Principal] Lanzando hilo...")
    hilo.start()
    #le pongo otro for tmbn
    aux = 0
    for _ in range(10000):
        aux +=1
    


    numero += 500
    print(f"[Principal] Esperando a que termine... DE MOMENTO NUMERO VALE {numero}")
    hilo.join()
    print(f"Todo terminado, ahora numero es: {numero}")