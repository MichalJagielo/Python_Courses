#!/usr/bin/env python
# coding: utf-8

# Zadanie 1 
# Napisz program, który dla dwóch zbiorów danych $s_1=\{1,2,3,4\}$ 
# oraz $s_2=\{3,4,5,6\}$ wyświetli:
# - elementy obu zbiorów (bez powtórzeń),
# - elementy wspólne dla obu zbiorów,
# - elementy zbioru $s_1$ nie będące elementami zbioru $s_2$,
# - elementy zbioru $s_2$ nie będące elementami zbioru $s_1$.
𝑠1={1,2,3,4}
𝑠2={3,4,5,6}

s3 = s1^s2
print('elementy obu zbiorów bez powtórzeń S3=', s3)
s4 = s1&s2
print('elementy wspólne dla obu zbiorów S4=', s4)
s5 = s1-s2
print('elementy zbioru  𝑠1  nie będące elementami zbioru  𝑠2/ S5=', s5)
s6 = s2-s1
print('elementy zbioru  𝑠2  nie będące elementami zbioru  𝑠1/ S6=', s6)


# Zadanie 2 
# Wykorzystując słownik napisz translator tekstu na alfabet Mors'a.
# Szczegółowe informacje znajdzisze pod linkiem: http://alfabetmorsa.pl/.
# Przetłumacz poniższy tekst. 
# Załóżmy, że znakiem rozdzielającym słowa w alfabecie Morse'a jest znak `/`.
#litery = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
#         'V','W','X','Y','Z',' ']
#mors = ['•-','-•••','-•-•','-••','•','••-•','--•','••••','••','•---','-•-','•-••','--','-•',
#       '---','•--•','--•-','•-•','•••','-','••-','•••-','•--','-••-','-•--','--••','/']
#tekst = 'Matematyka i informatyka jest super'


litery = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
          'V','W','X','Y','Z',' ']
mors = ['•-','-•••','-•-•','-••','•','••-•','--•','••••','••','•---','-•-','•-••','--','-•',
        '---','•--•','--•-','•-•','•••','-','••-','•••-','•--','-••-','-•--','--••','/']
tekst = 'Matematyka i informatyka jest super'
print('--------------------------------------------------')
tekst1 = list(tekst.upper())        #Zamiana tekstu do translacji na wielkie litery
#print(tekst1)
print('--------------------------------------------------')


slownik = {}        #Przypisanie klucz:wartosc z list litery[key]:mors[value]

for key in litery:
    for value in mors:
        slownik[key] = value
        mors.remove(value)
        break
print("Słownik z litery[key] : mors[value]")
print(slownik)

print("--------------------------------------------------")

#print("Długość tekst1 =",len(tekst1))
#print("Długość słownik =",len(slownik))

print("--------------------------------------------------")

print("Tekst do zakodowania z wielkich liter")
print(tekst1)
print("--------------------------------------------------")
translator = []   #Pusta lista do ktorej przypiszemy wartosci z morsa == litery z tekstu
for el in tekst1:
    if el in litery:
        translator.append(slownik[el])
print("Kod w alfabecie Mors'a")        
print(translator)


# Zadanie 3
# Uzupełnij poniższy program, tak aby wypisywał tekstowy komunikat o wyniku 
# dzielenia liczb `x` i `y` lub o ewentualnym błędzie (z informacją o szczegółach błędu). 
# Program powinien być odporny na błędy niezależnie od przekazanych argumentów. 
# Jeśli nie będzie błedów w dzieleniu, wybisz `brak błędów`. 
# Skorzytaj z mechanizmu obsługi wyjątków i klauzuli `try`.
x = input("Podaj liczbę x ")
y = input("Podaj liczbę y ")
z = x/y
print("Wynik równania z = x/y")

while True:
    try:
        x = input("Podaj liczbę x: ")
        x1 = float(x)
    except ValueError:
        print("Podano nieprawidłową wartość parametru x. Podaj prawidłową wartość")
    else:
        break
while True:
    try:
        y = input("Podaj liczbę y: ")
        y1 = float(y)
        assert y1 != 0, "Parametr y musi być różny od zera!"
    except ValueError:
        print("Podano nieprawidłową wartość parametru y. Podaj prawidłową wartość")
    else:
        z = x1/y1
        print("Brak błędów")
        print("z =", z)
        break



