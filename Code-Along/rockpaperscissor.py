from random import choice

SIGNS = ["rock", "paper", "scissors"]

def main():
    print(f"welcome to the {', '.join(SIGNS)} game.")
    print_rules()
    number_of_rounds = select_number_of_rounds()

    print(f"\nbest of {number_of_rounds}, wins. lets start\n")
    
    game_loop(number_of_rounds)

def print_rules():
    print("\nRules: Each player picks a sign:")
    for winners, losers in zip([0, 1, 2], [2, 0, 1]):
        print(f"{SIGNS[winners]} wins over {SIGNS[losers]}.")

        

def select_number_of_rounds():
    while True:
        try:
            rounds = int(input("Select number of rounds: "))
            if 0 <= rounds <= 10: return rounds
            else: print("rounds must be between 1 and 10")
        
        except ValueError:
            print("number of rounds must be an int.")

def game_loop(number_of_rounds):
    for current_round in range(1, number_of_rounds + 1):
        print(f"ROUND {current_round}: ")
        sign_player_a = get_sign_from_user()
        sign_player_b = get_sign_from_computer()

        print(f"Computer picks {sign_player_b}")
        
        if is_draw(sign_player_a, sign_player_b):
            print("Draw")
        elif wins_over(sign_player_a, sign_player_b):
            print("player wins")
        else:
            print("computer wins")



def get_sign_from_user():
    while True:
        sign = input("Pick a sign: ").strip().lower()
        if sign in SIGNS: 
            return sign
        else: 
            print(f"you must pick either of {', '.join(SIGNS)}")

def get_sign_from_computer():
    return choice(SIGNS)

def is_draw(sign_a, sign_b):
    return sign_a == sign_b

    
def wins_over(sign_a, sign_b):
    for winners, losers in zip([0, 1, 2], [2, 0, 1]):
        if sign_a == SIGNS[winners] and sign_b == SIGNS[losers]: return True

    return False


main()