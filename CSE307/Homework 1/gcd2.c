#include <stdio.h>
#include <stdlib.h>

int main() {
	int i, j;
	scanf("%d",&i);
	scanf("%d",&j);
	while (i != j && i > 0 && j > 0) {
		if (i > j) i = i % j;
		else j = j % i;
	}
	if(i != 0) {
		printf("GCD = %d\n",i);	
	}
	else {
		printf("GCD = %d\n",j);
	}
	return 0;
}