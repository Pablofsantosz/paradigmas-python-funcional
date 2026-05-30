from functools import reduce
Vet_num =[10,25,1,7,9,62,75,81,11,19]

maior_num = reduce(lambda aux, x: aux if aux    > x else x, Vet_num)
print(f'Maior Numero: {maior_num}')