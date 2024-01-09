""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""
class Fridge:
    def __init__(self):
        self.contents = {}

    def add_product(self, product, quantity):
        product = product.lower() 
        if product in self.contents:
            self.contents[product] += quantity
        else:
            self.contents[product] = quantity

    def remove_product(self, product, quantity):
        product = product.lower() 
        if product in self.contents:
            if self.contents[product] >= quantity:
                self.contents[product] -= quantity
                if self.contents[product] == 0:
                    del self.contents[product]
            else:
                print(f"Nepakanka {product} šaldytuve.")
        else:
            print(f"{product} neegzistuoja šaldytuve.")

    def check_product_quantity(self, product, needed_quantity):
        product = product.lower()
        if product in self.contents:
            if self.contents[product] >= needed_quantity:
                print(f"{product} šaldytuve yra pakankamai: {self.contents[product]}")
            else:
                print(f"Nepakanka {product} šaldytuve. Yra tik {self.contents[product]}")
        else:
            print(f"{product} neegzistuoja šaldytuve.")

    def print_contents(self):
        print("Šaldytuvo turinys:")
        for product, quantity in self.contents.items():
            print(f"{product}: {quantity}")

    def check_recipe(self, recipe):
        needed_products = {}
        for item in recipe.split(", "):
            product, quantity = item.split(": ")
            product = product.lower() 
            needed_products[product] = float(quantity)

        missing_products = {}
        for product, quantity in needed_products.items():
            if product not in self.contents or self.contents[product] < quantity:
                missing_products[product] = quantity - self.contents.get(product, 0)

        if missing_products:
            print("Receptas neišeina. Trūksta:")
            for product, quantity in missing_products.items():
                print(f"{product}: {quantity}")
        else:
            print("Receptas išeina!")

    def manual_interaction(self):
        print("Sveiki atvykę į šaldytuvo valdymo sistemą!")
        print("Pasirinkite veiksmą:")
        print("1. Pridėti produktą")
        print("2. Išimti produktą")
        print("3. Tikrinti produkto kiekį")
        print("4. Patikrinti receptą")
        print("5. Spausdinti šaldytuvo turinį")
        print("0. Išeiti")

        while True:
            choice = input("Įveskite veiksmo numerį: ")

            if choice == "1":
                product = input("Įveskite produkto pavadinimą: ")
                quantity = float(input("Įveskite kiekį: "))
                self.add_product(product, quantity)
                print(f"{quantity} {product} pridėta į šaldytuvą.")

            elif choice == "2":
                product = input("Įveskite produkto pavadinimą: ")
                quantity = float(input("Įveskite kiekį: "))
                self.remove_product(product, quantity)
                print(f"{quantity} {product} išimta iš šaldytuvo.")

            elif choice == "3":
                product = input("Įveskite produkto pavadinimą: ")
                needed_quantity = float(input("Įveskite norimą kiekį: "))
                self.check_product_quantity(product, needed_quantity)

            elif choice == "4":
                recipe = input("Įveskite receptą (pvz.: Sviestas: 0.2, Pomidoras: 4): ")
                self.check_recipe(recipe)

            elif choice == "5":
                self.print_contents()

            elif choice == "0":
                print("Viso gero!")
                break

            else:
                print("Neteisinga įvestis.")


# Sukuriame šaldytuvą
fridge = Fridge()

# Rankinis valdymas
fridge.manual_interaction()
