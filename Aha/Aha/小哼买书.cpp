#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main()
{
	int a[1001], i, j, t, n;

	for (i = 1; i <=1000; i++)
	{
		a[i] == 0;
	}

	scanf("%d", &n);

	for (i = 1; i <= n; i++)
	{
		scanf("%d", &t);
		a[t] = 1;
	}

	for (i = 1; i <= 1000; i++)
	{
		if (a[i] == 1)
			printf("%d ", i);
	}						 

	getchar();
	getchar();
	return 0;
}
