#CLASS CREATION AND PARAMETERS DEFINITION
class ContoBancario:
    def __init__(self, titolare, saldo):
        self.titolare = titolare
        self.saldo = saldo

#FUNCTIONS DEFINITION 
def deposit_amount(amount):
    conto1.saldo += amount

def withdrawal(minus):
    conto1.saldo -= minus

#LOGIC
conto1 = ContoBancario("Mario", 100)
print(f"Benvenuto: {conto1.titolare}, saldo: {conto1.saldo}")
operation = int(input("Scegli l operazione da eseguire \n 1 = mostra saldo \n 2 = deposito \n 3 = prelievo\n"))
if operation == 1:
    print(f"Ecco il tuo sald attuale: {conto1.saldo}")
elif operation == 2:
   deposit = int(input("inserisci la somma da depositare: "))
if operation == 2:
    deposit_amount(deposit)
    print(f"Saldo aggiornato: {conto1.saldo}")
elif operation == 3:
    prelievo = int(input("inserisci la somma da prelevare: "))
    if prelievo > conto1.saldo:
        print (f"Prelievo fallito Ecco il tuo saldo attuale:  {conto1.saldo} perfavore inserisci un importo minore o uguale al tuo saldo attuale")
    else:
        withdrawal(prelievo)
        print(f"Prelievo avvenuto con successo ecco il tuo saldo residuo: {conto1.saldo}")




