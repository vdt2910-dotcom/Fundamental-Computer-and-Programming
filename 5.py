t = float(input("Enter talents: "))
p = float(input("Enter pounds: "))
l = float(input("Enter lots: "))

lots_total = t * 20 * 32 + p * 32 + l
grams_total = lots_total * 13.3

kg = int(grams_total // 1000)
g = grams_total % 1000

print("The weight in modern units:")
print(f"{kg} kilograms and {g:.2f} grams.")