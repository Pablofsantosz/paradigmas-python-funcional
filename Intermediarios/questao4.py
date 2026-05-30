from functools import reduce
Vet_num =[4,5,1,15,9,12,8,3,15]

filtra_dobra = list(map(lambda x: x * 2, filter(lambda x: x > 5, Vet_num)))
print(f"numeros maiores que 5 dobrados {filtra_dobra}")
