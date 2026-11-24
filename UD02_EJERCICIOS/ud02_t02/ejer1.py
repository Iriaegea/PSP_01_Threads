# Crear un hilo cuyo método run() deberá dormirlo durante unos 2000 milisegundos 
# (el cuerpo del método irá encerrado en un bloque try… catch (una excepción).
# Luego en el programa principal quiero que me muestres el estado del hilo antes 
# de ejecutarse (indicará false) y durante su ejecución (indicará que está vivo, 
# true). Luego con el método join() esperaremos a que el hilo muera y se mostrará 
# su estado (deberá estar muerto, false).
# El método hilo.is_alive() me dice cuál es el estado del hilo.

import threading
import time

class miHilo(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        try:
            time.sleep(2) # * 1000
        except Exception:
            print(f"Error")


        

if __name__ == "__main__":
    

    hilo = miHilo()

    print(f"Estado del hilo antes de ejecutarse: {hilo.is_alive()}" )
    hilo.start()
   
    print(f"Estado del hilo en ejecucion: {hilo.is_alive()}" )
    hilo.join()
    print(f"Estado del hilo al terminar de ejecutarse: {hilo.is_alive()} ")


    