#Vamos a ver como una variable “contador” no funciona correctamente debido a
#  que se accede concurrentemente a una misma zona de memoria 
# sin que se produzca exclusión mutua (esto intentaremos solucionarlo más 
# adelante cuando se 
# trate el sincronismo de los hilos).
# Crea una subclase Thread la cual tendrá un único atributo que será una
# cadena; como métodos: se redefine su constructor pasándole un string 
# como argumento, se llama al constructor de la superclase, se le asigna
#  al atributo de objeto como valor el del string pasado como argumento.

# En el programa principal crea 2 objetos de tu subclase Thread (2 hilos) 
# cada uno con un valor, por ejemplo, el hilo1 con SI y el hilo2 con NO; y
# una variable global contador inicializada a cero. 

# El método run() de cada hilo mostrará hasta un máximo de 10 veces el valor
# de contador incrementado y luego el valor del atributo string

import threading

contador = 0

class miHilo(threading.Thread):
    def __init__(self, cadena):
        super().__init__()
        self.cadena = cadena

    def run(self):
        global contador
        for _ in range(10):
            contador +=1
            print(contador)
            print(self.cadena)

        

if __name__ == "__main__":
    hilo1 = miHilo("SI")
    hilo2 = miHilo("NO")
    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

