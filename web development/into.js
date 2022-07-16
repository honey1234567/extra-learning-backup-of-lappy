console.log("Hello");
//run code with node filename.js
//declare variable
let a;//by default it is undefined and 'let' it is of anytype
console.log(a)
//date types: primitive types:number(like integer),string,boolean,null
for(let i=1;i<=5;i++){
    console.log(i);
}
//Non primitive: function,arrays,object
   //function definition")
function sayHi(param){
    console.log(param);
    let rval = Math.random() > .5 ?true:"less tahn 0.5"
return rval;
 
}
//function call
sayHi();//undefined
sayHi(10);//10
let rval = sayHi([1,2]);
console.log(rval);

//object: group of key value pair
let cap ={
    name:"steve",
    sayHIII : function(){
console.log("HIIIIIIIIIIIIIII")
    }
}
console.log(cap.sayHIII());
console.log(cap.name)
//delete addres
delete cap.address;
//Arrays
let arr = [2,3];


let arr1 = arr.slice(1,2)//slice doesn't make copy insted it creates new array
console.log(arr1) //[3]
arr1.push("last");//[ 3, 'last' ]
arr.unshift("first")//[ first,3, 'last' ]
console.log(arr1)//
arr.splice(0,1);//from oth index remove 1 guy ,sploice chages actual array
console.log(arr)//[3]
// arr.pop() -removes last value
// arr.shift() -  removes first value
//string functions-charAt,substring(a,b],charCodeAt(index)-gives ascii value of character at index 4 in string
//                  split(character)-gives arry of string after splitting ,if split character was like str.split("") then output will 
 //                   be array of individual characters
 // ['a','b'].join('$')-"1$2"
 //string.trim()-removes lading and  back space from string
 //Note-browser searching is done on the basis of split with spaces and join with '+' of string
 

