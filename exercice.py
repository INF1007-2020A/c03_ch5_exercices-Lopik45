#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def convert_to_absolute() -> float:
    nb = input("Veuiller entrer un nombre:")
    if nb<0:
        nb = nb*(-1)
    return nb

def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    liste = ""
    for char in prefixes:
        liste+= char+suffixes
        if char!="P":
            liste+=", "
    liste +=" et Qack."    
    return liste


def prime_integer_summation() -> int:
    nb_pre=0
    resultat = 0
    nb = 2
    premier = True
    while nb_pre < 100:
        b=2
        while b <= int(nb**0.5):
            if nb%b == 0:
                premier = False
                break
            else:
                premier = True
            b+= 1
        if premier == True or int(nb**0.5)==1:
            resultat+=nb
            nb_pre+=1
        nb+=1
    return resultat


def factorial(number: int) -> int:
    i=0
    resultat=1
    while i < number:
        resultat = resultat*(number-i)
        i+=1
    return resultat


def use_continue() -> None:
    for nb in range(1,11):
        if nb==5:
            continue
        print(nb)
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 nombres premier est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()
