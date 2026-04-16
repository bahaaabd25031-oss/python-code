#include <stdio.h>
int main(){
    int arr[4][5] = {{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20}};
    int i , j;
    for(i = 0;i < 5;i++)
    {
        int sum = 0;
        for(j = 0;j < 4;j++)
        {
            sum += arr[j][i];
        }
        printf("the sum of coloumn %d is: %d\n",i+1,sum);
    }
    return 0;
}