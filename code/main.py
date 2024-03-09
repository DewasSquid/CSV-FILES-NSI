import csv

def load_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return list(csv.reader(f, delimiter=";"))


villes = load_csv("villes.csv")
pays = load_csv("pays.csv")
langues = load_csv("langues.csv")


def villes_commencent_par_pa():
    return [ville for ville in villes if ville[1].lower().startswith("pa")]


def pays_amerique_du_sud():
    return [p for p in pays if p[2] == "South America"]


def villes_europe_commencent_par_pa():
    codes_pays_europe = [p[0] for p in pays if p[2] == "Europe"]
    return [
        v for v in villes if v[2] in codes_pays_europe and v[1].lower().startswith("pa")
    ]


def villes_plus_100k_europe():
    codes_pays_europe = [p[0] for p in pays if p[2] == "Europe"]
    return [v for v in villes if v[2] in codes_pays_europe and int(v[4]) > 100000]


def nombre_formes_gouvernements():
    return len(set(p[11] for p in pays))


def nombre_pays():
    return len(pays)


def pays_parlent_francais():
    return [p for p in pays if any(l[1] == "French" for l in langues if l[0] == p[0])]


def pays_francais_officiel():
    return [
        p
        for p in pays
        if any(l[1] == "French" and l[2] == "T" for l in langues if l[0] == p[0])
    ]


def villes_moins_100k_afrique_francais_officiel():
    codes_pays_afrique_francais_officiel = [
        p[0]
        for p in pays
        if p[2] == "Africa"
        and any(l[1] == "French" and l[2] == "T" for l in langues if l[0] == p[0])
    ]
    return [
        v
        for v in villes
        if v[2] in codes_pays_afrique_francais_officiel and int(v[4]) < 100000
    ]


def pays_amerique_sud_plus_10M_republicain():
    return [
        p
        for p in pays
        if p[2] == "South America" and int(p[6]) > 10000000 and "Republic" in p[11]
    ]


def villes_plus_100k_nord_americains_espagnol():
    codes_pays_nord_americains_espagnol = [
        p[0]
        for p in pays
        if p[2] == "North America"
        and any(l[1] == "Spanish" for l in langues if l[0] == p[0])
    ]
    return [
        v
        for v in villes
        if v[2] in codes_pays_nord_americains_espagnol and int(v[4]) > 100000
    ]


def surface_europe():
    return sum(float(p[4]) for p in pays if p[2] == "Europe")


def surface_polynesie():
    for p in pays:
        if "Polynesia" in p[1]:
            return float(p[4])
    return None


def pays_oceanie_plus_10k_km2():
    return [p for p in pays if p[2] == "Oceania" and float(p[4]) > 10000]


def langues_officielles_europe_est():
    codes_pays_europe_est = [p[0] for p in pays if p[3] == "Eastern Europe"]
    return set(l[1] for l in langues if l[0] in codes_pays_europe_est and l[2] == "T")


def population_moyenne_pays_asie():
    populations = [int(p[6]) for p in pays if p[2] == "Asia"]
    return sum(populations) / len(populations)


def population_moyenne_villes_pays_asie():
    codes_pays_asie = [p[0] for p in pays if p[2] == "Asia"]
    populations = [int(v[4]) for v in villes if v[2] in codes_pays_asie]
    return sum(populations) / len(populations)


def capitales_europe_ordre_alphabetique():
    codes_pays_europe = [p[0] for p in pays if p[2] == "Europe"]
    capitales = [
        next(v[1] for v in villes if v[0] == p[13])
        for p in pays
        if p[0] in codes_pays_europe
    ]
    return sorted(capitales)


def villes_pays_afrique_capitale_plus_3M():
    codes_pays_afrique_capitale_plus_3M = [
        p[0]
        for p in pays
        if p[2] == "Africa"
        and any(int(v[4]) > 3000000 for v in villes if v[0] == p[13])
    ]
    return [v for v in villes if v[2] in codes_pays_afrique_capitale_plus_3M]


def pays_amerique_nord_independance_avant_1912_portugais_plus_49_villes():
    codes_pays_amerique_nord_independance_avant_1912_portugais = [
        p[0]
        for p in pays
        if p[2] == "North America"
        and p[5] != "NULL"
        and int(p[5]) < 1912
        and any(l[1] == "Portuguese" for l in langues if l[0] == p[0])
    ]
    return [
        p
        for p in pays
        if p[0] in codes_pays_amerique_nord_independance_avant_1912_portugais
        and len([v for v in villes if v[2] == p[0]]) > 49
    ]


fonctions = [
    villes_commencent_par_pa,
    pays_amerique_du_sud,
    villes_europe_commencent_par_pa,
    villes_plus_100k_europe,
    nombre_formes_gouvernements,
    nombre_pays,
    pays_parlent_francais,
    pays_francais_officiel,
    villes_moins_100k_afrique_francais_officiel,
    pays_amerique_sud_plus_10M_republicain,
    villes_plus_100k_nord_americains_espagnol,
    surface_europe, surface_polynesie,
    pays_oceanie_plus_10k_km2,
    langues_officielles_europe_est,
    population_moyenne_pays_asie,
    population_moyenne_villes_pays_asie,
    capitales_europe_ordre_alphabetique,
    villes_pays_afrique_capitale_plus_3M,
    pays_amerique_nord_independance_avant_1912_portugais_plus_49_villes
]

for fonction in fonctions:
    print(fonction.__name__)
    print(fonction())
    print("\n")
