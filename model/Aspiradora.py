class Aspiradora:

    def __init__(self, status, behavior):
        self.__status = status
        self.__behavior = behavior

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def set_behavior(self, behavior):
        self.__behavior = behavior

    def get_behavior(self):
        return self.__behavior
