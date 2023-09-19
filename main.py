import random as rnd
plik = open("kartkowka.txt", "w")
for i in range(26):
    plik.write("Grupa " + chr(i + 65) + "\n\nWykonaj podane konwersje między systemami liczbowymi:\n\n")
    liczby10 = []
    for j in range(4):
        liczby10.append(rnd.randint(10000, 1000000))
    plik.write(' ,'.join(map(str, liczby10)))
    plik.write("\n\n")
