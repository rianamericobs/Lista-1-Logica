a = 5
b = 10
c = 3

# Exemplo 1: Disjunção em uma decisão
if a > b or c < b:
    print("a é maior que b ou c é menor que b")  # Verdadeiro, pois (5 > 10) or (3 < 10)

# Exemplo 2: Disjunção em uma atribuição
result = (a > b) or (c > b)
print("Resultado:", result)  # Falso, pois (5 > 10) or (3 > 10) é falso (result = False)
