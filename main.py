##BiblioSoftware: Soluzione Integrata per la Gestione delle Biblioteche

#aggiungi_libro(titolo, copie)
Descrizione: Aggiunge un nuovo libro alla biblioteca con il numero di copie specificato.
Se il libro esiste già, aggiorna il numero di copie aggiungendo quelle nuove.
Se il libro non esiste, lo aggiunge al sistema.

Creo un dizionario dove le chiavi sono i nomi dei libri e i valori le copie. I nomi dei libri e le relative copie vengono date in input dall'utente
"""

from helper import aggiungi_libro

biblioteca = {}
copie = 0
titolo = ""

a = aggiungi_libro(titolo, copie)
print(a)

"""#rimuovi_libro(titolo)
Descrizione: Rimuove un libro dalla biblioteca.
Se il libro esiste, viene eliminato dal sistema.
Se il libro non esiste, il programma stampa un messaggio di errore

"""

def rimuovi_libro(titolo):
  while True:
    titolo = input("Inserisci un libro da eliminare")
    if titolo == "esci":
      print("Hai deciso di chiudere. Alla prossima!")
      break
    else:
      if titolo not in biblioteca:
        print(f"Attenzione, il libro {titolo} non esiste")
      else:
        biblioteca.pop(titolo)
        print(f"Il libro {titolo} è stato rimosso")
    return biblioteca

b = rimuovi_libro("titolo")
print(biblioteca)

"""#verifica_disponibilita(titolo)
Descrizione: Controlla se un libro è disponibile nella biblioteca.
Restituisce True se almeno una copia è disponibile.
Restituisce False se il libro non esiste o non ci sono copie disponibili.

"""

biblioteca = {'La città': 1, 'Il gatto': 4, 'Il cane': 4, 'Il fiume': 0}
def verifica_disponibilita(titolo):
  titolo = input("Inserisci un libro da controllare ")
  flag_y = biblioteca[titolo]> 0 and titolo in biblioteca
  flag_n = biblioteca[titolo]<= 0 or titolo not in biblioteca
  if flag_y:
    print(flag_y)
    print(f"Il libro {titolo} è disponibile")
  if flag_n:
    flag_n = False
    print(flag_n)
    print(f"Il libro inserito, {titolo}, non è disponibile")
  return biblioteca
c = verifica_disponibilita("titolo")
print(biblioteca)

"""#prendi_in_prestito(titolo)
Descrizione: Riduce il numero di copie disponibili di un libro di 1, simulando un prestito.
Se il libro è disponibile, decrementa il numero di copie di 1.
Se non ci sono copie disponibili o il libro non esiste, stampa un messaggio di errore.

"""

biblioteca = {'La città': 1, 'Il gatto': 4, 'Il cane': 4, 'Il fiume': 0}
def prendi_in_prestito (titolo):
  titolo = input("Inserisci un libro da prendere in prestito ")
  if titolo in biblioteca and biblioteca[titolo]>0:
      biblioteca[titolo]-= 1
      print(f"Complimenti, hai preso in prestito il libro {titolo}")
  else:
    print(f"Mi dispiace, il titolo inserito, {titolo}, non è disponibile")
  return biblioteca

d = prendi_in_prestito ("titolo")
print(biblioteca)

"""#statistiche_biblioteca()
Descrizione: Restituisce un dizionario con informazioni sulla biblioteca.
**totale_libri: numero totale di titoli**
**copie_totali: numero totale di copie**
**media_copie: numero medio di copie per libro**

"""

biblioteca = {'La città': 1, 'Il gatto': 3, 'Il cane': 4, 'Il fiume': 0}
statistiche = {"totale_libri": 0, "copie_totali": 0,"media_copie":0}
def statistiche_biblioteca():
  for chiave, valore in biblioteca.items():
    totale_libri = len(biblioteca)
    copie_totali = sum(biblioteca.values())
    media_copie = copie_totali/len(biblioteca)
  statistiche["totale_libri"] = totale_libri
  statistiche ["copie_totali"] = copie_totali
  statistiche ["media_copie"] = media_copie
  return statistiche

e = statistiche_biblioteca()
print(statistiche)
print(biblioteca)

"""#visualizza_libri()
Descrizione: Mostra un elenco di tutti i libri nella biblioteca insieme al numero di copie disponibili.
Se la biblioteca è vuota, stampa un messaggio che indica che non ci sono libri.

"""

biblioteca = {'La città': 1, 'Il gatto': 3, 'Il cane': 4, 'Il fiume': 0}
def visualizza_libri():
  for chiave, valore in biblioteca.items():
    print(chiave, valore)
  if not biblioteca: #SE IL DIZIONARIO E' VUOTO
    print ("Mi dispiace ma la biblioteca è vuota")
  return biblioteca

f = visualizza_libri()
print(f)

"""##restaurare_libro(titolo, copie)
Descrizione: Ripristina (aggiunge) copie di un libro che è stato preso in prestito o che necessita di più copie.
Se il libro esiste, aggiunge il numero specificato di copie.
Se il libro non esiste, stampa un messaggio di errore.

"""

biblioteca = {'La città': 1, 'Il gatto': 3, 'Il cane': 4, 'Il fiume': 0}
def restaurare_libro(titolo, copie):
  titolo = input("Inserisci il libro da ripristinare ")
  if titolo in biblioteca:
    copie = int(input("Inserisci le copie "))
    biblioteca[titolo]+= copie
    print(f"Il numero di copie richiesto, {copie}, è stato aggiunto al libro {titolo}")
  else:
    print(f"Attenzione, il libro inserito, {titolo}, non esiste")
  return biblioteca


g = restaurare_libro("titolo", "copie")
print(g)

