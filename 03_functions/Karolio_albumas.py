from datetime import datetime

dainu_kolekcija = {}

def trukme_formatuoti(trukme):
    minutes, seconds = divmod(int(trukme), 60)
    return f"{minutes:02d}:{seconds:02d}"

def parse_trukme(trukme_text):
    try:
        trukme = datetime.strptime(trukme_text, "%M:%S")
        return trukme.minute * 60 + trukme.second
    except ValueError:
        print("Neteisingas trukmės formatas. Naudokite MM:SS formatą.")
        return None

def prideti_daina(daina, trukme_text, kompaktas=None):
    if kompaktas is not None and kompaktas != '':
        if kompaktas not in dainu_kolekcija:
            naujas_kompaktas = input(f"Kompaktas '{kompaktas}' nerastas. Sukurkite naują kompaktą: ")
            dainu_kolekcija[naujas_kompaktas] = {}
        trukme = parse_trukme(trukme_text)
        if trukme is not None:
            dainu_kolekcija[kompaktas][daina] = trukme
    else:
        trukme = parse_trukme(trukme_text)
        if trukme is not None:
            dainu_kolekcija[daina] = trukme

def issimti_daina(daina):
    for kompaktas, dainos in dainu_kolekcija.items():
        if daina in dainos:
            trukme = dainos.pop(daina)
            return trukme
    return None

def patikrinti_kolekcija():
    print("===[ Muzikos Kolekcija ]===")
    for kompaktas, dainos in dainu_kolekcija.items():
        print(f"{kompaktas}:")
        for daina, trukme in dainos.items():
            formatted_trukme = trukme_formatuoti(trukme)
            print(f"  {daina}: {formatted_trukme}")
    print("============================")

def spausdinti_trukme():
    bendra_trukme = sum(trukme for dainos in dainu_kolekcija.values() for trukme in dainos.values())
    formatted_bendra_trukme = trukme_formatuoti(bendra_trukme)
    print(f"Bendra dainų kolekcijos trukmė: {formatted_bendra_trukme}")
    
def rodyti_menu():
    print("\n┏----------------------------┓")
    print("|  BIBLIOTEKOS GENERATORIUS  |")
    print("┗----------------------------┛")
    print("\nPasirinkimai:")
    print("\n1. Pridėti dainą")
    print("2. Išimti dainą")
    print("3. Spausdinti kolekciją")
    print("4. Spausdinti trukmę")
    print("5. Baigti programą")

while True:
    rodyti_menu()
    pasirinkimas = input("\nPasirinkite veiksmą (1-5): ")

    if pasirinkimas == '1':
        daina = input("Įveskite dainos pavadinimą: ")
        trukme_text = input("Įveskite dainos trukmę (MM:SS): ")
        kompaktas = input("Įveskite kompaktą: ")
        prideti_daina(daina, trukme_text, kompaktas)
    elif pasirinkimas == '2':
        daina = input("Įveskite dainos pavadinimą, kurią norite išimti: ")
        trukme = issimti_daina(daina)
        if trukme is not None:
            formatted_trukme = trukme_formatuoti(trukme)
            print(f"{daina} išimta iš kolekcijos. Trukmė: {formatted_trukme}")
        else:
            print(f"{daina} nerasta kolekcijoje.")
    elif pasirinkimas == '3':
        patikrinti_kolekcija()
    elif pasirinkimas == '4':
        spausdinti_trukme()
    elif pasirinkimas == '5':
        print("Programa baigta.")
        break
    else:
        print("Neteisingas pasirinkimas. Bandykite dar kartą.")