#include <stdio.h>

int main() {
    int a = 5;
    int b = 10;

    // Exemplo 1: Negação em uma decisão
    if (!(a > b)) {
        printf("a não é maior que b\n"); // Verdadeiro, pois !(5 > 10) é verdadeiro
    }

    // Exemplo 2: Negação em uma atribuição
    int result = !(a < b);
    printf("Resultado: %d\n", result); // Falso, pois !(5 < 10) é falso (result = 0)

    return 0;
}
