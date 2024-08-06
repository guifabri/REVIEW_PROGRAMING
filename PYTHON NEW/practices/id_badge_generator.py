print ("Please enter the following information: ")
print ()
first = input ("First name: ")
last = input ("Last name: ")
email = input ("Enail address: ")
phone = input ("Phone number: ")
job_tittle = input ("Job tittle: ")
id_number = input ("ID Number: \n")

# Ask for the additional information
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month = input("Starting Month: ")
training = input("Completed additional training? ")

# This is a comment
print("\nThe ID Card is: ")
print ("--------------------------------")
print(f"{last.upper() }, {first.capitalize() }")
print(f"ID: {id_number}")
print()
print (email.lower() )
print(phone.lower() )
print("---------------------------------")