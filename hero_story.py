

story1 = {"start": "Once upon a time there was a sleepy boy",
          "middle": "everytime he slept he nightmares of SQL",
          "end": "one day he conquered SQL and avenged the maiden Ayaz"
          }


# Print the entire dictionary
print(story1)

# Print the type of your dictionary
print(type(story1))

# Print only the keys
print(story1.keys())

# Print only the values
print(story1.values())

# Print the individual values using the keys (individually, lots of print commands)
print(story1["start"])
print(story1["middle"])
print(story1["end"])

# Now let's add a new key:value pair
story1["hero"] = "Arun"
