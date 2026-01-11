from cards import Card
from rules import COMBINATIONS, AGING_RULES

class Game:
    def __init__(self):
        self.cards = []
        self.next_id = 1
        self.add_card("Villageois", "human")
        self.add_card("Bois", "resource")
        self.add_card("Baie", "food")
        self.status = "EN COURS"

    def add_card(self, name, type_):
        self.cards.append(Card(self.next_id, name, type_))
        self.next_id += 1

    def get_card(self, card_id):
        return next(c for c in self.cards if c.id == card_id)

    def combine(self, id1, id2):
        c1 = self.get_card(id1)
        c2 = self.get_card(id2)

        key = frozenset([c1.name, c2.name])
        if key in COMBINATIONS:
            result = COMBINATIONS[key]
            self.cards.remove(c1)
            self.cards.remove(c2)
            self.add_card(result, "crafted")
            

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

