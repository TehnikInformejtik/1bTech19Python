# FUNKCJA "ORD"
# print(ord("A"))
# print(ord("Z"))
# W PYTHON KOD ASCII WIELKICH LITER A-Z SĄ OD 65 DO 90

# FUNKCJA "CHR" - ZWRACA ZNAK DLA DANEGO KODU
# print(chr(66))
# print(chr(75))

# zadanie testowe: wypisz alfabet liter wielkich
# for i in range(65,91):
#   print(chr(i), end=" ") 

# String w Python - "lista"           LEN() - LENGHT(DŁUGOŚĆ)
# napis = "ARGENTYNA"
# print(napis[0], napis[1], napis[2])

napis = input("Podaj coś do zaszyfrowania: ")
szyfr = ""
for i in range(len(napis)):
  print(napis[i])
  szyfr = szyfr + chr(ord(napis[i])+3)
print(szyfr)