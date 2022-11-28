entry = 'Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;' \
        'Mumbai:21_357_000;São Paulo:21_297_000'
diccionario = {}
for city_population in entry.split(';'):
    city, population = city_population.split(':')
    diccionario[city] = int(population)
print(diccionario)
