""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""

def add_income(budget: dict, purpose: str, amount: float) -> None:
    if 'income' not in budget:
        budget['income'] = []
    budget['income'].append({'purpose': purpose, 'amount': amount})

def add_expense(budget: dict, purpose: str, amount: float) -> None:
    if 'expenses' not in budget:
        budget['expenses'] = []
    budget['expenses'].append({'purpose': purpose, 'amount': -amount})

def print_budget(budget: dict) -> None:
    if 'income' in budget:
        print("Pajamos:")
        for index, income in enumerate(budget['income']):
            print(f"{index + 1}. {income['purpose']}: {income['amount']}")
    else:
        print("Nėra įrašų apie pajamas.")
    
    if 'expenses' in budget:
        print("\nIšlaidos:")
        for index, expense in enumerate(budget['expenses']):
            print(f"{index + 1}. {expense['purpose']}: {expense['amount']}")
    else:
        print("Nėra įrašų apie išlaidas.")

def calculate_balance(budget: dict) -> float:
    total_income = sum(income['amount'] for income in budget.get('income', []))
    total_expenses = sum(expense['amount'] for expense in budget.get('expenses', []))
    return total_income + total_expenses

def main(budget: dict) -> None:
    while True:
        print("===[ Biudžetas ]===")
        print("1: Pridėti pajamas")
        print("2: Pridėti išlaidas")
        print("3: Spausdinti biudžetą")
        print("4: Suskaičiuoti biudžeto balansą")
        print("0: Baigti")
        
        choice = input("Pasirinkimas: ")
        
        if choice == "0":
            break
        elif choice == "1":
            purpose = input("Pajamų paskirtis: ")
            amount = float(input("Pajamų suma: "))
            add_income(budget, purpose, amount)
        elif choice == "2":
            purpose = input("Išlaidų paskirtis: ")
            amount = float(input("Išlaidų suma: "))
            add_expense(budget, purpose, amount)
        elif choice == "3":
            print_budget(budget)
        elif choice == "4":
            balance = calculate_balance(budget)
            print(f"Biudžeto balansas: {balance}")
        else:
            print("Klaida: Netinkamas pasirinkimas!")
