# Vamos a hacer un programa similar al anterior pero instanciando 2 
# threads.
# En el HiloA mostrará el mensaje NO, hasta un máximo de 30 veces
# En el HiloB mostrará el mensaje YES, hasta un máximo de 30 veces
# En el programa principal mostrará un mensaje “Ejecución en HiloA” 
# y se ejecutará el HiloA; luego mostrará un mensaje “Ejecución en 
# HiloB” y se ejecutará el HiloB; y luego un mensaje “Ejecución en 
# main”. A continuación se muestran varias salidas de diferentes 
# ejecuciones:

import threading
class MiHilo(threading.Thread):
    def __init__(self, texto):
        super().__init__()
        self.texto = texto


    def run(self):
        for _ in range(30):
            print(self.texto)



if __name__ == "__main__":
    print("Ejecucion en hilo a...")
    hiloA = MiHilo("NO")
    hiloA.start()

    print("Ejecucion en hilo b...")
    hiloB = MiHilo("SI")
    hiloB.start()

    print("Ejecución en main...")


    hiloA.join()
    hiloB.join()




