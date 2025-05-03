const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input.shift()); //shift -> 첫번째 요소 제거, 제거한 요소 반환
const numbers = input[0].split(' ').map(Number);

function findPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

//sqrt -> 제곱근, 약수는 제곱근 이하에 존재함으로 제곱근 이하로 설정

const primeCount = numbers.filter(findPrime).length;
console.log(primeCount);
