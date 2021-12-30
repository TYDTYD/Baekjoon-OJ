#include<stdio.h>
int main()
{
    int a,b;

    scanf("%d %d", &a, &b);

    if(a<=0 || a>=10 || b<=0 || b>=10)
        return 0;

    printf("%.15f", (double)a/b);

    return 0;
}
