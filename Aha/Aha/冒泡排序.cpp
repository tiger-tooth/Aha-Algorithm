#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
//int main()
//{
//	int a[100], i, j, t, n;
//	scanf("%d", &n);
//	for (i = 1; i <= n; i++)
//	{
//		scanf("%d", &a[i]);
//	}
//
//	for (i = 1; i <= n - 1; i++)
//	{
//		for (j = 1; j <= n - i; j++)
//		{
//			if (a[j] < a[j + 1])
//			{
//				t = a[j];
//				a[j] = a[j + 1];
//				a[j + 1] = t;
//			}
//		}
//	}
//	for (i = 1; i <= n; i++)
//	{
//		printf("%d ", a[i]);
//	}
//	getchar();
//	getchar();
//	return 0;
//}

struct student
{
	char name[21];
	int score;
};

int main()
{
	int a[100], i, j, t, n;

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		scanf("%d", &a[i]);
	}



		getchar();
		getchar();
		return 0;

}


