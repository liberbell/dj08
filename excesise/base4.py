
class CharacterAlreadyExistsException(Exception):
    pass

class AllCharacters:

    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        if name in cls.all_characters:
            raise CharacterAlreadyExistsException("character already exists.")
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_remove(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character:
    def __init__(self, name, hp, offense, defense):
        AllCharacters.character_append(name)
        self.name = name
        self.hp = hp
        self.offense = offense
        self.defense = defense

    def attack(self, enemy, critical_point=1):
        if self.hp <= 0:
            print("character is dead.")
            return
        apptack_point = self.offense - enemy.offense
        apptack_point = 1 if apptack_point <= 0 else apptack_point
        enemy.hp -= apptack_point * critical_point
        if enemy.hp <= 0:
            AllCharacters.character_remove(enemy.name)

    def critical_hit(self, enemy):
        self.attack(enemy, 2)

Character_a = Character("Bob", 10, 5, 3)
Character_b = Character("Eric", 8, 6, 2)

print(Character_b.hp)
Character_a.attack(Character_b)
print(Character_b.hp)