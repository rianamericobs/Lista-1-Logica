#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int c = 3;

    // Exemplo 1: Disjunção em uma decisão
    if (a > b || c < b) {
        printf("a é maior que b ou c é menor que b\n"); // Verdadeiro, pois (5 > 10) || (3 < 10)
    }

    // Exemplo 2: Disjunção em uma atribuição
    int result = (a > b) || (c > b);
    printf("Resultado: %d\n", result); // Falso, pois (5 > 10) || (3 > 10) é falso (result = 0)

    return 0;
}
