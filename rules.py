COMBINATIONS = {

    frozenset(["Villageois", "Forêt"]): ["Bois","Villageois", "Forêt"],
    frozenset(["Villageois", "Lac"]): ["Eau","Villageois", "Lac"],

    frozenset(["Villageois", "Bois"]): ["Planche","Villageois"],

}

LIEU = {
    "Lac" : ["Poisson"],
    "Forêt" : ["Fruit","Animal"],
}

AGING_RULES = {
    "Baie": (3, "Baie pourrie"),
}
