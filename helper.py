def aggiungi_libro(titolo, copie):
  while True:
    titolo = input("Inserisci un libro ")
    if (titolo == "esci"):
      print("Hai deciso di chiudere. Alla prossima!")
      break
    else:
      if titolo not in biblioteca:
        copie = int(input("Inserisci il numero di copie "))
        biblioteca[titolo] = copie
        print(biblioteca)
      elif titolo in biblioteca:
        copie = int(input("Inserisci il numero di copie "))
        biblioteca[titolo] += copie
        print(biblioteca)

  return biblioteca