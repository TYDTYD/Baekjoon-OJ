#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n;
    int w;
    int money=0;

    scanf("%d %d", &n, &w);

    int* s=malloc(sizeof(int)*n);

    for(int i=0; i<n; i++)
    {
        scanf("%d", &s[i]);
        if(i==0 && s[i+1]>s[i])
        {
            w=w-s[i]*(w%s[i]);
            money=money+s[i]*(w%s[i]);
        }
        else if(s[i]>s[i-1] && s[i]<s[i+1] && i!=0 && i!=n-1)
        {
            w=w+s[i]*(w%s[i]);
            money=money-s[i]*(w%s[i]);
        }
        else if(s[i]<s[i-1] && s[i]>s[i+1] && i!=0 && i!=n-1)
        {
            w=w-s[i]*(w%s[i]);
            money=money+s[i]*(w%s[i]);
        }
        else if(i==n-1 && s[i]>s[i-1])
        {
            w=
        }

    }

    printf("%d", w);

    free(s);

    return 0;
}
