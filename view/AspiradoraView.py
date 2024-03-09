import os
from time import sleep


class AspiradoraView:

    acciones = {
        'preguntar_donde_estoy': 'donde_estoy?',
        'preguntar_esta_sucio': 'esta_sucio?',
        'limpiar': 'limpiando...',
        'mover': 'moviendome'
    }

    modelo = {
        ('me_movi', 'preguntar_donde_estoy', 'cuadrante_A'): 'estoy_en_A',
        ('me_movi', 'preguntar_donde_estoy', 'cuadrante_B'): 'estoy_en_B',
        ('estoy_en_A', 'preguntar_esta_sucio?', 'sucio'): 'cuadrante_sucio',
        ('estoy_en_A', 'preguntar_esta_sucio?', 'limpio'): 'cuadrante_limpio',
        ('estoy_en_B', 'preguntar_esta_sucio?', 'sucio'): 'cuadrante_sucio',
        ('estoy_en_B', 'preguntar_esta_sucio?', 'limpio'): 'cuadrante_limpio',
        ('cuadrante_sucio', 'limpiar_y_mover', 'finalice_accion'): 'me_movi',
        ('cuadrante_limpio', 'mover', 'finalice_accion'): 'me_movi'
    }

    def actualizar_estado(self, estado, accion, percepcion):
        if (estado, accion, percepcion) in self.modelo:
            return self.modelo[(estado, accion, percepcion)]
        else:
            return 'me_movi'

    def __init__(self):
        self.option = 0

    def show(self, estado, accion, percepcion, texto_accion):
        os.system('clear')
        print(f"Estado: {estado}, Accion: {accion}, Percepcion: {percepcion} (ingrese 0 para salir)", end=" -> ")

        print(f"{texto_accion}")

    def ask_for_perception(self):
        os.system('clear')
        print("Ingrese la percepcion")
        print("1. Sucio")
        print("2. Limpio")
        print("3. Cuadrante A")
        print("4. Cuadrante B")
        print("0. Salir")

        self.option = input("Ingrese una opcion: \n")

    def get_option(self):
        self.option = input("Ingrese percepcion: \n")
        return self.option

    def opcion_invalida(self):
        print("Opcion invalida")
        sleep(1)