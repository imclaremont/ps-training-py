const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const N = Number(input[0]);

let queue = new Array(N);
let head = 0;
let tail = 0;
let result = [];

for (let i = 1; i <= N; i++) {
  const temp = input[i];
  const [command, value] = temp.split(" ");

  if (command === "push") {
    queue[tail++] = Number(value);
  } else if (command === "pop") {
    result.push(head === tail ? -1 : queue[head++]);
  } else if (command === "size") {
    result.push(tail - head);
  } else if (command === "empty") {
    result.push(head === tail ? 1 : 0);
  } else if (command === "front") {
    result.push(head === tail ? -1 : queue[head]);
  } else if (command === "back") {
    result.push(head === tail ? -1 : queue[tail - 1]);
  }
}

console.log(result.join("\n"));