import os
from time import sleep


class ShowInfoView:

    def __init__(self):
        self.option = 0

    def show(self, estado_cuadrante_1, estado_cuadrante_2, modo_aspiradora):
        os.system('clear')
        print("Mundo de la aspiradora dummy???")
        print("Estado de los cuadrantes")
        print("Cuadrante 1: " + estado_cuadrante_1)
        print("Cuadrante 2: " + estado_cuadrante_2)
        print("Comportamiento aspiradora: " + modo_aspiradora)
        print("1. Ensuciar cuadrante")
        print("2. Cambiar modo de aspiradora")
        print("0. Salir")

        self.option = input("Ingrese una opcion: \n")

    def despedir(self):
        print("Adios....")

    def opcion_invalida(self):
        print("Opcion invalida")
        sleep(1)

    def get_option(self):
        return self.option
