import csv

# Cette fonction charge un fichier CSV et le retourne sous forme de liste de listes.
def load_csv(filename):
    with open(filename, "r", encoding="utf-8") as f:
        result_list = list(csv.reader(f, delimiter=";"))
        del result_list[0]
        return result_list

# Charger les données des fichiers CSV dans des variables.
villes = load_csv("villes.csv")
pays = load_csv("pays.csv")
langues = load_csv("langues.csv")

# Fonction pour trouver les villes dont le nom commence par "Pa".
def villes_commencent_par_pa():
    return [ville for ville in villes if ville[1].lower().startswith("pa")]

# Fonction pour trouver les pays en Amérique du Sud.
def pays_amerique_du_sud():
    return [p for p in pays if p[2] == "South America"]

# Fonction pour trouver les villes en Europe dont le nom commence par "Pa".
def villes_europe_commencent_par_pa():
    # Récupération des codes des pays européens.
    codes_pays_europe = [p[0] for p in pays if p[2] == "Europe"]
    # Filtrage des villes dont le pays est en Europe et le nom commence par "Pa".
    return [v for v in villes if v[2] in codes_pays_europe and v[1].lower().startswith("pa")]

# Fonction pour trouver les villes en Europe avec une population de plus de 100 000 habitants.
def villes_plus_100k_europe():
    # Récupération des codes des pays européens.
    codes_pays_europe = [p[0] for p in pays if p[2] == "Europe"]
    # Filtrage des villes dont le pays est en Europe et la population est supérieure à 100 000.
    return [v for v in villes if v[2] in codes_pays_europe and int(v[4]) > 100000]

# Fonction pour compter le nombre de formes de gouvernement uniques parmi les pays.
def nombre_formes_gouvernements():
    # Utilisation d'un ensemble pour obtenir les formes de gouvernement uniques.
    return len(set(p[11] for p in pays))

# Fonction pour compter le nombre total de pays.
def nombre_pays():
    return len(pays)

# Fonction pour trouver les pays où le français est une langue parlée.
def pays_parlent_francais():
    # Utilisation de la compréhension de liste pour filtrer les pays parlant français.
    return [p for p in pays if any(l[1] == "French" for l in langues if l[0] == p[0])]

# Fonction pour trouver les pays où le français est une langue officielle.
def pays_francais_officiel():
    # Utilisation de la compréhension de liste pour filtrer les pays où le français est une langue officielle.
    return [p for p in pays if any(l[1] == "French" and l[2] == "T" for l in langues if l[0] == p[0])]

# Fonction pour trouver les villes en Afrique dans des pays où le français est une langue officielle et avec une population de moins de 100 000 habitants.
def villes_moins_100k_afrique_francais_officiel():
    # Récupération des codes des pays africains où le français est officiel.
    codes_pays_afrique_francais_officiel = [
        p[0] for p in pays
        if p[2] == "Africa" and any(
            l[1] == "French" and l[2] == "T" for l in langues if l[0] == p[0]
        )
    ]
    # Filtrage des villes en Afrique avec les critères spécifiés.
    return [v for v in villes if v[2] in codes_pays_afrique_francais_officiel and int(v[4]) < 100000]

# Fonction pour trouver les pays en Amérique du Sud avec une population de plus de 10 millions et une forme de gouvernement républicaine.
def pays_amerique_sud_plus_10M_republicain():
    # Utilisation de la compréhension de liste pour filtrer les pays avec les critères spécifiés.
    return [p for p in pays if p[2] == "South America" and int(p[6]) > 10000000 and "Republic" in p[11]]

# Fonction pour trouver les villes en Amérique du Nord dans des pays où l'espagnol est parlé et avec une population de plus de 100 000 habitants.
def villes_plus_100k_nord_americains_espagnol():
    # Récupération des codes des pays nord-américains où l'espagnol est parlé.
    codes_pays_nord_americains_espagnol = [
        p[0] for p in pays
        if p[2] == "North America" and any(
            l[1] == "Spanish" for l in langues if l[0] == p[0]
            )
        ]
    # Filtrage des villes dans les pays nord-américains avec les critères spécifiés.
    return [v for v in villes if v[2] in codes_pays_nord_americains_espagnol and int(v[4]) > 100000]

# Fonction pour calculer la surface totale des pays en Europe.
def surface_europe():
    # Utilisation de la fonction sum() pour calculer la somme des surfaces.
    return sum(float(p[4]) for p in pays if p[2] == "Europe")

# Fonction pour trouver la surface de la Polynésie.
def surface_polynesie():
    # Recherche de la surface de la Polynésie en parcourant la liste des pays.
    for p in pays:
        if "Polynesia" in p[1]:
            return float(p[4])
    return None

# Fonction pour trouver les pays en Océanie avec une superficie de plus de 10 000 km².
def pays_oceanie_plus_10k_km2():
    # Utilisation de la compréhension de liste pour filtrer les pays avec les critères spécifiés.
    return [p for p in pays if p[2] == "Oceania" and float(p[4]) > 10000]

# Fonction pour trouver les langues officielles des pays en Europe de l'Est.
def langues_officielles_europe_est():
    # Récupération des codes des pays en Europe de l'Est.
    codes_pays_europe_est = [p[0] for p in pays if p[3] == "Eastern Europe"]
    # Utilisation de l'ensemble pour obtenir les langues officielles uniques.
    return set(l[1

] for l in langues if l[0] in codes_pays_europe_est and l[2] == "T")

# Fonction pour calculer la population moyenne des pays en Asie.
def population_moyenne_pays_asie():
    # Filtrage des populations des pays en Asie et calcul de la moyenne.
    populations = [int(p[6]) for p in pays if p[2] == "Asia"]
    return sum(populations) / len(populations)

# Fonction pour calculer la population moyenne des villes dans les pays en Asie.
def population_moyenne_villes_pays_asie():
    # Récupération des codes des pays en Asie.
    codes_pays_asie = [p[0] for p in pays if p[2] == "Asia"]
    # Filtrage des populations des villes dans les pays en Asie et calcul de la moyenne.
    populations = [int(v[4]) for v in villes if v[2] in codes_pays_asie]
    return sum(populations) / len(populations)

# Fonction pour trouver les capitales des pays en Europe par ordre alphabétique.
def capitales_europe_ordre_alphabetique():
    # Récupération des codes des pays européens.
    codes_pays_europe = [p[0] for p in pays if p[2] == "Europe"]
    # Recherche des capitales des pays européens et tri par ordre alphabétique.
    capitales = [
        next(v[1] for v in villes if v[0] == p[13])
        for p in pays if p[0] in codes_pays_europe
    ]
    return sorted(capitales)

# Fonction pour trouver les villes dans les pays en Afrique ayant une population de plus de 3 millions.
def villes_pays_afrique_capitale_plus_3M():
    # Récupération des codes des pays en Afrique avec des villes de plus de 3 millions d'habitants.
    codes_pays_afrique_capitale_plus_3M = [
        p[0] for p in pays
        if p[2] == "Africa"
        and any(
            int(v[4]) > 3000000 for v in villes if v[0] == p[13]
            )
        ]
    # Filtrage des villes avec les critères spécifiés.
    return [v for v in villes if v[2] in codes_pays_afrique_capitale_plus_3M]

# Fonction pour trouver les pays en Amérique du Nord ayant obtenu leur indépendance avant 1912 où le portugais est parlé et avec plus de 49 villes.
def pays_amerique_nord_independance_avant_1912_portugais_plus_49_villes():
    # Récupération des codes des pays en Amérique du Nord ayant obtenu leur indépendance avant 1912 où le portugais est parlé.
    codes_pays_amerique_nord_independance_avant_1912_portugais = [
        p[0] for p in pays
        if p[2] == "North America" and p[5] != "NULL" and int(p[5]) < 1912
        and any(
            l[1] == "Portuguese" for l in langues if l[0] == p[0]
            )
        ]
    # Filtrage des pays avec plus de 49 villes.
    return [
        p for p in pays
        if p[0] in codes_pays_amerique_nord_independance_avant_1912_portugais
        and len([v for v in villes if v[2] == p[0]]) > 49
    ]

# Liste de toutes les fonctions à exécuter.
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
    surface_europe,
    surface_polynesie,
    pays_oceanie_plus_10k_km2,
    langues_officielles_europe_est,
    population_moyenne_pays_asie,
    population_moyenne_villes_pays_asie,
    capitales_europe_ordre_alphabetique,
    villes_pays_afrique_capitale_plus_3M,
    pays_amerique_nord_independance_avant_1912_portugais_plus_49_villes
]

# Exécuter chaque fonction et afficher le résultat.
for fonction in fonctions:
    print(fonction.__name__)
    print(fonction())
    print("\n")