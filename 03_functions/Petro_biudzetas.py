def add_income_or_expenses(budget, category: str, amount: float):
    if category in budget:
        budget[category] += amount
    else:
        budget[category] = amount
    return budget[category]

def print_finance(budget):
    print('Pajamų ir išlaidų žurnalas:')
    for index, (category, amount) in enumerate(budget.items(), start=1):
        if amount > 0:
            print(f'{index}. Pajamos ({category}): {amount:.2f} €')
        elif amount < 0:
            print(f'{index}. Išlaidos ({category}): {amount:.2f} €')
        else:
            print(f'{index}. {category}: {amount:.2f} €')

def calculate_balance(budget):
    balance = 0
    for amount in budget.values():
        balance += amount
    return balance
def main():
    budget = {}

    while True:
        print('''
        --- Ką norite pasirinkti?:--- 
        0. Nesigadink sau nervų ir išeik     
        1. Pridėti pajamas arba išlaidas
        2. Spausdinti finansų ataskaitą
        3. Skaičiuoti biudžeto balansą
            ''')
        choice = input('Pasirinkite veiksmą (0-3): ')
        
        if choice == '0':
             print('Teisingas sprendimas')
             break
        
        elif choice == "1":
            while True:
                category = input('Įveskite kategoriją: ')
                if category.isnumeric():
                    print('Pajamų ar išlaidų pavadinimas turi būti žodis!')
                    continue
                else:
                    break
            while True:
                amount_input = input('Įveskite sumą (neigiama suma reiškia išlaidas): ')
                try:
                    amount = float(amount_input)
                    break
                except ValueError:
                    print('Įvesti duomenys netinka. Prašome įvesti skaičių.')
            add_income_or_expenses(budget, category, amount)
            print(f'Pridėta: {amount:.2f} € prie kategorijos {category}')
        elif choice == "2":
            print_finance(budget)
        elif choice == "3":
            balance = calculate_balance(budget)
            print(f'Biudžeto balansas: {balance:.2f} €')
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")


if __name__ == "__main__":
    main()