// function scope, block scope, global scope

m =4; 
n =2;
if(m>n){
    var p =4;
}
console.log(p); //accessible
if(m>n){
    let g = 4;
}
//console.log(g) // not accessible    let defined varibale cannot be access outside the scope
if(m>n)
{
    const h =4;
}
//console.log(h); // not accessible

// function scope.....

function f1(){
    let v1 = 9;
}
function f2(){
    let v2 = 10;
}
function f3(){
    const v3 = 12;
}
//console.log(v1,v2,v3); // not accessible outside the fn.

//global scope....
var v5 = 43;
let v6 = 5;
let v7 = 55;

function check(){
    v5 =66;
    v6 = 77;
}
console.log(v5,v6,v7);

document.getElementById("demo").innerHTML =
"Browser inner window width: " + window.innerWidth + "px<br>" +
"Browser inner window height: " + window.innerHeight + "px";












