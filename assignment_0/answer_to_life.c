#include<stdio.h>

void main()
{
	int a[100];
	int i = 1, j;
	scanf("%d",&a[0]);
	printf("1st scan result %d %c\n",a[0],a[0]);
	if (a[0]>-100 && a[0]<100)
	{
		while((a[i-1]!=42) && (i<100) && (a[i-1]>-100) && (a[i-1]<100))
		{
			printf("inside while loop");
			scanf("%d",&a[i]);	
			i++;
		}

		for(j=0;j<i-1;j++)
		{
			printf("inside for loop; a[%d]=%d; i is: %d\t",j,a[j],i);
			printf("%d\n",a[j]);
		}
	}
}
