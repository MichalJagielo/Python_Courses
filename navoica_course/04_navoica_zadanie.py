#!/usr/bin/env python
# coding: utf-8

# Zadanie 1
# Napisz funkcję przyjmującą dwa argumenty: tekst do wypisania oraz szerokość linii 
#(argument o domyślnej wartości 80), wypisującą przesłany tekst wycentrowany w linii.
tekst = 'Przykładowy tekst'
def nowyTekst(tekst, szer):
    tekst = tekst.center(szer," ")
    print("Szerokość =",len(tekst))
    return tekst


nowyTekst(tekst, 80)


# Zadanie 2
# Napisz funkcję przyjmującą jako argumenty dwie listy, zwracającą listę, 
# której elementami jest suma odpowiednich elementów przesłanych 
# list (`[c[0]=a[0]+b[0], c[1]=a[1]+b[1], itd.]`). Jeśli listy nie są równej długości, 
# wyjściowa lista powinna mieć tyle elementów, ile ma krótsza z list. 
# Wykorzystaj mechanizm _list comprehension_.  
lista_a = [1,3,4,5,6]
lista_b = [4,6,5,7,8,9]
lista_c = []
# Bez warunku sprawdzającego długość list a,b. Funkcja, przy nieodpowiednim zakresie, zwraca błąd IndexError.
def list_sum (lista_a,lista_b):
    if len(lista_a)>= len(lista_b):
        
        lista_c = [lista_a[i]+lista_b[i] for i in range(len(lista_b))]
        
    else:
        lista_c = [lista_a[i]+lista_b[i] for i in range(len(lista_a))]
    
    return lista_c

list_sum(lista_a, lista_b)

print("lista_c[i] = lista_a[i] + lista_b[i] =", list_sum(lista_a, lista_b))


# Zadanie 3
# Napisz funkcję przyjmującą jako argument listę, kasującą z podanej listy 
# co trzeci element oraz wszystkie elementy o wartości mniejszej od 0. Wykorzystaj `del`.

"""
Wyniki różnią się od siebie w zależności od wartosci liczby +/-,ilości elementów dodanych
do pierwotnej listy oraz od przyjętej kolejności działań.
Moim zdaniem prawidłowe wyniki otrzymamy jeśli 
1. minus co 3 element 
2. delete el<0.
"""
List = [3, 0, 5, -1, 3, -5, -3, 5, 6]
List1 = List.copy()
def newList(List):
   
    k = 3
    del List1[k-1::3]
    return List1
    
List1 = [el for el in List1 if el >= 0]
newList(List1)


# Zadanie 4
# W pewnej grze twoje punkty są mnożone przez 1.1 za pokonanie pierwszego poziomu, 
# przez 1.2 za pokonanie drugiego poziomu itd. Stwórz listę ze wszystkimi mnożnikami, 
# a następnie napisz funkcję `final_score`, która obliczy i zwróci wynik 
# po ukończeniu dziesiątego poziomu. Niech początkowa ilość punktów będzie 
# argumentem funkcji. Wykorzystaj funkcję `reduce` oraz `lambda`.

from functools import reduce
def final_score(n):
    # Dla n = przyjęcie liczby punktów początkowych. 
    # Nie zakładam podania początkowej liczby punktów ujemnej.
    # Jeśli ujemna to całość w pętli if n>0 albo przez try:except z AssertionError a "n"
    # wprowadzane przez użytkownika float(input(n)) > 0 
    
    factor = []  #Pusta lista dla mnoznikow punktow
    levels = range(1,11)  #Liczba levelow, 11 bo range ostatni ucina a ma byc ich 10
    
    x=1
    y=0.1
    while x<=2:         #Tworzenie listy mnoznikow punktow. Przyjeto 1.1,1.2...+0.1 dla 10 levelow.
        x=x+y
        factor.append(float("%.1f" % x))  #Lista mnożników zamieniona na float z zaokrągleniem

    print("ScoresForEachLevel: ", factor)   
    print("LevelNumber: ", list(levels))
    
    FinalScores = reduce(lambda x,y:x*y,factor,n)   #Suma punkto za 10 levelow. Liczba poczatkowa dowolna
    
    FinalScores = round(FinalScores, 1)  #Zaokrąglenie wyniku do 1 miejsca po przecinku
    print("FinalScores: ", FinalScores)
    return FinalScores
final_score(4)


