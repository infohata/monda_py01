class Product:
    def __init__(self, name:str, quantity:float, unit_of_measurement = '', **kwargs):
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = unit_of_measurement # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}: {self.unit_of_measurement}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity}: {self.unit_of_measurement})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


class Fridge:
    def __init__(self):
        self.contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name.lower() == product_name.lower():
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float, unit_of_measurement:str):
        valid_units = ['kg', 'g', 'l', 'ml', 'vnt']
        if unit_of_measurement not in valid_units:
            print("Netinkamas vienetas! Galimi vienetai: kg, g, l, ml, vnt")
            return
        else:
            print('Iveskite tesinga pasirinkima')
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity, unit_of_measurement))

    def remove_product(self, name:str, quantity:float): 
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product:
            if product.quantity >= quantity:
                product.quantity -= quantity
   
            else:
                print(f'Nepakankamas kiekis {product.name} saldytuve yra {product.quantity}')
        else:
            print(f'Produktas {name} nerastas saldytuve')

    def print_contents(self):
        print("Saldytuvo turinys:")
        for product in self.contents:
            print(product)

    def create_recipe(self):
        recipe = Recipe()
        while True:
            print("Pridėkite ingredientą į receptą (irasykite zodi 'baigti' - kad iseiti is recepto kurimo)")
            ingredient_name = input("Koks ingredientas?: ")
            if ingredient_name.lower() == "baigti":
                break
            ingredient_quantity = float(input(f"Kiek {ingredient_name}?: "))
            recipe.add_ingredient(Product(ingredient_name, ingredient_quantity))
        return recipe

    def check_recipe(self, recipe: Recipe):
        missing_ingredients = []
        for ingredient in recipe.ingredients:
            _, product = self.check_product(ingredient.name)
            if product is not None:
                missing_quantity = product.quantity - ingredient.quantity
                if missing_quantity < 0:
                    missing_ingredients.append(Product(ingredient.name, abs(missing_quantity)))
            else:
                missing_ingredients.append(ingredient)
        if len(missing_ingredients) == 0:
            print('Jus turite reikiamus produktus')
        else:
            print(f'Jums truksta siu produktu: {missing_ingredients}')
            
#Jums truksta siu produktu: [(duona, 5.0: ), (agurkas, 10.0: ), (pomidoras, 9.0: )] neveikia atitinkamai patikrinimas recepto kazkur reikia uzbaigti recepto tikrinima, nes blogai isspausdina
def main():
    fridge = Fridge()
    
    while True:
        print("---Violetinis šaldytuvas---")
        print("0: Išeiti")
        print("1: Pridėti produktą į šaldytuvą")
        print("2: Pašalinti produktą iš šaldytuvo")
        print("3: Patikrinti produkto kiekį")
        print("4: Parodyti šaldytuvo turinį")
        print("5: Patikrinti receptą")
        
        choice = input("Pasirinkite: ")

        if choice == "0":
            break
        elif choice == "1":
            product_name = input("Kokį produktą norite pridėti?: ")
            product_quantity = float(input("Kokį kiekį norite pridėti?: "))
            unit_of_measurement = input('Koks tai yra matavimo vienetas? (options: kg, g, l, ml)')
            valid_units = ['kg', 'g', 'l', 'ml', 'vnt']
            if unit_of_measurement not in valid_units:
                print('Iveskite teisinga matavimo vieneta! Pvz: kg, g, l, ml, vnt')
                continue
            fridge.add_product(product_name, product_quantity, unit_of_measurement)
            print(f'Sekmingai ideta {product_name} {product_quantity}: {unit_of_measurement}.')
        elif choice == "3":
            product_name = input("Kokio produkto kiekį norite patikrinti?: ")
            _, product = fridge.check_product(product_name)
            if product:
                print(f"Produkto {product.name} kiekis šaldytuve: {product.quantity}: {unit_of_measurement}")
            else:
                print("Toks produktas nerastas šaldytuve.")
        elif choice == "2":
            product_name = input("Kokį produktą norite pašalinti?: ")
            product_quantity = float(input("Kokį kiekį norite pašalinti?: "))
            fridge.remove_product(product_name, product_quantity)
            print(f'Sekmingai isimta {product_name} {product_quantity}: {unit_of_measurement}')
        elif choice == "4":
            fridge.print_contents()
        elif choice == "5":
            recipe = fridge.create_recipe()
            fridge.check_recipe(recipe)
        else:
            print("Neteisingas pasirinkimas. Įveskite skaičių nuo 0 iki 5.") 
main()