const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const N = Number(input[0]);

let stack = [];
let result = [];

for (let i = 1; i <= N; i++) {
    const [command, value] = input[i].split(" ");

    if (command === "push") {
      stack.push(Number(value));
    } else if (command === "pop") {
      result.push(stack.length ? stack.pop() : -1);
    } else if (command === "size") {
      result.push(stack.length);
    } else if (command === "empty") {
      result.push(stack.length ? 0 : 1);
    } else if (command === "top") {
      result.push(stack.length ? stack[stack.length - 1] : -1);
    }
  }

console.log(result.join("\n"));