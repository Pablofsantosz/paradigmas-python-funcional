nomes = ["pablo", "joao", "maria", "ana", "carlos", "lucas", "juliana"]
print(f"Lista de nomes minusculos: {nomes}")

maiusculas_nomes = list(map(lambda nome: nome.upper(), nomes))
print(f"Lista de nomes em maiusculas: {maiusculas_nomes}")
