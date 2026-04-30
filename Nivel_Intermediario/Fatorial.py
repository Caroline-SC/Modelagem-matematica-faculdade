num = int(input("Digite um numero:"))

aux = num
for i in range(num-1,1,-1):
   aux *=  i

print(f'{num}! = {aux}')