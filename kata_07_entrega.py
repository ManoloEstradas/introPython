newPlanet = ''
planet = []

while newPlanet.lower() != 'done':
    if newPlanet:
        planet.append(newPlanet)
    newPlanet = input('Enter a new planet ')

for planeta in planet:
    print(planeta)