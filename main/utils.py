import random

class TaxiAPI:
    """Утилитный класс сервиса такси

    Сервис такси рассчитывает число километров 
    для созданных поездок.
    """

    @staticmethod
    def get_length():
        """Возвращает случайное значение длины пути
        """
        return random.randint(5, 50)