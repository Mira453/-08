import math
from tabulate import tabulate
cities = {
    'Баку': (40.4093, 49.8671),
    'Гянджа': (40.6828, 46.3606),
    'Сумгаїт': (40.5897, 49.6686),
    'Мінгечаур': (40.7656, 47.0486),
    'Шекі': (41.1919, 47.1706),
    'Хачмаз': (41.4644, 48.8057),
    'Ленкорань': (38.7520, 48.8510),
    'Ширван': (39.9310, 48.9200),
    'Євлах': (40.6186, 47.1506),
    'Нафталан': (40.5069, 46.8250),
    'Губа': (41.3653, 48.5130),
    'Сабірабад': (39.9933, 48.4783),
    'Агдаш': (40.6500, 47.4731),
    'Загатала': (41.6319, 46.6431),
    'Бейлаган': (39.7700, 47.6167)
}

def haversine(coord1, coord2):
    R = 6371
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def greedy_tsp(cities):
    unvisited = set(cities.keys())
    current_city = next(iter(unvisited))
    path = [current_city]
    unvisited.remove(current_city)
    total_distance = 0

    while unvisited:
        next_city = min(unvisited, key=lambda city: haversine(cities[current_city], cities[city]))
        distance = haversine(cities[current_city], cities[next_city])
        total_distance += distance
        current_city = next_city
        path.append(current_city)
        unvisited.remove(current_city)

    total_distance += haversine(cities[current_city], cities[path[0]])
    path.append(path[0])

    return path, total_distance


route, total_distance = greedy_tsp(cities)


road_connect = [
    ('Баку', 'Сумгаїт', 42),
    ('Баку', 'Ширван', 128),
    ('Ширван', 'Сабірабад', 47),
    ('Сабірабад', 'Бейлаган', 101),
    ('Євлах', 'Гянджа', 67),
    ('Гянджа', 'Нафталан', 44),
    ('Євлах', 'Агдаш', 40),
    ('Агдаш', 'Мінгечаур', 38),
    ('Мінгечаур', 'Шекі', 71),
    ('Шекі', 'Загатала', 76),
    ('Губа', 'Хачмаз', 27),
    ('Хачмаз', 'Сумгаїт', 138),
    ('Баку', 'Ленкорань', 282)
]


road_table = [[a, b, f"{d} км"] for a, b, d in road_connect]


direct_table = [[a, b, f"{haversine(cities[a], cities[b]):.2f} км"] for a, b, _ in road_connect]

headers = ["Місто 1", "Місто 2", "Відстань"]

print(f"Маршрут жадібного пошуку: {' → '.join(route)}")
print(f"Довжина маршруту по прямій: {total_distance:.2f} км\n")

print("Відстані між містами по прямій (км):")
print(tabulate(direct_table, headers=headers, tablefmt="grid"))

print("\nВідстані між містами по дорозі (км), якщо між ними є прямий шлях:")
print(tabulate(road_table, headers=headers, tablefmt="grid"))