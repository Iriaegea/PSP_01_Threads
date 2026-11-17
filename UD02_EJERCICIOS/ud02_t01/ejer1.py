# Crea un hilo que en su método run() muestre un “NO” hasta un máximo de 
# 30 veces. En el método principal, mostrará “YES” hasta un máximo de 30 
# veces.
# Como salida obtendrás una serie alternativa de NOes YESes ya que una vez
# iniciada la ejecución del thread, el tiempo de la CPU se reparte entre 
# todos los procesos y threads del sistema, con lo cual se intercalan 
# instrucciones del método main() con instrucciones del método run().

import threading

class MiHilo(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for _ in range(30):
            print("NO")


if __name__ == "__main__":
    miHilo = MiHilo()
    miHilo.start()

    for _ in range(30):
        print("YES")

    miHilo.join()


    



