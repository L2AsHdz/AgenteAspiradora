import os
from time import sleep


class FoulQuadrantView:

    def __init__(self):
        self.option = 0

    def show(self):
        os.system('clear')
        print("Mundo de la aspiradora dummy???")
        print("Escoge un cuadrante para ensuciar:")
        print("1. Ensuciar cuadrante 1")
        print("2. Ensuciar cuadrante 2")
        print("0. Salir")
        self.option = input("Seleccione una opcion: \n")

    def get_option(self):
        return self.option

    def opcion_invalida(self):
        print("Opcion invalida")
        sleep(1)