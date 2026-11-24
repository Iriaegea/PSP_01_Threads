import threading
import time

#el id no hace falta
class miHilo():
    def __init__(self, nombre):
        super().__init__(name=nombre)  #si hay que trabajar con el nombre se pone por ahí
    def run(self):
        print(f"Ejecutando el hilo{self.name}...")
        for i in range(1, 100):
            print(f"Valor desde el hilo con ident {self.ident}: {i}")
            time.sleep(0.1)


