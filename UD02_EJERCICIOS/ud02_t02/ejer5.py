import threading


resultado = 1
class factorial(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.numero = numero

    def run(self):
        
        if(numero == 0):
            print(f"factorial({self.numero}) = 1")
        else:
             print(f"factorial({self.numero}) = {self.numero* {factorial()} }")
    def factorial(self):
         global resultado
         arrayNumerosAnteriores = [num for num in range(1, self.numero-1)]
         arrayResultado= list(map(lambda n: n*self.numero, arrayNumerosAnteriores))

         for pos, n in enumerate(arrayResultado):

            if pos != len(arrayResultado):
                resultado = resultado * (n*(n+1))
            
                 
            
              
        #  resultado = list(map(lambda n : n* n+1 if n <  , arrayResultado ))
        

class fibonacci(threading.Thread):
    def __init__(self, numero):
            super().__init__()
            self.numero = numero
    
    def run(self):
        




if __name__ == "__main__":
    