const fs = require("fs");
const input = fs.readFileSync(0, "utf-8").trim().split("\n");

const N = input[0];
const arr = input.slice(1);

for( let i =0; i<N; i++){
    const str = arr[i];
    let stack = [];
    let isVPS = true;
    
    for ( let j=0; j< str.length; j++){
        const ch = str[j]

        if(ch == '('){
            stack.push(ch);
        }
        else{
            if(!stack.length){
                isVPS = false;
               break;  
            }
            stack.pop();
        }
    }
    if(stack.length){
        isVPS = false;
    }
    if (isVPS) console.log("YES");
    else console.log("NO");
}