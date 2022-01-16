#!/usr/bin/env python
# coding: utf-8

# Zadanie 1
# Korzystając z odpowiednich narzędzi wypisz linia po linii zawartość pliku 
# `file.txt` (Utwórz samodzielnie plik z przykładowym tekstem). 
# Następnie, wypisz zawartość pliku `file.txt` od tyłu.
path = r"D:\NAVOICA\Python3\file.txt"
'''
NIE DO KOŃCA JESTEM PEWIEN, KTÓRĄ WERSJĄ "ZAWARTOŚĆ PLIKU OD TYŁU" MAM SIĘ KIEROWAĆ
'''
with open(path, encoding="utf-8") as f:     ## Bez 'r' i tak jest domyślne. 
    for f1 in f:
        print(f1, end='')
print()
#### OD TYŁU WERSAMI ####
with open(path, encoding="utf-8") as f:
    f1 = f.readlines()
    f2=[]
    for el in f1:
        f2.append(el)
        f2_1 = (''.join(f2[::-1]))  ## Można jeszcze z reversed() ale wypisuje wtedy znaki od tylu
print(f2_1)                         ## Nie jestem pewien czy taki ma być rezultat.
#### OD TYŁU SŁOWAMI ####  
with open(path, encoding="utf-8") as f:
    f1 = f.read().split()
    f3 = []
    for el in range(len(f1)):
        x = f1.pop()
        f3.append(x)
    f3_1 = (' '.join(f3))
print(f3_1)


# Zadanie 2
# Napisz funkcję, która jako argument przyjmuje ścieżkę do pliku, 
# a następnie wyświetla informacje o:
# - liczbie wierszy w pliku,
# - liczbie znaków w pliku,
# - liczbie słów w pliku,
# - średniej długośći słowa w pliku.
def filepath(path):
    #path = "D:\\NAVOICA\\Python3\\dana.txt"

    with open(path, encoding="utf-8") as f:
        f1 = f.readlines()
        Number_of_rows = len(f1)
        print(f"Number of rows in file: {Number_of_rows}")

    with open(path, encoding="utf-8") as f:
        f1 = f.read()
        No_of_letters = len(f1)
    print(f"Number of letters in words: {No_of_letters}")
    
    with open(path, encoding="utf-8") as f:
        f1 = f.read().split()
        No_of_words = len(f1)
    print(f"Number of words in file: {No_of_words}")
    word_list = f1
    #print(word_list)
    k = []
    for el in word_list:
        k.append(len(el))
        avg = round(sum(k)/len(k))
    print(f"Average number of letters in word: {avg}")
    print("Words in average length:")
    for el in word_list:
        if len(el) == avg:
            print(el, end=", ")
   
filepath("D:\\NAVOICA\\Python3\\dana.txt")


# Zadanie 3
# Stwórz własny moduł o nazwie `kalkulator`, w którym zdefiniowane jako funkcje 
# będą podstawowe operacje matematyczne: dodawanie, odejmowanie, mnożenie i dzielenie. 
# W module umieść kod, który w przypadku wykonania pliku wyświetli 
# wynik wywołania zdefiniowanych funkcji dla przykładowych argumentów.
print("Program wykona podstawowe obliczenia +, -, *, /, dla zadanych liczb x i y") 
x = float(input("Podaj liczbe x: "))
y = float(input("Podaj liczbe y: "))

print()
def dodawanie(x, y):
    z = x + y
    return z

def odejmowanie(x, y):
    z = x - y
    return z                          

def mnożenie(x, y):
    z = x * y
    return z

def dzielenie(x, y):
    z = x/y
    assert y != 0, 'ValueError, ZeroDivisionError'
    return z
if __name__=='__main__':
    print()
print("Dodawanie: {0:.2f}".format(dodawanie(x,y)))
print("Odejmowanie: {0:.2f}".format(odejmowanie(x,y)))
print("Mnożenie: {0:.2f}".format(mnożenie(x,y)))
print("Dzielenie: {0:.2f}".format(dzielenie(x,y)))



