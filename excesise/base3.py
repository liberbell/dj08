from random import randint

def generator_enemy_hand():
    while True:
        yield "1"
        yield "2"
        yield "3"

def is_win(my_hand, enemy_hand):
    if my_hand == "1" and enemy_hand == "2":
        return True
    elif my_hand == "2" and enemy_hand == "3":
        return True
    elif my_hand == "3" and enemy_hand == "1":
        return True
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
    enemy_hand = str(randint(1, 3))
    print("Your hand: {}. Computer hand: {}".format(hand_dict.get(my_hand), hand_dict.get(enemy_hand)))
    if my_hand == enemy_hand:
        print("equal")
    elif is_win(my_hand, enemy_hand):
        print("win")
        break
    else:
        lose_count += 1
        if lose_count == 3:
            print("lost")
            break
        else:
            print("lost again.")

