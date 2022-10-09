list_cities = [
    {
        "name": "Москва",
        "population": 12 * 10 ** 6,
    },
    {
        "name": "Санкт-Петербург",
        "population": 5 * 10 ** 6,
    },
    {
        "name": "Ижевск",
        "population": 0.6 * 10 ** 6,
    },
]
filter_population = 10 ** 6

million_cities = []
for city in list_cities:
    if city ['population'] > filter_population:
        million_cities.append(city)
print(million_cities)

million_cities = [city for city in list_cities if city['population'] > filter_population]
print(million_cities)
