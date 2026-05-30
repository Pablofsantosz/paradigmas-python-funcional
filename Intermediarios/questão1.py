from functools import reduce
Vet_num =[10,25,32,47,59,61,74,81,99,100]

soma= reduce(lambda aux, x: aux + x, Vet_num)
print(f'Soma: {soma}')