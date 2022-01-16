#!/usr/bin/env python
# coding: utf-8



# Zadanie 1
# Napisz program, który dla dwóch liczb rzeczywistych zapisanych w zmiennych
# `x` i `z` typu `float`, oraz dwóch liczb całkowitych zapisanych w zmiennych
#  `i` i `j` typu `int` oblicz wartość następujących wyrażeń arytmetycznych
# i zapisze je do zmiennych `v` i `y`:
# $$v=\frac{\ln{x^2}+2x^2+z^{-2}}{(x+z)i}+\frac{i}{j}$$
# $$y=\frac{x\ln{(x^2+1)}}{2}\sin^2{(2x^2-1)}$$
import math
x=1.5 
z=2.3 
i=2 
j=3
v=(2*math.log(x) + 2*x*x + 1/z**2)/((x + z)*i) + i/j
print('v = ', v)
y=((x*math.log(x**2 + 1))/2)*(math.sin(2*x*x -1)**2)
print('y = ', y)


# Zadanie 2
# Napisz program, który zaokrągli podaną liczbę `x` w górę do podanej liczby 
# miejsc po przecinku `n`.
import math
x=2.444
n=2
y='%s' %float('%.2g5' % x)
print('Liczba x po zaokragleniu: ', y)


# Zadanie 3 
# Napisz program, który we wprowadzonym tekscie wyeliminuje pierwsze 
# wystąpienie podanego znaku. Zakładamy, że podany znak na pewno występuje w tekscie.
tekst='przykładowy tekst'
znak = 'y'
nowy_tekst = tekst.replace(znak, '', 1)
print('Nowy tekst: ', nowy_tekst)
#2
tekst='przykładowy tekst'
znak = 'y'
x = tekst.find("y")
y = tekst.rfind("y")
print(x)
print(y)
tekst1 = list(tekst)
tekst1[3] = ""
new_tekst = "".join(tekst1)
print('Nowy_tekst: ', new_tekst)


# Zadanie 4
# Napisz program, który we wprowadzonym tekscie wyeliminuje ostatnie wystąpienie
# podanego znaku. Zakładamy, że podany znak na pewno występuje w tekscie.
tekst='przykładowy tekst'
znak = 'y'
x = tekst.find("y")
y = tekst.rfind("y")
print('Pozycja pierwszego wystąpienia y: ', x)
print('Pozycja drugiego wystąpienia y: ', y)
tekst1 = list(tekst)
tekst1[10] = ""
new_tekst = "".join(tekst1)
print('Nowy_tekst: ', new_tekst)


# Zadanie 5
# Dane są dwa teksty. Napisz program, który dołączy fragment tekstu pierwszego
# od znaku o podanej pozycji na koniec tekstu drugiego oraz poda liczbę słów 
# w nowo utworzonym tekscie. Zakładamy, że słowa rozdziela spacja `(' ')`.
t1 = 'przykładowy tekst 1'
t2 = 'przykładowy tekst 2'
t3 = (t2 + t1[4:])
print(t3)
print(len(t3.split(' ')))


# Zadanie 6
# Napisz program, który korzystając ze zmiennej `data`, w której przechowywana
# jest data w formacie `rrrr-mm-dd` (np. 2019-11-04), utworzy trzy nowe zmienne
# `rok`, `miesiac`, `dzien` i przypisze im odpowiednie wartości jako liczby całkowite.
import datetime
data =  datetime.date(2021, 11, 17)
print(data)
data1=data.strftime('%Y/%m/%d')
str(data1)
x=int(data1[:4])
print('Zmienna rok:', x)
y=int(data1[5:7])
print('Zmienna miesiac:', y)
z=int(data1[8:])
print('Zmienna dzien:', z)



