const fs = require("fs");
const N = fs.readFileSync(0, "utf-8").trim().split("\n");

const queue = [];

for ( let i = 0; i< N; i++){
    queue[i] = i+1;
}

let head = 0;
let tail = N;

while (tail - head > 1) {
    head++;
    queue[tail++] = queue[head++];
}

console.log(queue[head]);