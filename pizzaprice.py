def unit_price(diameter, price):
    radius = diameter / 2 / 100      
    area = 3.14 * radius * radius
    return price / area


d1 = float(input("Pizza 1 diameter (cm): "))
p1 = float(input("Pizza 1 price (USD): "))

d2 = float(input("Pizza 2 diameter (cm): "))
p2 = float(input("Pizza 2 price (USD): "))

u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)

if u1 < u2:
    print("Pizza 1 is cheaper per square meter.")
elif u1 > u2:
    print("Pizza 2 is cheaper per square meter.")
else:
    print("Both pizzas have the same price per square meter.")