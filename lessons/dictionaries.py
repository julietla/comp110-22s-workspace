"""Demonstations of dictionary capabilities."""

# Declaring type of dictionary
schools: dict[str, int]

# Initialize to empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "lookup"
# Use single quote within the double quote for f string
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

if "Duke" in schools:
    print(f"Duke is present: {is_duke_present}")
else: 
    print("Key is not in schools.")

# Update/reassign a key-value pair
schools["UNC"] = 20000  # value changed
schools["NCSU"] += 200  # adding 200 to original value

print(schools)

# Deminstration of dictonary literals
# Empty dictionary literal
schools = {}  # same as dict()
print(schools)

# Alternatiely, initialize key-value pairs
# schools = ("UNC": 19400, "Dukie": 6717, "NCSU": 26150)
# print(schools)

# What happens when a key does not exist?
# print(schools["UNCC"])
# Leads to KeyError: 'UNCC'

# Example looping over the keys of a dict
for key in schools:
    print(f"Key: {key} -> Value: {schools[key]}")