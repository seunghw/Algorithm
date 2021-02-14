/**
 * 입출력과 사칙연산
 * 0129
 */

//1
console.log("Hello World!");

//2
console.log("강한친구 대한육군");
console.log("강한친구 대한육군");

//3   생략된 /를 출력하기 위해서는 하나 백슬레쉬를 하나 더 붙여야함 ex) \: = : 출력이된다.
console.log(`\\    /\\
)  ( ')
(  /  )
\\(__)|`);

console.log(`\\    /\\\n)  ( ')\n(  /  )\n\\(__)|`);

//4

console.log(`
|\\_/|
|q p|   /}
( 0 )"""\\
|"^"\`    |
\|\|_/=\\\\__|`);
console.log(`|\\_/|
|q p|   /}
( 0 )"""\\
|"^"\`    |
\|\|_/=\\\\__|`);

//5

var fs = require("fs");
var input = fs.readFileSync("/dev/stdin").toString().split(" ");
var a = parseInt(input[0]);
var b = parseInt(input[1]);
console.log(a + b);
