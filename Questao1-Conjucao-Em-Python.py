a = 5
b = 10
c = 7

# Exemplo 1: Conjunção em uma decisão
if a < b and c > a:
    print("b é maior que a e c é maior que a")  # Verdadeiro, pois (5 < 10) and (7 > 5)

# Exemplo 2: Conjunção em uma atribuição
result = (a < b) and (c < b)
print("Resultado:", result)  # Verdadeiro, pois (5 < 10) and (7 < 10) é verdadeiro (result = True)
