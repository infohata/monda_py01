# Specialiai klaidinga skaičiuoklė

countdown = 10

while countdown > 0:  # Bug 1: Sąlyga turėtų būti countdown > 0
    print(countdown)
    countdown -= 1    # Bug 2: Turįtų būti atimama po 1-ną

print("Blast Off!")  # Bug 3: Turėtų išspausdinti "Blast Off!"
