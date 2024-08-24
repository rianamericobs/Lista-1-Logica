from sympy import symbols, simplify
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
from sympy.logic.inference import satisfiable

def parse_expression(expr, var_list):
    # Cria símbolos para cada variável
    variables = symbols(var_list)
    # Substitui os operadores lógicos por suas versões do sympy na expressão
    expr = (expr.replace("AND", "And")
                .replace("OR", "Or")
                .replace("NOT", "Not")
                .replace("IMPLIES", "Implies")
                .replace("IFF", "Equivalent"))
    # Avalia a expressão com os símbolos e as funções lógicas
    return eval(expr, {**{str(v): v for v in variables}, "And": And, "Or": Or, "Not": Not, "Implies": Implies, "Equivalent": Equivalent})

def classify_sentence(expr, var_list):
    sympy_expr = parse_expression(expr, var_list)
    simplified_expr = simplify(sympy_expr)
    if simplified_expr == True:
        return "Tautology"
    elif simplified_expr == False:
        return "Contradiction"
    elif satisfiable(sympy_expr):
        return "Satisfiable"
    else:
        return "Contradiction"

# Interface de usuário
if __name__ == "__main__":
    expr = input("Enter a logical expression (use AND, OR, NOT, IMPLIES, IFF): ")
    var_list = input("Enter the variables separated by commas (e.g., P, Q, R): ")
    result = classify_sentence(expr, var_list)
    print(f"The sentence '{expr}' is a {result}.")
