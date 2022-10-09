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

pushkin = GreenZoneIndex ('Пушкин', 28676,[302, 487, 420, 325, 471, 363, 404])
territory_name = "Пушкин"
territory_area = 28676,
green_zones = [302, 487, 420, 325, 471, 363, 404]
# TODO Создать экземпряр класса и с помощью его атрибутов распечатать индекс озеленения в процентах до 2 знака после запятой.
print(f'Индекс озеленения территории {pushkin.territory_name} равен {pushkin.green_index*100} %')

list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]
list_territories_class = []
for city in list_territories:
    list_territories_class.append(GreenZoneIndex(city['territory_name'], city['territory_area'], city['green_zones']))

print(list_territories_class)

def get_mean_green_index (list_):
  sum_green_index = 0
  for object in list_:
    sum_green_index += object.green_index
  av_green_index = sum_green_index / len(list_)
  return round(av_green_index, 4)

print(get_mean_green_index(list_territories_class)*100,'%')
