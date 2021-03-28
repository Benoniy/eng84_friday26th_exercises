# Control Flow Age and Permission

### Time it should take:

30 Minutes

### Tasks:
  ***Create a simple program that uses control flow!***

* Potential outcomes for the program:
    1. You can vote and drive
    2. You can vote
    3. You can drive
    4. You can't legally drink, but your mates/uncles might have your back (bigger 16)
    5. You're too young, go back to school!
    
    
* User Stories:
    1. As a user I should be able to keep being prompted for input until I say 'exit'
    

* Starter Code:
    ```
    age = 19
    driver_license = True
    ```

### Acceptance Criteria:

* It's a program that run's continuously
* It Handles strings and integers
* It has an exit condition
* All the business logic works

### Solution:  
  ***The solution for this task is located in [control_flow_age_and_permission.py](https://github.com/Benoniy/eng84_friday26th_exercises/blob/main/control_flow_age_and_permission.py)***
1. First I created two functions to allow the user to supply their age and license status, these are used later on in the code.
    ```python
    # Gets the age of the user
    def get_age():
        age_input = input("What is your age?: ")
        while not age_input.isdigit():
            age_input = input("Please enter you age using digits: ")
        return int(age_input)
    
    
    # Gets the license status of the user
    def get_license():
        license_input = input("Do you have a driving license?: ")
        while not license_input.lower() in ("y", "n"):
            license_input = input("Please enter you answer using y or n: ")
        return license_input == "y"
    ```
2. Then I created a while loop to fulfill the user requirement that the program should be continuous until "exit" is used.
    ```python
    # Makes the program continuous
    while True:
        # Give the user an opportunity to exit the program
        user_input = input("\nLets see if you can vote! (continue or exit): ")
        if user_input.lower().count("exit") > 0:
            break
    ```
3. Finally, I called the functions that I had created before to supply information about the user and then used that to construct  
an if statement that houses the primary logic of the program.
    ```python
    # Get the users age and license status
    age = get_age()
    driver_license = get_license()

    if age < 16:  # If the user is too young to do anything
        print("You're too young, go back to school!")
        continue
    elif age < 18:  # If the user is just old enough to potentially drive but not drink
        print("You can't legally drink, but your mates/uncles might have your back (bigger 16)")
        if driver_license:
            print("You can legally drive")
    elif age > 17:  # If the user is old enough to drink and vote and potentially drive
        print("You can legally drink")
        print("You can legally vote", end=" ")
        if driver_license:
            print("and you can legally drive")
        else:
            print("but you cant legally drive")

    ```

-----------------------------------------------------------------
# Your Hero Story!

### Time it should take:

30-50 Minutes

### Tasks:
***You're going to write a story, cut it into sections and then store the sections in a python dictionary!***


1. Define a dictionary called story1, it should have the following keys:  
   'start', 'middle' and 'end'.  
   It should use the contents of your story as the values for the keys
   

2. Print the entire dictionary


3. Print the type of your dictionary


4. Print only the keys


5. Print only the values


6. Print the individual values using the keys (individually, lots of print commands)


7. Now let's add a new key:value pair.  
     `'hero': yourSuperHero`


### Acceptance Criteria:

* All 7 tasks are done
* Runs with no errors
* Tell a story  

### Solution:  
  ***The solution for this task is located in [hero_story.py](https://github.com/Benoniy/eng84_friday26th_exercises/blob/main/hero_story.py)***
1. I started by defining my dictionary which used 'start', 'middle' and 'end' for the keys and my story for the values.
    ```python
    story1 = {"start": "Once upon a time there was a sleepy boy",
              "middle": "everytime he slept he nightmares of SQL",
              "end": "one day he conquered SQL and avenged the maiden Ayaz"
              }
    ```
2. I then used a for loop to print the entire dictionary in a nice format
    ```python
    # Print the entire dictionary
    print("\nPrint the entire dictionary:")
    for key, val in story1.items():
        print(key + ":", val)
    ```
3. Next I printed the type of the dictionary using the type() method
    ```python
    # Print the type of your dictionary
    print("\nPrint the type of your dictionary:")
    print(type(story1))
    ```
4. Next I printed only the keys in a nice format using a for loop
    ```python
    # Print only the keys
    print("\nPrint only the keys:")
    for key in story1.keys():
        print(key)
    ```
5. In the very same way I also printed the values in a nice format
    ```python
    # Print only the values
    print("\nPrint only the values:")
    for val in story1.values():
        print(val)
    ```
6. Next using individual print statements, I printed each part of the story in order 
    ```python
    # Print the individual values using the keys (individually, lots of print commands)
    print("\nPrint the individual values using the keys:")
    print(story1["start"])
    print(story1["middle"])
    print(story1["end"])
    ```
7. Finally, I added a new key value pair to the dictionary to hold the name of my hero and then printed it
    ```python
    # Now let's add a new key:value pair
    story1["hero"] = "Arun"
    print("hero: " + story1["hero"])
    ```
--------------------------------------------------------------------