const fs = require('fs');
const input = fs
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);

const N = input[0].trim();
const shirt = input[1].trim().split(' ');
const arr = input[2].trim().split(' ');

const T = arr[0];
const P = arr[1];

let sum = 0;

for (let i = 0; i < shirt.length; i++) {
  sum += Math.ceil(shirt[i] / T);
}

console.log(sum);

const answer = Math.floor(N / P);

console.log(answer + ' ' + N - answer * P);
