
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

    def attack(self, enemy):
        apptack_point = self.offense - enemy.offense
        apptack_point = 1 if apptack_point <= 0 else apptack_point
        enemy.hp -= apptack_point
        if enemy.hp <= 0:
            AllCharacters.character_remove(enemy.name)