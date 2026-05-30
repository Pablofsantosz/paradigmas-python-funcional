fibonacci = lambda numero: (
    numero
    if numero <= 1
    else fibonacci(numero - 1) + fibonacci(numero - 2)
)

x=20

resultado = list(
    map(
        fibonacci,
        range(x)
    )
)

print(resultado)