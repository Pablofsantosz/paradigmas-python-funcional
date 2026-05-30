nomes = [
    "Lucas",
    "Beatriz",
    "Beca",
    "Rafael",
    "Camila",
    "Clara",
    "Eduardo",
    "Alice",
    "Luiza",
    "Samuel"
]

iniciais = set(
    map(
        lambda nome: nome[0],
        nomes
    )
)

resultado = dict(
    map(
        lambda inicial: (
            inicial,
            list(
                filter(
                    lambda nome: nome[0] == inicial,
                    nomes
                )
            )
        ),
        iniciais
    )
)

print(resultado)