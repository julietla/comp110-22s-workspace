"""Ex of for in syntax"""

names: list[str] = ["Kris", "Kaki", "Ezri", "Marc"]


# Ex iterating through names with while loop
print("while output:")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1


# Using for in loop to iterate through same loop as while loop above
print("for...in output:")
for name in names:
    print(name)

for x in [1, 2, 3]:
   print(x)


ys: list[int] = [110, 120]
for y in ys:
    print(y)


i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
    y: int = ys[i]
    print(y)
    i += 1