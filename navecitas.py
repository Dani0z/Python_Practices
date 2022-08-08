import os
import time
import escenarium
from actores import Jugador, Enemigo, Bullet
import random

# This code needs two more file to run properly.
    # Those files are:
        # actores.py
        # escenarium.py


if __name__ == "__main__":


    # Clases


    # Pornadas

    generadorEscenario = escenarium.GeneradorDeEscenarios()
    jugador = Jugador(1)
    enemigo = Enemigo(7)
    bulletEnemy = Bullet(enemigo.x, enemigo.y +1, "|")
    bulletPlayer = Bullet(jugador.x, jugador.y -1, "|")



    # Escenas

    while True:
        os.system("cls")
        escenario = generadorEscenario.generarEscenario()
        jugador.pintar(escenario)
        enemigo.pintar(escenario)


        # Shot H
        if(bulletEnemy.getInWait() == True):
            decision = random.choice([True, False, False, False])
            if(decision == True):
                bulletEnemy.getShot(enemigo, 1)

        if(bulletEnemy.getInWait() == False):
            bulletEnemy.pintar(escenario)


        # Shot X
        if(bulletPlayer.getInWait() == True):
            decision2 = random.choice([True, False, False])
            if(decision2 == True):
                bulletPlayer.getShot(jugador, -1)

        if(bulletPlayer.getInWait() == False):
            bulletPlayer.pintar(escenario)

        for fila in escenario:
            for columnas in fila:
                print(columnas, end="")
            print()


        if(bulletPlayer.x == enemigo.x and bulletPlayer.y == enemigo.y):
            print("You win!!")
            print("Game Over!!")
            input("Press Enter to continue")

        elif(bulletEnemy.x == jugador.x and bulletEnemy.y == jugador.y):
            print("Enemy wins!!")
            print("Game Over!!")
            input("Press Enter to continue")


        # ID's
        # print(jugador.mostrarID())
        # print(enemigo.mostrarID())
        # print(bullet.mostrarID())

        time.sleep(0.08)
        jugador.mover()
        enemigo.mover()
        bulletEnemy.mover()
        bulletPlayer.mover()