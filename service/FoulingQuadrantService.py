from view.FoulingQuadrantView import FoulQuadrantView


class FoulingQuadrantService:

    def __init__(self, mundo):
        self.__view = FoulQuadrantView()
        self.__mundo = mundo

    def run(self):
        self.__view.show()
        option = self.__view.get_option()

        if option == "0":
            return

        if option == "1":
            self.__mundo.cuadrante_1.set_status("sucio")
        elif option == "2":
            self.__mundo.cuadrante_2.set_status("sucio")
        else:
            self.__view.opcion_invalida()
            self.run()
