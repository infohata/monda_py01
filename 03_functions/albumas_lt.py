""" Komandinio/individualaus darbo užduotis
===[ Muzikos Albumas ]===

Reikalavimai:

* Žodynas albumas turi turėti atlikėją ir pavadinimą, gali turėti ir kitų atributų
* Albumo žodyne sukurkite takelių (dainų) sąrašą, kur kiekvienas takelis yra žodynas, talpinantis eilės numerį, pavadinimą ir trukmę sekundėmis. 
** Bonus: trukmės įvedimas "minutės:sekundės" formatu (žmogui suprantamu).
* Programa turi leisti vartotojui užpildyti/pakeisti albumo informaciją (pavadinimą, atlikėją, ...)
* Programa turi leisti vartotojui sukurti/ištrinti takelį, užpildant takelio informaciją (pavadinimą, trukmę)
* Galimybė peržiūrėti albumą, išspausdinant takelių kiekį ir bendrą jų trukmę šalia kitų atributų.
* Peržiūrėti albumo dainas. Bonus: išrūšiuotas pagal eilės numerį. Takelio trukmė turi būti pateikta žmogui suprantama laiko išraiška.

Pastabos:
* Stenkitės nekartoti kodo - funkcionalumui, kuriam kodas kartotųsi, parašykite atskiras funkcijas ir jas panaudokite kelis kartus kur reikia.
"""
albumas = {
    "Atlikėjas": "Gilė",
    "Pavadinimas": "Gilės kalėdos",
    "Dainų sąrašas": [
        {"Eilės numeris": 1, "Dainos pavadinimas": "Čiūto, Čiūto", "Trukmė": 247},
        {"Eilės numeris": 2, "Dainos pavadinimas": "Atlėkė Elnias Devyniaragis", "Trukmė": 201},
        {"Eilės numeris": 3, "Dainos pavadinimas": "Kelkit Anksti, Bajorai", "Trukmė": 242},
        {"Eilės numeris": 4, "Dainos pavadinimas": "Sakalėli, Sierasai", "Trukmė":  230 }
    ]}

def konvertuoti_i_minutes(sekundes):
    minutes = sekundes // 60
    likutis_sekundžių = sekundes % 60
    return f"{minutes}:{likutis_sekundžių:02d}"


print("\nAlbumo informacija:")
print(f"Atlikėjas: {albumas['Atlikėjas']}")
print(f"Pavadinimas: {albumas['Pavadinimas']}")
print("\nDainų sąrašas:")
for daina in albumas["Dainų sąrašas"]:
    trukmė_minutėmis = konvertuoti_i_minutes(daina['Trukmė'])
    print(f"Eilės numeris: {daina['Eilės numeris']} Dainos pavadinimas: {daina['Dainos pavadinimas']} Trukmė: {trukmė_minutėmis}")
    
def redaguoti_albumo_informacija(albumas):
    print("\nDabartinė albumo informacija:")
    print(f"Atlikėjas: {albumas['Atlikėjas']}")
    print(f"Pavadinimas: {albumas['Pavadinimas']}")
    print("\nĮveskite naują informaciją:")
    naujas_atlikejas = input("Naujas atlikėjas: ")
    naujas_pavadinimas = input("Naujas pavadinimas: ")
    albumas['Atlikėjas'] = naujas_atlikejas
    albumas['Pavadinimas'] = naujas_pavadinimas

redaguoti_albumo_informacija(albumas)

print("\nNauja albumo informacija:")
print(f"Atlikėjas: {albumas['Atlikėjas']}")
print(f"Pavadinimas: {albumas['Pavadinimas']}")
for daina in albumas["Dainų sąrašas"]:
    trukmė_minutėmis = konvertuoti_i_minutes(daina['Trukmė'])
    print(f"Eilės numeris: {daina['Eilės numeris']} Dainos pavadinimas: {daina['Dainos pavadinimas']} Trukmė: {trukmė_minutėmis}")








def prideti_daina(albumas):
    print("Pridėti naują dainą:")
    numeris = input("Eilės numeris: ")
    pavadinimas = input("Dainos pavadinimas: ")
    trukmė = input("Dainos trukmė (min:sek): ")
    naujas_daina = {"Eilės numeris": numeris, "Pavadinimas": pavadinimas, "Trukmė": trukmė}
    albumas["Dainų sąrašas"].append(naujas_daina)
    print(f"\nNauja daina '{pavadinimas}' pridėta į albumą!\n")
    
    print("\nAlbumo informacija:")
    print(f"Atlikėjas: {albumas['Atlikėjas']}")
    print(f"Pavadinimas: {albumas['Pavadinimas']}")
    print("\nDainų sąrašas:")
    prideti_daina(albumas)
