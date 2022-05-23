import random

random.seed(42)
num_families = 100_000
boys_per_family = [0] * num_families
for i in range(num_families):
    while random.choice(["M", "F"]) == "M":
        boys_per_family[i] += 1

total_boys = sum(boys_per_family)
ratio = total_boys / num_families
print(f"The male-to-female ratio in the next generation is {ratio:.2f}.")
