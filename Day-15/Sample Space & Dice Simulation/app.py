import itertools
import random

actions = ["Click", "Scroll", "Exit"]
sample_space = list(itertools.product(actions, repeat=2))

print("Sample Space:")
print(sample_space)
print("Total Outcomes:", len(sample_space))

event = [outcome for outcome in sample_space if "Click" in outcome]
print("Favorable Outcomes:", event)
print("Probability of at least one Click:", len(event) / len(sample_space))


trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    if die1 + die2 == 7:
        count_sum_7 += 1

print("Experimental Probability (Sum=7):", count_sum_7 / trials)
