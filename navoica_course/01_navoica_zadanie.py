#!/usr/bin/env python
# coding: utf-8


# Zadanie 1
# Napisz program, który dla wprowadzonej liczby naturalnej `n`
# sprawdzi czy liczba ta jest parzysta i wyświetli napis `parzysta` 
# dla liczby `n` parzystej albo `nieparzysta` dla liczby `n` nieparzystej 
# albo `niepoprawna liczba` gdy podana liczba bęzie z poza dopuszczalnego zakresu.

n = 2.2
# print(n)
#n = int(input("Podaj liczbę n: "))
if n < 0:
    print("niepoprawna liczba")
elif type(n) is float:
    print("niepoprawna liczba")
else:
    print("parzysta" if n % 2 == 0 else "nieparzysta")


# Zadanie 2 
# Napisz program, który spośród trzch podanych liczb `a, b, c` 
# wybierze i wyświetli największą z nich.
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
l_max = max(a, b, c)
print("Największa podana liczba to: {}".format(l_max))


# Zadanie 3
# Napisz program, który na zmiennej `kolejka` typu `list` 
# wykona poniższe operacje zgodnie z algorytmem `FIFO`:
# - dodaj element o wartości `2` do kolejki,
# - dodaj element o wartości `4` do kolejki,
# - pobierz element z kolejki,
# - dodaj element `6` do kolejki,
# - pobierz element z kolejki,
# - dodaj elemeny `7` do kolejki.
kolejka = [2, 4, 5]
kolejka.append(2)
kolejka.append(4)
kolejka.pop(0)
kolejka.append(6)
kolejka.pop(0)
kolejka.append(7)
print("Nowa kolejka: ", kolejka)


# Zadanie 4
# Napisz program, który dla podanej listy `L`, zwróci nową listę, 
# której elementami będą elementy listy `L` ale tylko te z nieparzystych pozycji. 
L = [2, 4, 3, 4, 5, 5, 2, 3]
L1 = L[::2]
print("Nowa list: ", L1)


# Zadanie 5
# Napisz program, który dla podanej listy `L`, zwróci nową listę, 
# której elementami będą elementy listy `L` ale tylko te z parzystych pozycji.
L = [2, 4, 3, 4, 5, 5, 2, 3]
L1 = L[1::2]
print("Nowa list: ", L1)


# Zadanie 6
# Dla liczb naturalnych z przedziału $[m, k], m<k$ znajdź średnią arytmetyczną 
# tych liczb, które są podzielne pezez zadaną liczbę naturalną $p$.
m = 4
k = 10
p = 2

l = list(range(m, k+1))
print("Twój przedzial: ", l)

l1 = [i for i in l if i % p == 0]
print("Liczby z Twojego przedzialu podzielne przez p: \nl1=", l1)

# for e in enumerate(l1):
#   print(e)
print("--------------------------------------")
śr_art = sum(l1)/len(l1)
print("śr_art z l1: ", śr_art)


# Zadanie 7 
# Dany jest przedział $[p1, p2]$ liczb naturalnych oraz liczba naturalna $p$ 
# z jego wnętrza. Utwórz sumę liczb naturalnych z przedziału $[p1, p]$ 
# oraz lioczyn pozostałych liczb.
p1 = 2
p2 = 9
p = 5
print("p1 =", p1, "\np2 =", p2, "\np =", p)
l = list(range(p1, p2+1))
print("Przedział [p1,p2]:", l)
l1 = list(range(p1, p+1))
print("Lista l1 z przedzialu [p1,p]:", l1)
print("Suma elementow l1=", sum(l1))
l2 = [el for el in l if el not in l1]
print("Pozostałe elementy:", l2)
x = 1
for i in l2:
    x = x*i
print("Iloczyn=", x)


# Zadanie 8
# Napisz program, który z dwóch zadanych liczb naturalnych $a$ i $b$ 
# utworzy listę zawiarającą elementy $c$ będące elementami ciągu Fibonacciego wg algorytmu:
# $$\begin{array}{c}c=a+b\\a=b\\b=c\end{array}$$
# dopóki $c$ nie przekroczy wartości $(a+b)^3$, 
# a następnie zwróci sumę wszystkich elementów utworzonej listy.
a = 2
b = 4
c = a+b
l = []
for i in range(a, c+b):
    c = a+b
    a, b = b, c
    l.append(c)
    print(l)
print("Suma elementów ciągu =", sum(l))



