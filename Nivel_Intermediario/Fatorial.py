def factorial(n):
   if n==1:
      return n
   else:
      return n* factorial(n-1)
   
num = int(input("Digite um numero:"))

print(f'')
print(f'{num}! = {factorial(num)}')