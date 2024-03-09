import random
from time import sleep

from view.AspiradoraView import AspiradoraView
from view.ShowInfoView import ShowInfoView


class AspiradoraService:

    reglas = {
        'me_movi': 'preguntar_donde_estoy',
        'estoy_en_A': 'preguntar_esta_sucio',
        'estoy_en_B': 'preguntar_esta_sucio',
        'cuadrante_sucio': 'limpiar',
        # 'cuadrante_sucio_n': 'no_hacer_nada',
        'cuadrante_limpio': 'mover',
        'limpie': 'mover',
        'no_hice_nada': 'limpiar',
    }

    acciones = {
        'preguntar_donde_estoy': 'donde_estoy?',
        'preguntar_esta_sucio': 'esta_sucio?',
        'no_hacer_nada': 'no estoy haciendo nada...',
        'limpiar': 'limpiando...',
        'mover': 'moviendome'
    }

    modelo = {
        ('me_movi', 'preguntar_donde_estoy', 'cuadrante_A'): 'estoy_en_A',
        ('me_movi', 'preguntar_donde_estoy', 'cuadrante_B'): 'estoy_en_B',

        ('estoy_en_A', 'preguntar_esta_sucio', 'sucio'): 'cuadrante_sucio',
        ('estoy_en_A', 'preguntar_esta_sucio', 'limpio'): 'cuadrante_limpio',
        ('estoy_en_B', 'preguntar_esta_sucio', 'sucio'): 'cuadrante_sucio',
        ('estoy_en_B', 'preguntar_esta_sucio', 'limpio'): 'cuadrante_limpio',

        ('cuadrante_sucio', 'limpiar', 'termine'): 'limpie',
        ('cuadrante_sucio', 'no_hacer_nada', 'termine'): 'no_hice_nada',

        ('no_hice_nada', 'limpiar', 'termine'): 'limpie',
        ('limpie', 'mover', 'cuadrante_A'): 'me_movi',
        ('limpie', 'mover', 'cuadrante_B'): 'me_movi',

        ('cuadrante_limpio', 'mover', 'cuadrante_A'): 'me_movi',
        ('cuadrante_limpio', 'mover', 'cuadrante_B'): 'me_movi'
    }

    def __init__(self, mundo):
        self.__view = AspiradoraView()
        self.__mundo = mundo
        self.__estado = 'me_movi'
        self.__accion = 'preguntar_donde_estoy'
        self.__percepcion = ''
        self.__texto_accion = ''

    def run2(self):
        option = -1

        while option != 0:

            option = self.__view.get_option()
            self.__percepcion = option

            self.__view.show(self.__estado, self.__accion, self.__percepcion, self.__texto_accion)

            if option == "0":
                return

            self.__estado = self.__view.actualizar_estado(self.__estado, self.__accion, self.__percepcion)
            self.__accion = self.reglas[self.__estado]
            self.__texto_accion = self.__view.acciones[self.__accion]

    def actualizar_estado(self, estado, accion, percepcion):
        if (estado, accion, percepcion) in self.modelo:
            return self.modelo[(estado, accion, percepcion)]
        else:
            return 'me_movi'

    def run(self):
        current_quadrant = self.__mundo.current_quadrant
        while True:
            sleep(1)

            if self.__mundo.aspiradora.get_behavior() == 1:

                if self.__accion == 'preguntar_donde_estoy' or self.__accion == 'mover':
                    self.__percepcion = self.__mundo.current_quadrant.get_name()
                elif self.__accion == 'preguntar_esta_sucio':
                    self.__percepcion = self.__mundo.current_quadrant.get_status()
                elif self.__accion == 'no_hacer_nada' or self.__accion == 'limpiar':
                    self.__percepcion = 'termine'

                print(f"Estado: {self.__estado}, Accion: {self.__accion}, Percepcion: {self.__percepcion}", end="")
                self.__estado = self.actualizar_estado(self.__estado, self.__accion, self.__percepcion)
                print(f" -> {self.__estado}")

                self.__accion = self.reglas[self.__estado]
                self.__texto_accion = self.acciones[self.__accion]

                print(f"{self.__texto_accion}")

                if self.__percepcion == "limpio" or self.__percepcion == 'termine':
                    self.__mundo.current_quadrant = self.__mundo.cuadrante_2 if self.__mundo.current_quadrant.get_name() == "cuadrante_A" else \
                        self.__mundo.cuadrante_1




            #     if self.__mundo.current_quadrant.get_name() == "Cuadrante 1":
            #         if self.__mundo.cuadrante_1.get_status() == "Sucio":
            #             print("El cuadrante 1 esta sucio")
            #             self.__mundo.aspiradora.set_status("limpiando")
            #         else:
            #             number = random.randint(0, 1)
            #
            #             if number == 0:
            #                 current_quadrant = self.__mundo.cuadrante_2
            #                 self.__mundo.aspiradora.set_status("cuadrante limpio me estoy moviendo al cuadrante 2")
            #             else:
            #                 self.__mundo.aspiradora.set_status("cuadrante limpio, no estoy haciendo nada")
            #
            #     elif self.__mundo.current_quadrant.get_name() == "Cuadrante 2":
            #         if self.__mundo.cuadrante_2.get_status() == "Sucio":
            #             print("El cuadrante 2 esta sucio")
            #             self.__mundo.aspiradora.set_status("limpiando")
            #         else:
            #             number = random.randint(0, 1)
            #
            #             if number == 0:
            #                 current_quadrant = self.__mundo.cuadrante_1
            #                 self.__mundo.aspiradora.set_status("cuadrante limpio me estoy moviendo al cuadrante 1")
            #             else:
            #                 self.__mundo.aspiradora.set_status("cuadrante limpio, no estoy haciendo nada")
            #
            #     mensaje = ("Estoy en el " + self.__mundo.current_quadrant.get_name() + ", "
            #                + self.__mundo.aspiradora.get_status())
            #
            #     if self.__mundo.current_quadrant.get_status() == "Sucio":
            #         for i in range(self.__mundo.current_quadrant.get_cleaning_time()):
            #             sleep(1)
            #             print(mensaje)
            #
            #         print("He terminado de limpiar el " + self.__mundo.current_quadrant.get_name())
            #         sleep(1)
            #         self.__mundo.current_quadrant.set_status("Limpio")
            #     else:
            #         print(mensaje)
            #
            #     self.__mundo.current_quadrant = current_quadrant
            # else:
            #     cuadrante = "Estoy en el cuadrante " + self.__mundo.cuadrante_1.get_name() if random.randint(0, 1) == 0 \
            #         else "No se en que cuadrante estoy"
            #     estado_cuadrante = ", el cuadrante esta " + self.__mundo.cuadrante_1.get_status() if random.randint(0,
            #                                                                                                         1) == 0 \
            #         else ", no se si el cuadrante esta limpio"
            #     accion = (
            #         ", estoy limpiando" if self.__mundo.cuadrante_1.get_status() == "Sucio" else ", no estoy haciendo nada") \
            #         if random.randint(0, 1) == 0 else ", estoy en reposo"
            #
            #     print(cuadrante + estado_cuadrante + accion)
