#include <stdio.h>

int main() {
	int street[] = {7, 106, 216, 432, 34560};
	int size = sizeof(street) / sizeof(street[0]);
	int target = 432;
	int res = -1;
	int low = 0;
	int high = size - 1;

	while (low <= high) {
		int mid = low + (high - low) / 2;
		if (street[mid] == target) {
			res = mid;
			break;
		}
		if (street[mid] < target) {
			low = mid + 1;
		} else {
			high = mid - 1;
		}
	}

	if (res != -1) {
		printf("This n found in: %d\n", res);
	} else {
		printf("N not founded\n");
	}
	return 0;
}

