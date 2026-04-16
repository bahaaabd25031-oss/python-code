#include <stdio.h>
int main(){
    int rows;
    int i , j , k;
    scanf("%d", &rows);
    for(i = 1;i <= rows;i++)
    {
        for(k = rows-i;k > 0;k--)
            printf(" ");
        for(j = 0;j < i;j++)
            printf("%d ",i);
        printf("\n");
    }
    return 0;
}