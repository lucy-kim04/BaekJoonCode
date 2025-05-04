// https://www.acmicpc.net/problem/1018

const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const board = input.slice(1).map((line) => line.trim().split(''));

let minPaint = Infinity;

for (let i = 0; i <= N - 8; i++) {
  for (let j = 0; j <= M - 8; j++) {
    let count1 = 0; // W부터 시작하는 경우
    let count2 = 0; // B부터 시작하는 경우

    for (let x = 0; x < 8; x++) {
      for (let y = 0; y < 8; y++) {
        const curr = board[i + x][j + y];
        const shouldBeWhite = (x + y) % 2 === 0;

        if (shouldBeWhite) {
          if (curr !== 'W') count1++; // W로 시작해야 하는데 다르면 칠해야 함
          if (curr !== 'B') count2++; // B로 시작해야 할 경우 반대
        } else {
          if (curr !== 'B') count1++;
          if (curr !== 'W') count2++;
        }
      }
    }

    minPaint = Math.min(minPaint, count1, count2);
  }
}

console.log(minPaint);
