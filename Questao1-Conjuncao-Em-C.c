#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;
    int c = 7;

    // Exemplo 1: Conjunção em uma decisão
    if (a < b && c > a) {
        printf("b é maior que a e c é maior que a\n"); // Verdadeiro, pois (5 < 10) && (7 > 5)
    }

    // Exemplo 2: Conjunção em uma atribuição
    int result = (a < b) && (c < b);
    printf("Resultado: %d\n", result); // Verdadeiro, pois (5 < 10) && (7 < 10) é verdadeiro (result = 1)

    return 0;
}
