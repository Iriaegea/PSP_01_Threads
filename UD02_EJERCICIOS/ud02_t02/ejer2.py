import threading
import time
import random
# usar time.perf_counter()
inicio = 0
class miHilo(threading.Thread):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

    def run(self):
        try:
            milisg = random.uniform(0, 10)
            print(f"El hilo {self.nombre} va a estar dormido durante {milisg} milisegundos")
            time.sleep(milisg)
        except  Exception:
            print("Error")

        print(f"Hilo {self.nombre} ha despertado")

        

       


if __name__ == "__main__":
    hilo1 = miHilo("hilo1")
    hilo2 = miHilo("hilo2")
    hilo3 = miHilo("hilo3")

    print(f"Iniciando subprocesos...")
    hilo1.run()
    hilo2.run()
    hilo3.run()

    hilo1.join()
    hilo2.join()
    hilo3.join()
   




