# PRE

# print(list(range(2,9,2)))
# pętla liczb dwucyfrowych od 10 do 21
# pętla liczb dwucyfrowych nieparzystych od 15 do 31  
# pętla liczb dwucyfrowych malejąco (step ujemny)
# pętla liczb dwucyfrowych malejąco (step dodatni)
# pętla liczb 3-cyfrowych podzielnych przez 20

# for i in range(3, 10):
#    print(i)


# zadania

# print(list(range(10,22)))

# print(list(range(15, 32, 2)))

# print(list(range(99, 9, -1)))

# print(list(range(-99, -9, 1)))

# print(list(range(100, 1000, 20)))

# zad 1
# n = int(input())
# for i in range(n):
#   print(i**3+3, end=" ")

# zad 2
# for i in range(105,1000,15):
#   print(i,end=" ")

# zad 3
# p = int(input())
# for i range(1, p+1):
#   in p % i == 0:
#      print(i,end=" ")

# zad 4
# s = 0
# for i in range(10,100):
#   s=s+i
# print(s)

# zad 5
# n = int(input("W ile osob gramy? "))

# suma = n*(n+1) // 2
# for i in range(n-1):
#    a = int(input())
#    suma = suma - a
# print(suma)

# napisz pętlę sumującą liczby dwucyfrowe parzyste

suma=0
for i in range(10, 100, 2):
  suma=suma+i
print(suma)

#