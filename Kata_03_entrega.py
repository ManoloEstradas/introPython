#Mensaje advertencias asteroides!!
vel = 49
if(vel <= 25):
  print("Fire in the holl!!")
else:
  print("Have a good day")


velaster = 19
if(velaster <= 20):
  print("Look Up, y pide un deseo")
else:
  print("No hay deseos para hoy")


velAster = 49
sizeAster = 100
if(velAster >= 25 and sizeAster >= 25):
  print("Peligro! Asteroide de posible extinción viene en camino")
elif(velAster >= 20):
  print("Look Up, y pide un deseo")
elif(sizeAster < 25):
  print("Have a good day")
else:
  print("Have a good day")
