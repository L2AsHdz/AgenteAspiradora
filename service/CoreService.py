import threading

from model.Aspiradora import Aspiradora
from model.Mundo import Mundo
from service.AspiradoraService import AspiradoraService
from service.FoulingQuadrantService import FoulingQuadrantService
from view.ShowInfoView import ShowInfoView


class CoreService:

    def __init__(self):
        self.mundo = Mundo()
        self.showInfoView = ShowInfoView()

    def run(self):
        option = -1

        aspiradora_service = AspiradoraService(self.mundo)
        hilo = threading.Thread(target=aspiradora_service.run)
        hilo.start()

        while option != 0:
            self.showInfoView.show(
                self.mundo.cuadrante_1.get_status(),
                self.mundo.cuadrante_2.get_status(),
                "Inteligente" if self.mundo.aspiradora.get_behavior() == 1 else "Pendejo"
            )

            option = self.showInfoView.get_option()
            if option == "1":
                foulingService = FoulingQuadrantService(self.mundo)
                foulingService.run()

            if option == "2":
                if self.mundo.aspiradora.get_behavior() == 1:
                    self.mundo.aspiradora.set_behavior(2)
                else:
                    self.mundo.aspiradora.set_behavior(1)
            elif option == "0":
                self.showInfoView.despedir()
                exit()
            else:
                self.showInfoView.opcion_invalida()
