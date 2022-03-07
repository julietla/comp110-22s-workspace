"""Exs of using lists"""


from random import randint
# Generate random integer, want between 1 and 6

rolls: list[int] = list()
# Want to express list of int values
rolls.append(1)
rolls.append(3)
print(rolls)

rolls.append(randint(1,6))
rolls.append(randint(1,6))
print(rolls)

print(rolls[1])

# Access length of list (number of items)
print(rolls[len(rolls) - 1])
last_index: int = (rolls[len(rolls) - 1])
print(rolls[last_index])

