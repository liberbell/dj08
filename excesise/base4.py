
class AllCharacters:

    all_characters = []
    alive_characters = []
    dead_characters = []

    @classmethod
    def character_append(cls, name):
        cls.all_characters.append(name)
        cls.alive_characters.append(name)

    @classmethod
    def character_remove(cls, name):
        cls.dead_characters.append(name)
        cls.alive_characters.remove(name)

class Character: