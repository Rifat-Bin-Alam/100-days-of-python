friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#my soln
import random

person = random.randint(0,4)

print(f"{friends[person]}")

#soln 1
print(random.choice(friends))

