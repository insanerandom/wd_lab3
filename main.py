import random
import sys
import ciaggeo
import ciagaryt


def zadanie4(przypr1, przypr2, przeciwpr): #funkcja z zadania4
    a = przypr1 * przypr1
    b = przypr2 * przypr2
    c = przeciwpr * przeciwpr
    if (a + b == c):
        print("Trojkat jest prostokatny")
    else:
        print("Trojkat nie jest prostokatny")
    return

def zadanie5(a = 5, b = 3, h = 4): #funkcja z zadania5
    c = a + b
    return ((c * h) / 2)

def zadanie6(a = 1, b = 4, ile = 10): #funkcja z zadania6
    a = a * b
    if ile == 1:
        return a
    return zadanie6(a, b, ile - 1)

def zadanie7(a = 1, b = 4, ile = 10): #funkcja z zadania7
    a *= b
    if ile == 1:
        return a
    return zadanie7(a, b, ile - 1)

def zadanie8(** ceny):
    count = 0
    suma = 0
    for cos in ceny:
        print(cos)
        count += 1
        suma = suma + ceny[cos]
    print("ilosc produktow: ", count)
    print("suma produktow: ", suma)

print("\nZad2")
liczby = []
for i in range(0, 10, 1):
    liczby.append(random.randint(1, 100))
print(liczby)
lista = [i for i in liczby if i % 2 == 0]
print(lista)
print("\nZad3")
produkty = {
    "maka": "kg",
    "cytryny": "kg",
    "jajka": "sztuki",
    "mleko": "litry",
    "czosnek": "sztuki",
    "ananas": "sztuki"
}
newList = []
print(produkty)
#wersja z petla
for key, value in produkty.items():
    if value == "sztuki":
        newList.append(key)
print(newList)
#wersja z comprehension
newList2 = [key for key, value in produkty.items() if value == "sztuki"]
print(newList2)
print("\nZad4")
zadanie4(3, 4, 5)
print("\nZad5")
print(zadanie5())
print("\nZad6")
print(zadanie6(2, 7, 4))
print("\nZad7")
print(zadanie7(2, 7, 4))
print("\nZad8")
zadanie8(maka = 2.80, cytryny = 4.10, jajka = 1, mleko = 2.90, czosnek = 2.20, ananas = 12.80)
print("\nZad9")
ciag1 = [3, 6, 12, 24, 48, 96]
ciag2 = [2, 4, 6, 8, 10, 12, 14, 16]
print(ciaggeo.nty_wyraz(ciag1[0], 2, 4))
print(ciaggeo.suma_n_wyrazow(ciag1[0], 2, 3))
print(ciagaryt.nty_wyraz(ciag2[0], 5, 2))
print(ciagaryt.suma_n_pierwszych(ciag2[0], ciag2[2], 3))
print("\nZad10")
liczby = []
for i in range(0, 10, 1):
    pot = random.randint(1, 100)
    while pot % 4 != 0:
        pot = random.randint(1, 100)
    pot = str(pot)
    liczby.append(pot)
print(liczby)
plik = open("text.txt", "w")
for i in range(0, len(liczby), 1):
    plik.write(liczby[i])
    if i != len(liczby) - 1:
        plik.write(" ")
plik.close()
print("\nZad11")
plik = open("text.txt", "r")
wiersze = plik.readlines()
plik.close()
print(wiersze)



