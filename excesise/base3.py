
def generator_enemy_hand():
    while True:
        yield "1"
        yield "2"
        yield "3"

def is_win(my_hand, enemy_hand):
    if my_hand == "1" and enemy_hand == "2":
        return True
    elif my_hand == "1" and enemy_hand == "3":
        return False

hand_dict = {
    "1": "rock",
    "2": "scissors",
    "3": "paper"
    }

lose_count = 0
enemy_hands = generator_enemy_hand()

while True:
    my_hand = input("What is your hand? 1:rock, 2:scissors, 3:paper:")
    if my_hand not in ("1", "2", "3"):
        print("Wrong input.")
        continue
    enemy_hand = next(enemy_hands)
    print("Your hand: {}. Computer hand: {}".format(hand_dict.get(my_hand), hand_dict.get(enemy_hand)))
    if my_hand == enemy_hand