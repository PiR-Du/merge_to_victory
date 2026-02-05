COMBINATIONS = {

    frozenset(["Villageois", "Forêt"]): ["Bois","Villageois", "Forêt"],
    frozenset(["Villageois", "Montagne"]): ["Pierre","Villageois", "Montagne"],
    frozenset(["Villageois", "Lac"]): ["Eau","Villageois", "Lac"],
    frozenset(["Planche", "Champ"]): ["Pré"],
    frozenset(["Eau", "Champ"]): ["Potager"],
    frozenset(["Pré", "Vache"]): ["Pré","Vache","Lait"],
    frozenset(["Pré", "Poule"]): ["Pré","Poule","Oeuf"],

    frozenset(["Bébé", "lait"]): ["Villageois"],

    frozenset(["Villageois", "Vache"]): ["Villageois","Viande"],
    frozenset(["Villageois", "Poule"]): ["Villageois","Viande"],

    frozenset(["Villageois", "Bois"]): ["Villageois","Planche"],

    frozenset(["Villageois", "Planche", "Planche"]): ["Villageois","Maison"],
    frozenset(["Villageois", "Villageois", "Maison"]): ["Villageois", "Villageois", "Maison",'Bébé'],

    frozenset(["Pierre", "Bois"]): ["Feu"],
}

LIEU = {
    "Lac" : ["Poisson"],
    "Forêt" : ["Baie","Vache","Poule"],
}

AGING_RULES = {
    "Baie": (3, "Baie pourrie"),
}
