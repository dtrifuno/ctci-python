import random

poison_bottle = random.randint(0, 999)
bottles = [False] * 1000
bottles[poison_bottle] = True

results = [False] * 10

for i, poisoned in enumerate(bottles):
    if not poisoned:
        continue

    for j in range(10):
        if i & (0b1 << j):
            results[j] = True

results.reverse()
strips_poison_bottle = int("".join(["1" if result else "0" for result in results]), 2)

print(f"The poisoned bottle is {poison_bottle}.")
print(f"The test strips results are {results}.")
print(f"That spells out bottle {strips_poison_bottle}.")
