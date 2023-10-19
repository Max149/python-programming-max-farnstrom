import random

total_rolls = 1000000

def simulate_rolls(number_of_dice, n_sides_of_dice=6):
    results = {i: 0 for i in range(number_of_dice, number_of_dice * n_sides_of_dice + 1)}
    
    for _ in range(total_rolls):
        total = sum(random.choice(range(1, n_sides_of_dice + 1)) for _ in range(number_of_dice))
        results[total] += 1

    return results


dice_results = simulate_rolls(5)
print("Results:")
for outcome, count in dice_results.items():
    print(f"{outcome}: {count}")