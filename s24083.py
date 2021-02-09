# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:36:07 2020

@author: USER
"""

from fractions import Fraction as frac







def print_sozluk(sozluk):
    for i in sozluk.values():     
        for j in i[0]:
            if len(i[0])==1:
                print(j)
                break
            if j == i[0][-1]:
                print(j,end=("="))
                print(i[1])
                break
            print(j,end=("+"))





def kesirKarsilastirma(kesir1, kesir2):
    """ 
    kesir1 ve kesir2, [pay, payda] seklinde tutulan iki elemanli listelerdir.  
    
    
    """
    if kesir1[0]*kesir2[1] >= kesir2[0]*kesir1[1]:        
        return True
    return False

def kucuktenbuyuge(liste, eleman):
    """ 
    liste kucukten buyuge sirali olacagi icin 
    eklenecek 'eleman'in yerini tespit edip, uygun yere ekleyeceksiniz 
    
    """
    sadelestirlmis_sayi = frac(eleman).limit_denominator()
    kesir1 = [sadelestirlmis_sayi.numerator, sadelestirlmis_sayi.denominator]

    for i in liste:
        if kesirKarsilastirma(i, kesir1):           
            liste.insert(liste.index(i), kesir1)
            return
    liste.append(kesir1)
        
def buyuktenkucuge(liste, eleman):
    """ 
    liste buyukten kucuge sirali olacagi icin 
    eklenecek 'eleman'in yerini tespit edip, uygun yere ekleyeceksiniz 
    
    """
    sadelestirlmis_sayi = frac(eleman).limit_denominator()
    kesir1 = [sadelestirlmis_sayi.numerator, sadelestirlmis_sayi.denominator]
    
    for i in reversed(liste):
        if kesirKarsilastirma(i, kesir1):           
            liste.insert(liste.index(i)+1, kesir1)
            return
    liste.insert(0, kesir1)

def soru1(liste):
    """ 
    1. soru icin gerekenleri bu fonksiyonun altinda yapacaksiniz:
    liste1 icerisinde kucukten buyuge olan elemanlari, liste2 icerisinde de buyukten kucuge olan elemanlari tutacaksiniz 
    """
    
    
    liste1 = []    
    liste2 = []
  
        
    for i in liste:

        if(type(i) != float and type(i) !=int):
            raise ValueError('Values must be type of float!')

        temp = frac(i).limit_denominator()
        total = temp.numerator+temp.denominator
        
        if total>50:
            kucuktenbuyuge(liste1, i)
        else:
            buyuktenkucuge(liste2, i)
            
            
    return liste1 , liste2
    
def soru2(liste):
    """ 
    soru2 icerisinde istenilen sozlugu olusturduktan sonra ekrana yazdiriniz, 
   
   
    """
    sozluk = {}

    for i in liste:
        sadelestirlmis_sayi = frac(i).limit_denominator()
        key = sadelestirlmis_sayi.denominator
        value = sadelestirlmis_sayi.numerator
        
        if(sadelestirlmis_sayi.denominator in sozluk):
            sozluk[key][0].append(value)
            sozluk[key] = [sozluk[key][0], sozluk[key][1] + value]
        else:
            sozluk[key] = [[value], value]

    print_sozluk(sozluk)





i = 0
listeler = [[1.1, 13.86, 25.346, 17.1, 2.2], [1.7], [5.7], [10.9, 0.2, 0.6, 3], [1, 2, 3], [1, 2, 3, 50, 60, 70]]
for liste in listeler:
    print("Girdi", i, ":", liste)
    liste1, liste2 = soru1(liste)
    print(liste1)
    print(liste2)

    soru2(liste)
    i += 1
    print("\n")