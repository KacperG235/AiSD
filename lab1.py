#Zad 1
def foo1(imie, nazwisko):
    kropka = imie[0] + "." + nazwisko
    return kropka
print(foo1("Krzysztof", "Kononowicz"))

#Zad 2
def foo2(imie, nazwisko):
    kropka = imie[0].capitalize() + "." + nazwisko.capitalize()
    return kropka
print(foo2("kacper", "gutowski"))

#Zad 3
def foo3(liczba1, liczba2, wiek):
    rok = str(liczba1) + str(liczba2)
    rok = int(rok)
    data = rok - wiek
    return data
print(foo3(20, 22, 21))

#Zad 4
def foo4(imie, nazwisko, foo):
    return foo(imie, nazwisko)
print(foo4('wojtek', 'suchodolski', foo2))

#Zad 5
def foo5(liczba1, liczba2):
    if liczba1 > 0 and liczba2 > 0 and liczba2 != 0:
        return liczba1/liczba2
print(foo5(1, 2))

#Zad 6
def foo6():
    suma = 0
    while suma < 100:
        liczba = int(input("podaj liczbe: "))
        suma += liczba

#Zad 7
def foo7(lista):
    return tuple(lista)
list1 = [1, 2, 3, 5]
list2 = foo7(list1)
print(type(list2))

#Zad 8
def foo8(ile_wartosci):
    lista = []
    while ile_wartosci != 0:
        wartosc = input("Podaj element: ")
        lista.append(wartosc)
        ile_wartosci -= 1
    lista = tuple(lista)
    return lista

#Zad 9
def foo9(liczba):
    tydzien = {1: "Poniedzialek", 2: "Wtorek", 3: "Środa", 4: "Czwartek", 5: "Piatek", 6: "Sobota", 7: "Niedziela"}
    return tydzien[liczba]
print(foo9(6))

#zad 10
def foo10(wyraz):
    if wyraz == wyraz[::-1]:
        print("Palindrom")
    else:
        print("Nie Palindrom")
foo10("kajaku")

