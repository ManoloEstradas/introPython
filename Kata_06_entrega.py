planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets.append('pluton')

#print(len(planets))
#print(planets[-1])


user_planet = input('Please enter the name of the planet (with a capital letter to start)')

planet_index = planets.index(user_planet)

print('Here are the planets closer than ' + user_planet)
print(planets[0:planet_index])

print('Here are the planets further than ' + user_planet)
print(planets[planet_index + 1:])



