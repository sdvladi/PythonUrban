class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """
        # TODO все аргументы конструктора записать в атрибуты экземпляра класса
        self.territory_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones
        self.green_index = self.calculate_green_index()  # индекс озеленения
        # TODO посчитать индекс озеленения с помощью метода calculate_green_index

    def calculate_green_index (self):
        self.green_index = sum(self.green_zones) / self.territory_area
        return round(self.green_index, 4)
        """
        Метод для вычисления индекса озеленения.

        Индекс рассчитывается как отношение площади всех парков к площади территории
        """

pushkin = GreenZoneIndex ('Пушкин', 28676,[302, 487, 420, 325, 471, 363, 404])
territory_name = "Пушкин"
territory_area = 28676,
green_zones = [302, 487, 420, 325, 471, 363, 404]
# TODO Создать экземпряр класса и с помощью его атрибутов распечатать индекс озеленения в процентах до 2 знака после запятой.
print(f'Индекс озеленения территории {pushkin.territory_name} равен {pushkin.green_index*100} %')
# Ожидаемый ответ Индекс озеленения территории Пушкин равен 9.67%


