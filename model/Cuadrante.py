class Cuadrante:
    def __init__(self, position, status, cleaning_time):
        self.__position = position
        self.__status = status
        self.__cleaning_time = cleaning_time

    def set_status(self, status):
        self.__status = status

    def get_status(self):
        return self.__status

    def get_name(self):
        return "Cuadrante " + str(self.__position)

    def set_position(self, position):
        self.__position = position

    def get_position(self):
        return self.__position

    def get_cleaning_time(self):
        return self.__cleaning_time