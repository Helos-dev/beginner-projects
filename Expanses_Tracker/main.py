#LIBRARIES IMPORTATION
import datetime
import modulo

#LOGIC
print("EXPENSES TRACKER")

#LETTURA SALDO SALVATO
try:
    with open("saldo.txt", "r") as f:
        conto = int(f.read())
    print(f"Saldo trovato: {conto}")
except FileNotFoundError:
    conto = int(input("Nessun saldo salvato. Inserisci i fondi disponibili: "))

scelta = int(input("Ecco le funzioni disponibili: \n 1 Mostra Saldo \n 2 Aggiungi al conto \n 3 Registra Spesa \n Scegli l'operazione da eseguire: "))

oggi = datetime.date.today()

#LOOPS
if scelta == 1:
    modulo.mostraconto(conto)

elif scelta == 2:
    aggiunta = int(input("Scegli la somma da aggiungere al tuo conto: "))
    conto = modulo.aggiungiconto(aggiunta, conto)

    with open("Expanses.txt", "a") as f:
        f.write(f"{oggi} | RICARICA | +{aggiunta} | Nuovo saldo: {conto}\n")

elif scelta == 3:
    spesa_val = int(input("Importo della spesa: "))
    motivazione = input("Inserisci la motivazione dell'acquisto: ")
    conto = modulo.spesa(spesa_val, motivazione, oggi, conto)

    with open("Expanses.txt", "a") as f:
        f.write(f"{oggi} | SPESA | -{spesa_val} | Motivo: {motivazione} | Nuovo saldo: {conto}\n")

else:
    print("Scelta non valida.")

#SALVATAGGIO SALDO AGGIORNATO
with open("saldo.txt", "w") as f:
    f.write(str(conto))