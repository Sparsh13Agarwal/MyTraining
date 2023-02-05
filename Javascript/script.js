// console.log("Hello");
// let name = 'sparsh';
// console.log(name);

// let element = document.getElementById('div1');
// //element = element.childNodes
// //console.log(element);
// element.style.color ="red"

// let sel = document.querySelector('#div1')
// console.log(sel)

// Array.from(sel).forEach()
function myFunction(){
    let person = prompt("please enter your name","Rohit");
    if(person!=null){
        document.getElementById("demo").innerHTML = "Hello" + person + "! How are you?";
    }
}
function mySum(){
    let a = prompt("please enter first number");
    let b = prompt("please enter second number");
    let c = parseFloat(a) +parseFloat(b);
    document.getElementById("demo1").innerHTML = "your sum is" + c;
}
const ages = [3,10,18,19,20];
function checkAge(age){
    return age>18;
}
function myFunc(){
    console.log(ages.find(checkAge));
}
myFunc()
// let x = null;
let y;

// console.log(x);
// console.log(y);
// console.log(x===y);

const emp ={
    fname: 'test',
    lname:'singh',
    age :22
}

let cars = ["BMW","Audi","Mercedes"];
const d = new Date('2023-01-24');
//console.log(d)
let x = 16 + "Volvo"
//console.log(x)
//let x ='hiii'  cannont redefine variable if

//console.table(emp)
// console.log(typeof cars)

a = ["hi","hellloo",2]
// console.log(a instanceof Array)

const Empp ={
    eid: "E101",
    fname: "James",
    lname: "Bond",
    fullName: function(){
        return this.fname + " "+this.lname;
    }
}
console.log("fullname:",Empp.fullName());

// x = new Number();  object of class Number 
// console.log(window)
// let temp = 10
// let v = (temp%2==0)?"even":"odd";
// console.log(v)

// let j = 1;
// while(j<10){
//     console.log(j);
//     j++;
// }

// for (let i =1;i<=10;i++){
//     if(i==6){
//         continue;
//     }
//     console.log('Number:'+i);
// }

//let day;
// let n = "Wednesday";
// switch(new Date().getDay()){
//     case 0:
//         day = "Sunday";break;
//     case 2:
//         day = "Tuesday";break;
//     case 6:
//         day = "Saturday";break;
//     default:
//         day = "........";
// }
// console.log(day);
var objImage = null;
function init() {
    objImage = document.getElementById("s1");
    objImage.style.position = "relative";
    objImage.style.left = "0px";
    objImage.style.top = "0px";
}
init()
function moveS(e){
    var key = e.which || e.keyCode || 0;
    switch(key){
        case 37:
            moveLeft();break;
        case 39:
            moveRight();break;
        case 38:
            moveUp();break;
        case 40:
            moveDown();
            break;
        
    }
}

function move(){
    for(var i=30;i<=2500;i++){
        return 20
    }
}
// function frame() {
//     if (pos == 350) {
//       clearInterval(id);
//     } else {
//       pos++; 
//       elem.style.top = pos + "px"; 
//       elem.style.left = pos + "px"; 
//     }
//   }

function moveLeft() {
    
    objImage.style.left = parseInt(objImage.style.left) - move() + "px";
    objImage.style.transform = 'rotateY(0deg)';
}
function moveUp() {
    objImage.style.top = parseInt(objImage.style.top) - move() + "px";
    objImage.style.transform = 'rotateZ(90deg)';
}
function moveRight() {
    objImage.style.left = parseInt(objImage.style.left) + move() + "px";
    objImage.style.transform = 'rotateY(180deg)';
    
}
function moveDown() {
    objImage.style.top = parseInt(objImage.style.top) + move() + "px";
    objImage.style.transform = 'rotateZ(180deg)';
}


// game over.....
// array methods

// const fruits = ["Banana","Orange","Apple","Mango"];
// console.log(fruits.toString());
// console.log(fruits.join("<>"));
// console.log(fruits.pop());
// console.log(fruits.push("kiwi"));
// console.log(fruits);

// let i =1;
// const myInterval = setInterval(function(){
//     console.log("here is the message number "+i);
//     i+=1;
// },2000);
// console.log(myInterval);
// setTimeout(function(){
//     clearInterval(myInterval);
// },1000);

// function = (variable,expression){

// }
// evalueates the expression
// find variable by variablename
// assign two result of expression
// return result of the expression

//--------------------------------------------------------------------
// const myObject ={
//     x:10,
//     y:true,
//     z: 'abc'
// }
// for (let key in myObject){
//     console.log(key, myObject[key])
// }
// let myobj = [1,2,3,4,5] 
// for (let key of myobj){
//     console.log(key);
// }
// console.log("hell")
//--------------------------------------------------------------------
// const Emp={
    
//     fullName:function(){
//         return this.fname +" "+this.lname
//     }   
// }
// const Emp1 ={
//     fname:"Rohit",
//     lname:"k"
// }
// const Emp2={
//     fname:"Rahul",
//     lname:"l"
// }
// Emp.fullName.call(Emp1);
// console.log(Emp.fullName.call(Emp2));
// //.apply(Emp1,["kiran","patel"])
//--------------------------------------------------------------------

// opps in javascript

// class Car {
//     constructor (name,year){
//         this.name = name;
//         this.year = year;
//     }
//     age(){
//         let date = new Date();
//         return date.getFullYear() - this.year
//     }
// }
// let mycar = new Car("BMW",2014);
// console.log("my car is "+ mycar.age()+" years old");

//--------------------------------------------------------------------
// class Emp {
//     static Company = "Bajaj Markets";
//     constructor(eid,ename,esal){
//         this.eid = eid;
//         this.ename = ename;
//         this.esal = esal;
//     }
//     set emp_id(eid){this.eid = eid;}
//     set emp_name(ename){this.ename=ename;}
//     set emp_sal(esal){this.esal = esal;}
//     get emp_id(){return this.eid;}
//     get emp_name(){return this.ename;}
//     get emp_sal(){return this.emp_sal;}
//     disp(){
//         console.log(this.eid,this.ename,this.esal);
//     }
//     static get_company(){return Emp.Company;}
// }
// let e1 = new Emp("E01","Rahul",10000);
// console.log(e1.disp(),Emp.get_company());

// console.log(e1.eid,e1.ename,e1.esal);
// e1.eid ="E002";
// e1.ename = "karan";
// e1.esal = 15000;
// console.log(e1.eid,e1.ename,e1.esal);
// Emp.Company = "BFDL";
// console.log(Emp.Company);

//--------------------------------------------------------------------
class Meetup{
    constructor(organizer){
        this.organizer = organizer;
    }
}
// inheritance using extends keyword
class TechMeet extends Meetup{
    constructor(organizer,techTopic){
        super(organizer);
        this.techTopic = techTopic
    }
}
let js = new TechMeet("JS Enterprise","Microservices");
console.log(js.organizer,js.techTopic);