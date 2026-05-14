#include <stdio.h>

int main() {
	int num[] = {1, 5, 10, 50};
	int ch = 10000000;

	for (int i=3; i >= 0; i--) {
		int count = ch / num[i];
		ch = ch % numbers[i];

		if (count > 0) {
			printf("If the denomination of a coin is %d, then you need %d of these coins.\n", numbers[i], count);
		}
	}
	return 0;


}
