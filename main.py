#LIBRARIES IMPORTATION
import random 
import string
#LENGTH AND CHARACTER DEFINITION
length = int(input("Enter the length of the password: "))
char = ( 
        string.ascii_letters+
        string.ascii_lowercase+
        string.ascii_uppercase+
        string.digits+
        string.punctuation
)
#SITE REQUEST
site = input("Please write the app or site you need the password for: ")

#GENERATING THE PASSWORD
password = "".join(
    random.choice(char)
    for _ in range(length)

)

with open("Passwords.txt", "a") as f:
    f.write(f"{site} = {password}\n")

print(f"Password generata per {site} e salvata nel file.")

 

