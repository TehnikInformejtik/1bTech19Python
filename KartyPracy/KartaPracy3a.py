#zad 1
# n = int(input())
# for i in range(n):
#   print("*-|", end=" ")

#zad 2
# n=int(input())
# for i in range(1,n+1):
#   print("*"*i,end="")
#   if i%2==0:
#     print("--",end="")
#   else:
#     print("||",end="")

#zad 3
# n=int(input())
# for i in range(1,n+1):
#   print("*",end="")
#   if i%2==0:
#     print("-"*i,end="")
#   else:
#     print("|"*i,end="")

#zad 7
# n = int(input())
# for i in range(n):
#   for j in range(n):
#     print(f"({i},{j})",end="")
#   print()

# LUB

# n= int(input())
# for i in range(n):
#   for j in range(n):
#     if i==0:
#       print("*",end="")
#     else:
#       print("-",end="")

# LUB

n=int(input())
for i in range(n):
  for j in range(n):
    if i==0 or j==0 or j==n-1 or i==n-1 or (i==n/2) or (j==n/2):
      