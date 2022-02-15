#Ejercicio 1
from math import ceil, floor
from unittest.mock import seal


planet = {
    'name': 'Mars',
    'moons': 2
}
print(planet['name'], planet['moons'])

planet.update ({
  'polar': 6752,
  'equatorial': 6792

})

print(planet)


#Ejercicio 2

# Planets and moons

planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

moons = planet_moons.values()
planets = len(planet_moons.keys())

total_moons = 0
for moon in moons:
    total_moons = total_moons + moon

average = total_moons / planets

print(ceil(average))

