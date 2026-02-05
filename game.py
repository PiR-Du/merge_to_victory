from cards import Card
from rules import COMBINATIONS, AGING_RULES, LIEU
import json
import random

class Game:
    def __init__(self):

        self.card_defs = self.load_cards()

        self.cards = []
        self.next_id = 1
        self.add_card("Forêt")
        self.add_card("Lac")
        self.add_card("Villageois")
        self.add_card("Villageois")
        self.status = "EN COURS"

    def load_cards(self):
        with open("cards.json", encoding="utf-8") as f:
            data = json.load(f)["cards"]

        return {card["name"]: card for card in data}


    def add_card(self, name):
        labels = self.card_defs[name]

        self.cards.append(
            Card(
                id=self.next_id,
                name=name,
                type=labels["type"],
            )
        )
        self.next_id += 1

    def get_card(self, card_id):
        return next(c for c in self.cards if c.id == card_id)

    def combine(self, id1, id2):
        c1 = self.get_card(id1)
        c2 = self.get_card(id2)

        key = frozenset([c1.name, c2.name])
        if key in COMBINATIONS:
            results = COMBINATIONS[key]
            self.cards.remove(c1)
            self.cards.remove(c2)
            for result in results :
                self.add_card(result)
            # Bonus
            if c1.type == "lieu" :
                for bonus in LIEU[c1.name] :
                    chance = random.randrange(5)
                    if chance == 1 :
                        self.add_card(bonus )
            if c2.type == "lieu" :
                for bonus in LIEU[c2.name] :
                    chance = random.randrange(5)
                    if chance == 1 :
                        self.add_card(bonus)

    def tick(self):
        for card in self.cards[:]:
            card.age += 1
            if card.name in AGING_RULES:
                limit, new_name = AGING_RULES[card.name]
                if card.age >= limit:
                    card.name = new_name
                    card.age = 0
        if self.is_victory():
            self.status = "VICTOIRE 🎉"
        elif self.is_defeat():
            self.status = "DÉFAITE 💀"
        else:
            self.status = "EN COURS"

    
    def has_card(self, name, count=1):
        return sum(c.name == name for c in self.cards) >= count

    def is_victory(self):
        return self.has_card("Maison", 3)

    def is_defeat(self):
        return not self.has_card("Villageois")

