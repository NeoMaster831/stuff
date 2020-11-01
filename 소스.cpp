#define _CRT_SECURE_NO_WARNINGS
#include "opencv2/opencv.hpp"
#include <iostream>

using namespace std;

struct Ball {
	int x; int y;
};

Ball blue; Ball red;

int main() {
	
	int rows, cols;
	scanf("%d %d", &rows, &cols);
	char zzfQQ[100][100]; // rows&cols 저장할 곳

	for (int i = 0; i < rows; i++) {
		scanf("%s", &zzfQQ[i]);
	}

	for (int i = 0; i < rows; i++) { // 공 찾는곳
		for (int j = 0; j < cols; j++) {
			if (zzfQQ[i][j] == 'R') {
				red.y = i; red.x = j;
			}

			else if (zzfQQ[i][j] == 'B') {
				blue.y = i; blue.x = j;
			}
		}
	}

	int attempt = 0;

	for (int i = 0; i < 10; i++) { // rows 증가
		
		int redC[2]; redC[0] = red.x; redC[1] = red.y;
		int blueC[2]; blueC[0] = blue.x; blueC[1] = blue.y;

		if (zzfQQ[redC[0] + 1][redC[1]] == '.') { // 오른쪽이 . 이라면
			red.x = redC[0] + 1; // oldX -> newX
		}

		else if (zzfQQ[redC[0] - 1][redC[1]] == '.') { // 왼쪽이 . 이라면
			red.x = redC[0] - 1;
		}
		
		else if (zzfQQ[redC[0]][redC[1] + 1] == '.') { // 아래쪽이 . 이라면
			red.y = redC[1] + 1;
		}

		else if (zzfQQ[redC[0]][redC[1] - 1] == '.') { // 위쪽이 . 이라면
			red.y = redC[1] - 1;
		}

		// 이번엔 블루

		if (zzfQQ[blueC[0] + 1][blueC[1]] == '.') { // 오른쪽이 . 이라면
			blue.x = blueC[0] + 1; // oldX -> newX
		}

		else if (zzfQQ[blueC[0] - 1][blueC[1]] == '.') { // 왼쪽이 . 이라면
			blue.x = blueC[0] - 1;
		}

		else if (zzfQQ[blueC[0]][blueC[1] + 1] == '.') { // 아래쪽이 . 이라면
			blue.y = blueC[1] + 1;
		}

		else if (zzfQQ[blueC[0]][blueC[1] - 1] == '.') { // 위쪽이 . 이라면
			blue.y = blueC[1] - 1;
		}

		attempt++;

		// 목적지에 도달?
		if (zzfQQ[red.x][red.y] == 'O') {
			// blue?

			if (zzfQQ[blue.x][blue.y] == 'O') {
				printf("-1");
			}

			else printf("%d", attempt);
		}
	}

	printf("%d", attempt);
}