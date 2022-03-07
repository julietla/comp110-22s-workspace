"""Example of boolean operators and, or, and not"""

# Example 1
rainy: bool = True
cold: bool = True

print(not cold)
print(not True)

print(rainy or cold)

print(rainy and cold)

if rainy and cold:
    print("Bring a jacket!")
else:
    print("Don't need a jacket!")

# Example 2
age: int = 19
height: float = 6.1

if age > 18 and height >= 5.0:
    print("You can ride!")
else:
    print("Try the teacups instead.")

age: int = 11
if age > 18 and height >= 5.0:
    print("You can ride!")
else:
    print("You can't ride.")