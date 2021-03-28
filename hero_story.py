

story1 = {"start": "Once upon a time there was a sleepy boy",
          "middle": "everytime he slept he nightmares of SQL",
          "end": "one day he conquered SQL and avenged the maiden Ayaz"
          }


# Print the entire dictionary
print("\nPrint the entire dictionary:")
for key, val in story1.items():
    print(key + ":", val)

# Print the type of your dictionary
print("\nPrint the type of your dictionary:")
print(type(story1))

# Print only the keys
print("\nPrint only the keys:")
for key in story1.keys():
    print(key)

# Print only the values
print("\nPrint only the values:")
for val in story1.values():
    print(val)

# Print the individual values using the keys (individually, lots of print commands)
print("\nPrint the individual values using the keys:")
print(story1["start"])
print(story1["middle"])
print(story1["end"])

# Now let's add a new key:value pair
story1["hero"] = "Arun"
print("hero: " + story1["hero"])
