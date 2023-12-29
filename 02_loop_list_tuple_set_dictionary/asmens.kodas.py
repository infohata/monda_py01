while True:
    asmens_kodas = input("Įveskite asmens kodą arba 0, kad išeiti:")
    if asmens_kodas == "0":
        print("viso gero")
        break
    # ar visi skaičiai ir ar jų yra 11?
    if not asmens_kodas.isnumeric() or len(asmens_kodas) != 11:
        print("Neteisingas: turi būti 11 skaitmenų skaičius")
        continue
    menuo= int(asmens_kodas[3:5])
    print("mėnuo", menuo)
    if menuo <1 or menuo > 12:
        print("Neteisingas: gimimo mėnesio skaičius negali būti didesnis negu 12 arba lygus 0")
        continue
    diena = int(asmens_kodas[5:7])
    print("diena", diena)
    #TODO: patikrinti priklausomai nuo mėnėsio
    if diena <1 or diena > 31:
        print ("Neteisingas: gimimo dienos skaičius negali būti didesnė už 31 arba lygus 0")
        continue
    # paskutinio skaičiaus tikrinimas
    kontrolinis = 0
    daugikliai = "1234567891"
    kiti_daugikliai = "3456789123"
    for daugiklio_nr, skaitmuo in enumerate(asmens_kodas[:10]):
        kontrolinis += int(skaitmuo) * int (daugikliai[daugiklio_nr])
    print ("Kontrolinis: ", kontrolinis, kontrolinis % 11)
    if kontrolinis % 11 == 10:
        kontrolinis = 0
        for daugiklio_nr, skaitmuo in enumerate(asmens_kodas[:10]):
            kontrolinis += int(skaitmuo) * int(kiti_daugikliai[daugiklio_nr])
        print ("Kitas kontrolinis: ", kontrolinis, kontrolinis % 11)
    tikrinamas = kontrolinis % 11
    if tikrinamas == 10:
        tikrinamas = 0
    paskutinis = int(asmens_kodas[10])
    if paskutinis != tikrinamas:
        print("Neteisingas: paskutinis skaičius klaidingas")
        continue
    print("TEISINGAS")