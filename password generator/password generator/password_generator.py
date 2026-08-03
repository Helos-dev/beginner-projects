#PASSWORD GENERATOR
import random 
import string

length = int(input("inserisci il numero di caratteri della tua password: "))

char =  (
    string.ascii_letters+
    string.ascii_lowercase+
    string.ascii_uppercase+
    string.digits+
    string.punctuation
)

password = "".join(
    random.choice(char)
    for _ in range(length)

)

print("Ecco la tua password: ")
print(password)
