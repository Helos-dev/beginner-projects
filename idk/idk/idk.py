#CLASS CREATION AND PARAMETERS DEFINITION
class ContoBancario:
    def __init__(self, titolare, saldo):
        self.titolare = titolare
        self.saldo = saldo

#LOGIC
conto1 = ContoBancario("Mario", 100)
print(f"Benvenuto: {conto1.titolare}, saldo: {conto1.saldo}")
operation = int(input("Scegli l operazione da eseguire \n 1 = mostra saldo \n 2 = deposito \n 3 = prelievo\n"))
if operation == 1:
    print(conto1.saldo)
