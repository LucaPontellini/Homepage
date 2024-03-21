#Esercizio: in una copisteria, il costo unitario delle fotocopie varia a seconda del numero da effettuare secondo la seguente tabella: n.1-19 0,10 euro, n.20-100 0,08 euro, piu di 100 0,05 euro. Inoltre se le fotocopie sono da rilegare viene aggiunto un costo di 1,80 euro.
            #Dati in input il umero di fotocopie da effettuare, il nome del cliente e un indicazione che segnali se il plico è da rilegare, calcola il costo totale e stampa il seguente prospetto: Gentile Sig. ___ il suo preventivo è di ___ euro compresa la rilegatura. L'ultima riga è da scrivere solo se è richiesta la rilegatura.

print ("Welcome to the copy shop. This is the table of the various prices for photocopies:\n -number of photocopies from 1 to 19 --> € 0.10\n -number of photocopies from 20 to 100 --> € 0.08\n number of photocopies more than 100 --> € 0.05")
photocopies = input (int ("Enter the number of photocopies: '"))
          