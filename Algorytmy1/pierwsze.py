#1 sprawdzanie czy liczba dzieli się tylko przez 1 i samą siebie (2,3,5,7,11,13,17,19,23)
#dzielniki właściwe: dzielniki liczby poza 1 i nią samą

# n=int(input())
# for i in range(2,n):
#   if n%i==0:
#     print("Liczba nie jest pierwsza")
#     exit()
# print("liczba jest pierwsza")



#2 GENEROWANIE LICZB PIERWSZYCH

n = int(input("Podaj do jakiej liczby mam szukać liczb pierwszych: \n"))
for i in range(2, n+1):
  flaga = True
  for j in range(2, i):
    if i%j==0:
      flaga = False
      break
  if flaga:
    print(i,end=" ")



#3 GENEROWANIE LICZB PIERWSZYCH

p = int(input("Podaj od ilu mam szukać liczb pierwszych: \n"))
i=2
licznik=0
while 1:
  flaga = True
  for j in range(2,int(i**0.5)+1):
    if i%==0:
      flaga = False
      break
  if flaga == True:
    print(i,end=" ")
  licznik += 1
  if licznik == p:
    break
  else:
    i=i+1
      