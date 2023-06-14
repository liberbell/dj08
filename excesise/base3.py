
def generator_enemy_hand():
    while True:
        yield "1"
        yield "2"
        yield "3"

hand_dict = {"1": "rock", "2": "scissors", "3": "paper"}

lose_count = 0
enemy_hands = generator_enemy_hand()