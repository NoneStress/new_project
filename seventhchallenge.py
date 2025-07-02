import math

x1 = float(input("Saisissez l'abscisse du pointA: "))
y1 = float(input("Saisissez l'ordonnee du pointA: "))
x2 = float(input("Saisissez l'abscisse du pointB: "))
y2 = float(input("Saisissez l'ordonnee du pointB: "))

distance = math.sqrt((x2 - x1)**2 +(y2 - y1)**2)
print(f"La distance entre A et B est de {distance}")