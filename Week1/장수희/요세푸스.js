const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const [N,K] = input[0].split(" ").map(Number);

const arr = [];

for ( let i =0; i< N; i++){
    arr[i] = i+1;
}

let result = [];

while(arr.length){
    for ( let i =0; i< K - 1; i++){
       arr.push(arr.shift());
    }
    result.push(arr.shift())
}

console.log("<" + result.join(", ") + ">")