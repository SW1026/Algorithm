#include <stdio.h>

int
main(int argc, char **argv)
{
        char *pStr=NULL;
        int i, j, n;
        scanf("%d", &n);
        int x[n], y[n];
        int score[n];
        for(i=0; i<n; ++i)
        {
                scanf("%d %d", &x[i], &y[i]);
                score[i] = 1;
        }

        for(i=0; i<n; ++i)
        {
                for(j=0; j<n; ++j)
                {
                        if(i==j)
                                continue;
                        if(x[i] > x[j] && y[i] > y[j])
                        {
                                score[j] += 1;
                        }

                }
        }

        for(i=0; i<n; ++i)
        {
                printf("%d ",score[i]);
        }
}
