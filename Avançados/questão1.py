import csv


with open("emprestimo.csv", newline="") as arquivo:

    leitor_arquivo_csv = csv.DictReader(arquivo)

    
    emprestimos = list(
        map(
            lambda linha: {
                "id": int(linha["id"]),
                "valor": float(linha["valor"]),
                "quantidade": int(linha["quantidade"])
            },
            leitor_arquivo_csv
        )
    )
    
emprestimos_maiores = list(filter(lambda emprestimo: emprestimo["valor"] > 1000,emprestimos))

emprestimos_com_juros = list(
    map(
        lambda emprestimo: {
            "id": emprestimo["id"],
            "valor_original": emprestimo["valor"],
            "valor_com_juros": emprestimo["valor"] * 1.10,
            "quantidade": emprestimo["quantidade"]
        },
        emprestimos_maiores
    )
)

print(emprestimos_com_juros)