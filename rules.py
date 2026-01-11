COMBINATIONS = {
    frozenset(["Villageois", "Bois"]): "Planche",
    frozenset(["Villageois", "Pierre"]): "Brique",
    frozenset(["Planche", "Planche"]): "Maison",
    frozenset(["Villageois", "Maison"]): "Enfant",
    frozenset(["Enfant", "Temps"]): "Villageois",

    frozenset(["Arbre", "Temps"]): "Bois",
    frozenset(["Champ", "Temps"]): "Baie",
    frozenset(["Rivière", "Villageois"]): "Poisson",

    frozenset(["Villageois", "Hache"]): "Bois",
    frozenset(["Villageois", "Pioche"]): "Pierre",

    frozenset(["Bois", "Feu"]): "Charbon"
}


AGING_RULES = {
    "Baie": (3, "Baie pourrie"),
}
