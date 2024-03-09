from model.Aspiradora import Aspiradora
from model.Cuadrante import Cuadrante


class Mundo:

    def __init__(self):
        self.cuadrante_1 = Cuadrante("A", "limpio", 5)
        self.cuadrante_2 = Cuadrante("B", "limpio", 10)
        self.aspiradora = Aspiradora("En reposo", 1)
        self.current_quadrant = self.cuadrante_1

    def ensuciar_cuadrante(self, id_cuadrante):
        if id_cuadrante == 1:
            self.cuadrante_1.set_status("sucio")
        else:
            self.cuadrante_2.set_status("sucio")

