#include <stdio.h>
#include <math.h>
int main() {
    //a^2+b^2=c^2
    double a, b;
    printf("Value for a: ");
    scanf("%lf", &a);
    printf("Falue for b: ");
    scanf("%lf", &b);
    double c = sqrt(a*a + b*b);

    printf("Hypotenuse is: %f\n", c);
}