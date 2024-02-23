import random
from time import sleep

from view.ShowInfoView import ShowInfoView


class AspiradoraService:

    def __init__(self, mundo):
        self.__mundo = mundo
        self.__show_info = ShowInfoView()

    def run(self):
        current_quadrant = self.__mundo.current_quadrant
        while True:
            sleep(3)

            if self.__mundo.aspiradora.get_behavior() == 1:
                if self.__mundo.current_quadrant.get_name() == "Cuadrante 1":
                    if self.__mundo.cuadrante_1.get_status() == "Sucio":
                        print("El cuadrante 1 esta sucio")
                        self.__mundo.aspiradora.set_status("limpiando")
                    else:
                        current_quadrant = self.__mundo.cuadrante_2
                        self.__mundo.aspiradora.set_status("cuadrante limpio me estoy moviendo al cuadrante 2")

                elif self.__mundo.current_quadrant.get_name() == "Cuadrante 2":
                    if self.__mundo.cuadrante_2.get_status() == "Sucio":
                        print("El cuadrante 2 esta sucio")
                        self.__mundo.aspiradora.set_status("limpiando")
                    else:
                        current_quadrant = self.__mundo.cuadrante_1
                        self.__mundo.aspiradora.set_status("cuadrante limpio me estoy moviendo al cuadrante 1")

                mensaje = ("Estoy en el " + self.__mundo.current_quadrant.get_name() + ", "
                           + self.__mundo.aspiradora.get_status())

                if self.__mundo.current_quadrant.get_status() == "Sucio":
                    for i in range(self.__mundo.current_quadrant.get_cleaning_time()):
                        sleep(1)
                        print(mensaje)

                    print("He terminado de limpiar el " + self.__mundo.current_quadrant.get_name())
                    sleep(1)
                    self.__mundo.current_quadrant.set_status("Limpio")
                else:
                    print(mensaje)

                self.__mundo.current_quadrant = current_quadrant
            else:
                random_number = random.randint(0, 1)
                cuadrante = ""
                estado_cuadrante = ""
                current_quadrant = self.__mundo.current_quadrant

                if random_number == 0:
                    cuadrante = "Estoy en el cuadrante " + self.__mundo.cuadrante_1.get_name()
                    estado_cuadrante = ", el cuadrante esta " + self.__mundo.cuadrante_1.get_status()
                    accion = ", estoy limpiando" if self.__mundo.cuadrante_1.get_status() == "Sucio" \
                        else ", no estoy haciendo nada"
                else:
                    cuadrante = "no se en que cuadrante estoy"
                    estado_cuadrante = ", no se si el cuadrante esta limpio"
                    accion = ", estoy limpiando"

                print(cuadrante + estado_cuadrante + accion)
