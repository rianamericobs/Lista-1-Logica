from sympy import symbols, simplify
from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent


def parse_expression(expr):
    # Substitui os operadores lógicos por suas versões do sympy na expressão
    expr = (expr.replace("AND", "&")
            .replace("OR", "|")
            .replace("NOT", "~")
            .replace("IMPLIES", ">>")
            .replace("IFF", "=="))
    return expr


def are_equivalent(expr1, expr2):
    # Extrair todos os símbolos únicos nas duas expressões
    var_set = set(expr1.replace('(', '').replace(')', '').split()) | set(
        expr2.replace('(', '').replace(')', '').split())
    variables = symbols(' '.join(var_set))

    # Parsear as expressões para objetos sympy
    parsed_expr1 = eval(parse_expression(expr1), {**{str(v): v for v in variables}})
    parsed_expr2 = eval(parse_expression(expr2), {**{str(v): v for v in variables}})

    # Simplificar a expressão de equivalência das duas expressões
    equivalence = Equivalent(parsed_expr1, parsed_expr2)

    # Verificar se a equivalência é uma tautologia
    is_equiv = simplify(equivalence)
    return is_equiv


# Interface de usuário
if __name__ == "__main__":
    expr1 = input("Enter the first logical expression (use AND, OR, NOT, IMPLIES, IFF): ")
    expr2 = input("Enter the second logical expression (use AND, OR, NOT, IMPLIES, IFF): ")
    if are_equivalent(expr1, expr2):
        print("The sentences are logically equivalent.")
    else:
        print("The sentences are not logically equivalent.")
