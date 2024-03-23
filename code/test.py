import csv

def ouvrir_fichier(fichier):
    fichier = open(fichier, "r", encoding="utf-8")
    return list(csv.reader(fichier, delimiter=";"))

langues = ouvrir_fichier("langues.csv")
villes = ouvrir_fichier("villes.csv")
pays = ouvrir_fichier("pays.csv")

def question_1():
    villes_pa = []
    for ville in villes:
        if ville[1].startswith("Pa"):
            villes_pa.append(ville)
    print(villes_pa)
question_1()

def question_2():
    pays_sud_am = []
    for p in pays:
        if p[2] == "South America":
            pays_sud_am.append(p)
    print(pays_sud_am)
question_2()

def question_3():
    codes_pays_europe = []
    for p in pays:
        if p[2] == "Europe":
            codes_pays_europe.append(p[0])
    villes_pa_europe = []
    for v in villes:
        if v[2] in codes_pays_europe and v[1].lower().startswith("pa"):
            villes_pa_europe.append(v)
    print(villes_pa_europe)
question_3()

def question_4():
    codes_pays_europe = []
    for p in pays:
        if p[2] == "Europe":
            codes_pays_europe.append(p[0])
    villes_100k_europe = []
    for v in villes:
        if v[2] in codes_pays_europe and int(v[4]) > 100000:
            villes_100k_europe.append(v)
    print(villes_100k_europe)
question_4()

def question_5():
    formes_gouvernements = set()
    for p in pays:
        formes_gouvernements.add(p[11])
    print(len(formes_gouvernements))
question_5()

def question_6():
    print(len(pays))
question_6()

def question_7():
    pays_francais = []
    for p in pays:
        for l in langues:
            if l[0] == p[0] and l[1] == "French":
                pays_francais.append(p)
    print(pays_francais)
question_7()


def question_8():
    pays_francais_off = []
    for p in pays:
        for l in langues:
            if l[0] == p[0] and l[1] == "French" and l[2] == "T":
                pays_francais_off.append(p)
    print(pays_francais_off)
question_8()

def question_9():
    codes_pays_afrique_francais_off = []
    for p in pays:
        if p[2] == "Africa":
            for l in langues:
                if l[0] == p[0] and l[1] == "French" and l[2] == "T":
                    codes_pays_afrique_francais_off.append(p[0])
    villes_100k_afrique_francais_off = []
    for v in villes:
        if v[2] in codes_pays_afrique_francais_off and int(v[4]) < 100000:
            villes_100k_afrique_francais_off.append(v)
    print(villes_100k_afrique_francais_off)
question_9()

def question_10():
    pays_sud_am_10M_rep = []
    for p in pays:
        if p[2] == "South America" and int(p[6]) > 10000000 and "Republic" in p[11]:
            pays_sud_am_10M_rep.append(p)
    print(pays_sud_am_10M_rep)
question_10()
