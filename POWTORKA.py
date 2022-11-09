#ABY WYJĄĆ LICZBĘ ZE ŚRODKA
# n = 12345
# print((n%1000)//100)

# from math import sqrt
# print(sqrt(16))



#if`y
# == <= >= > < !=  --- operatory porównań

# pętla liczba 3-cyfrowa podzielna przez 13 i niepodzielna przez 4
# for i in range(100,1000):
#    if i%13 == 0 and i%4 != 0:
#       print(i)



#ŁĄCZENIE WARUNKÓW
# a, b, c = 3, 5, 7
# if a<b<c:
#    print("Eppure si move")



#ZADANIA
# n = 24
# suma = 0
# ilosc = 0
# for i in range(1,25):
#    if n%i==0:
#        print(i)
#        suma = suma+i
#        ilosc = ilosc+1
# print("suma", suma)
# print("ilosc", ilosc)



#oblicz sumę k początkowych liczb trzycyfrowych
# 100+101+102+103...
# wejscie: 4
# wyjscie: 406(100+101+102+103)
# k=4
# suma=0
# ilosc=0
# for i in range(100,1000):
#    suma=suma+i
#    ilosc=ilosc+1
#    if ilosc==k:
#       break
# print(suma)

#DRUGA OPCJA
# k=4
# suma=0
# for i in range(100,100+k):
#    suma=suma+i
# print(suma)


#Oblicz sumę n początkowych wyrazów ciągu fibonacciego
#1+2+3+4+5+8=13
#n = int(input())
#a,b=0,1
#suma=0
#for i in range(n):
#    a,b=b,a+b
#    suma=suma+b
#print(suma)