from functools import reduce
Vet_num =[5,10,25,32]

produto_total = reduce(lambda aux, x: aux * x, Vet_num)
print(f'produto da lista vet_num: {produto_total}')