#define _CRT_SECURE_NO_WARNINGS

#include<stdio.h>
int main()
{
	int a[10], i, j;
	for (i = 0; i < 10; i++)
	{
		a[i] = 0;
	}

	for (i = 0; i < 5; i++)
	{
		scanf("%d", &j);
		a[j]++;
	}
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < a[i]; j++)
		{
			printf("%d", i);
		}
	}



	getchar();
	getchar();
	return 0;
}