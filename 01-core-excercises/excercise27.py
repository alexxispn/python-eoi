entry = 'Tokyo:38_140_000;Delhi:26_454_000;Shanghai:24_484_000;' \
        'Mumbai:21_357_000;São Paulo:21_297_000'
cities_population = {}
for city_population in entry.split(';'):
    city, population = city_population.split(':')
    cities_population[city] = int(population)
print(cities_population)

total_population = sum(cities_population.values())
for city in cities_population.keys():
    cities_population[city] *= 100 / total_population
print(cities_population)
