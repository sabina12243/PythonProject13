import math

def unit_price(diameter, price):
    radius = diameter / 2 / 100
    area = math.pi * radius ** 2
    return price / area

d1 = float(input("Enter diameter of first pizza (cm): "))
p1 = float(input("Enter price of first pizza (EUR): "))

d2 = float(input("Enter diameter of second pizza (cm): "))
p2 = float(input("Enter price of second pizza (EUR): "))

u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)

print("First pizza price per m²:", round(u1, 2))
print("Second pizza price per m²:", round(u2, 2))

if u1 < u2:
    print("First pizza is better value.")
elif u2 < u1:
    print("Second pizza is better value.")
else:
    print("Both pizzas are equal in value.")