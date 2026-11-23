import threading


class miHilo(threading.Thread):
    def __init__(self, comienzo, fin, nombre):
        super().__init__()
        self.comienzo = comienzo
        self.fin = fin
        self.nombre = nombre

    def run(self):
        print(f"Ejecutando {self.nombre}")
        for n in range(self.comienzo, self.fin):
            print(f"{self.nombre} dice: {n}")

        print(f"{self.nombre} teminado")



if __name__ == "__main__":
    hilo1 = miHilo(1, 11, "ThreadA")
    hilo2 = miHilo(20, 31, "ThreadB")

    print("Vamos a iniciar los dos hilos: ")


    hilo1.start()
    hilo2.start()
    print("Hilos inicializados")

    hilo1.join()
    hilo2.join()
    print("Programa finalizado")


