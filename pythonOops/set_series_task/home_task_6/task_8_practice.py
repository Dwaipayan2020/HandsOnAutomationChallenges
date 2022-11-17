d1 = {'a': {'r': 2, 's': 3}, 'b': 2, 'c': 3}
d2 = {'a': {'r': 2, 's': 3}, 'c': 3, 'b': 2}

var = [k1 for k1, v1 in d1.items() for k2, v2 in d2.items() if d1 == d2]

print(d1 == d2)


def side_effects(cities):
    print(cities)
    cities += ["Paris", "Marseille"]
    print(cities)


locations = ["Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg"]
side_effects(locations[:])
print(locations)

["Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg"]
["Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Paris", "Marseille"]
["Lyon", "Toulouse", "Nice", "Nantes", "Strasbourg", "Paris", "Marseille"]