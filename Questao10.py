from sympy import symbols, And, Or, Not, Implies, Equivalent
import re

# Mapeamento de conectivos lógicos em linguagem natural para conectivos lógicos proposicionais
connectives = {
    "e": And,
    "ou": Or,
    "não": Not,
    "se e somente se": Equivalent,
    "então": Implies  # Marcação para tratamento especial
}


# Função para identificar proposições atômicas como grupos de palavras
def identify_propositions(sentence):
    # Lista de símbolos proposicionais
    symbols_list = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U', 'V', 'X', 'Y', 'Z']
    propositions = {}
    symbol_index = 0

    # Identificar partes da sentença que não são conectivos para mapeamento de proposições
    parts = re.split(r'\b(se e somente se|se|então|e|ou|não)\b', sentence, flags=re.IGNORECASE)

    for part in parts:
        part = part.strip()
        if part and part.lower() not in connectives:
            if symbol_index < len(symbols_list):
                propositions[part] = symbols(symbols_list[symbol_index])
                symbol_index += 1

    return propositions


# Função para traduzir a sentença em lógica proposicional usando sympy
def translate_to_propositional_logic(sentence):
    propositions = identify_propositions(sentence)

    # Substituir proposições atômicas por símbolos proposicionais
    for prop, symbol in propositions.items():
        sentence = sentence.replace(prop, f"{symbol}")

    # Processar a sentença para construir a expressão lógica
    words = re.split(r'\b(se e somente se|se|então|e|ou|não)\b', sentence, flags=re.IGNORECASE)
    expression = None
    i = 0
    negate_next = False

    while i < len(words):
        word = words[i].strip()
        if not word:
            i += 1
            continue

        print(f"Processing: '{word}'")

        if word.lower() == "não":
            negate_next = True
        elif word == "se" and i + 2 < len(words) and words[i + 2].strip().lower() == "então":
            antecedent = symbols(words[i + 1].strip())
            consequent = symbols(words[i + 3].strip())
            new_expr = Implies(antecedent, consequent)
            expression = new_expr if expression is None else And(expression, new_expr)
            i += 3
        elif word.lower() == "se e somente se" and expression is not None and i + 1 < len(words):
            consequent = symbols(words[i + 1].strip())
            expression = Equivalent(expression, consequent)
            i += 1
        elif word.lower() in connectives:
            if expression is None:
                expression = connectives[word.lower()](symbols(words[i - 1].strip()), symbols(words[i + 1].strip()))
            else:
                expression = connectives[word.lower()](expression, symbols(words[i + 1].strip()))
            i += 1
        else:
            expr = symbols(word.strip())
            if negate_next:
                expression = Not(expr)
                negate_next = False
            else:
                expression = expr if expression is None else And(expression, expr)

        i += 1

    return expression, propositions


# Exemplo de uso
if __name__ == "__main__":
    sentence = input("Digite uma sentença em linguagem natural: ")
    logic_expression, mapping = translate_to_propositional_logic(sentence)
    print("Sentença em lógica proposicional:", logic_expression)
    print("Mapeamento das proposições:", mapping)
