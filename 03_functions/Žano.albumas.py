albumas = {
    'pavadinimas': '',
    'atlikejas': '',
    'takeliai': []
}

def uzpildyti_informacija(pavadinimas, atlikejas):
    albumas['pavadinimas'] = pavadinimas
    albumas['atlikejas'] = atlikejas

def prideti_takeli(pavadinimas, trukme):
    takelis = {'pavadinimas': pavadinimas, 'trukme': trukme}
    albumas['takeliai'].append(takelis)

def istrinti_takeli(takelio_numeris):
    if 0 <= takelio_numeris < len(albumas['takeliai']):
        albumas['takeliai'].pop(takelio_numeris)
    else:
        print("Takelio numeris neteisingas")

def perziureti_albuma():
    print(f"Albumo pavadinimas: {albumas['pavadinimas']}")
    print(f"Atlikėjas: {albumas['atlikejas']}")
    print(f"Takelių kiekis: {len(albumas['takeliai'])}")
    print(f"Bendra takelių trukmė: {bendra_trukme()} sekundės")

def perziureti_dainas():
    sorted_takeliai = sorted(albumas['takeliai'], key=lambda x: x['pavadinimas'])
    for indeksas, takelis in enumerate(sorted_takeliai):
        print(f"{indeksas + 1}. {takelis['pavadinimas']} - {formatuoti_trukme(takelis['trukme'])}")

def bendra_trukme():
    return sum(takelis['trukme'] for takelis in albumas['takeliai'])

def formatuoti_trukme(trukme):
    minutes, seconds = divmod(trukme, 60)
    return f"{minutes}:{seconds:02d}"

uzpildyti_informacija("Geriausios Dainos", "Atlikėjas X")
prideti_takeli("Daina A", 180)
prideti_takeli("Daina B", 150)
prideti_takeli("Daina C", 210)

perziureti_albuma()
print("\nDainos:")
perziureti_dainas()

