
import math
import random

#1. feladat:
'''Kérj be 1 páros számot a felhasználótól. (1 pont)
Amennyiben nem páros számot ad meg a felhasználó, akkor kérd be újra a számot, addig, amíg páros számot nem ad meg!  (1 pont)	'''
print("1.feladat")
def feladat1():
    a:int=int(input("Kerek egy páros számot!"))
    while not (a % 2 == 0):
        print("Ez nem páros!Kérek egy páros számot!")
        a:int=int(input("Kerek egy páros számot!"))
        if a % 2 == 0:
            print(a)

#2.feladat:
'''Írass ki a konzolra 13 db  [10, 150] zárt intervallumba eső véletlen számot. Hány 3-mal osztható van közöttük? 
A kiírás formátuma: „A számok között X db 3-mal osztható van!”'''
print("2.feladat")
def feladat2():
    i:int=0
    j:int=0
    while i<13:
        a:int=math.floor(random.random()*141+10)
        print(a,end=" ")
        i+=1
        if a % 3 == 0:   
            j+=1
        
    print("A számok között", j ,"db 3-mal osztható van!")

#3.feladat:
'''Írj eljárást, mely paraméterként kap egy text szöveget, és egy N számot. 
 Amennyiben a szöveg rövidebb, mint a megadott N szám, akkor írjuk ki „Nincs N. karakter!”
Ha hosszabb, akkor a text szövegnek az N. karakterét írjuk ki csupa nagybetűvel 3-szor! '''
print("3.feladt")
def feladat3(text:str,N:int):
    kiiras:int=N*3
    text:str=0
    while not (text < N):
        print("Nincs N. karakter!")
    else:
        print(kiiras)

#4.feladat:
'''Írj metódust, mely neveket kér a felhasználótól, amíg a @ jelet nem kapja.
Hány nevet adott meg a felhasználó? 
A kiírás formája: „A felhasználó 12 nevet adott meg.”'''
print("4.feladat")
def feladat4():
    i:int=0
    j:str="@"
    kiiras:int=0
    a:str=str(input("Kérek egy nevet!"))
    while not(a == j):
        a:str=str(input("Kérek egy nevet!"))
        print(a,end=" ")
        i+=1
        if a == j:
            kiiras+=1

    print("A felhasználó",kiiras,"nevet adott meg.")




