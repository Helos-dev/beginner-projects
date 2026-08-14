#FUNZIONE MOSTRACONTO
def mostraconto(conto):
    print(f"Ecco a quanto ammonta il tuo conto attuale: {conto}")

#AGGIUNGI AL TUO CONTO
def aggiungiconto(aggiunta, conto):
    conto = aggiunta + conto
    print(f"Ecco il tuo conto aggiornato: {conto}")
    return conto

#REGISTRAZIONE SPESA
def spesa(spesa, motivazione, data, conto):
    conto = conto - spesa
    print(f"Hai speso {spesa} per: {motivazione}. Nuovo saldo: {conto}")
    return conto