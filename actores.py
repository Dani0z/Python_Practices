import time
import random

if __name__ == "__main__":
    print("Este archivo no se puede utilizar tal cual. Debes importarlo en navecitas.py")

class ObjetoDelJuego():
    x = 1
    y = 1
    dibujo = "?"
    velocidad_x = 1
    __id = 0

    def pintar(self, escena):
        for num_fila, fila in enumerate(escena):
            for num_columna, columna in enumerate(fila):
                if(num_fila == self.y and num_columna == self.x):
                        escena[num_fila][num_columna] = self.dibujo
    
    def mover(self):
        decision = random.choice([True, False])
        if decision == False:
            return
        if(self.x == 17):
            self.velocidad_x = -1
        elif(self.x == 1):
            self.velocidad_x = 1
        self.x = self.x + self.velocidad_x

   # Getter 
    def mostrarID(self):
        return self.__id
   # Setter
    def setearID(self):
        self.__id = time.time()





class Jugador(ObjetoDelJuego):
    dibujo = ">┴<"
    y = 8
    def __init__(self, x):
        self.x = x
        super().setearID()
    


class Enemigo(ObjetoDelJuego):
    dibujo = "╠O╣" # ├O┤ ╠O╣
    def __init__(self, x):
        self.x = x
        super().setearID()


class Bullet(ObjetoDelJuego):
    __inWait = True
    velocidad_y = 1

    def __init__(self, columna, fila, caracter):
        self.x = columna
        self.y = fila
        self.dibujo = caracter
        super().setearID()

    def mover(self):
        if (self.__inWait == False):
            self.y = self.y + self.velocidad_y
            if self.y == 9:
                self.y = 10
                self.__inWait = True
            if self.y == 0:
                self.y = -1
                self.__inWait = True
    
    def getInWait(self):
        return self.__inWait

    def getShot(self, position, velocidad_y):
        self.x = position.x
        self.y = position.y + velocidad_y
        self.__inWait = False
        self.velocidad_y = velocidad_y
