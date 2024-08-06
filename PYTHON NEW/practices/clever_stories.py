# Collect words from the user
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
exclamation = input("Enter an exclamation: ").capitalize()
verb2 = input("Enter another verb: ")
verb3 = input("Enter one more verb: ")

# Create the story with the user's words
story = f"The other day, I was really in trouble. It all started when I saw a very "\
        "{adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all "\
        "I could think to do was to {verb2} over and over. Miraculously, "\
        "that caused it to stop, but not before it tried to {verb3} "\
        "right in front of my family."


# Display the story
print("\nHere is your story:\n")
print(story)
