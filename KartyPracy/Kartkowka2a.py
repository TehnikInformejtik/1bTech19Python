# zad 5
a = int(input("podaj pierwsza dlugosc: "))
b = int(input("podaj druga dlugosc: "))
c = int(input("podaj trzecia dlugosc: "))

if a+b>c and a+c>b and b+c>a:
  print("Tak")
else:
  print("Nie")