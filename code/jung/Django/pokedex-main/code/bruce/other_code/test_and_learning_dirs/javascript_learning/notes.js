typeof ""             // Returns "string"
typeof "John"         // Returns "string"
typeof "John Doe"     // Returns "string"

typeof 0              // Returns "number"
typeof 314            // Returns "number"
typeof 3.14           // Returns "number"
typeof (3)            // Returns "number"
typeof (3 + 4)        // Returns "number"

let car0;    // Value is undefined, type is undefined
car0 = undefined;    // Value is undefined, type is undefined

let car1 = "";    // The value is "", the typeof is "string"

function myFunction(p1, p2) {
    return p1 * p2;   // The function returns the product of p1 and p2
}


function name(parameter1, parameter2, parameter3) {
    // code to be executed
}


// The code inside the function will execute when "something" invokes (calls) the function:
// When an event occurs (when a user clicks a button)
// When it is invoked (called) from JavaScript code
// Automatically (self invoked)


let x = myFunction(4, 3);   // Function is called, return value will end up in x

function myFunction(a, b) {
  return a * b;             // Function returns the product of a and b
}


function toCelsius(fahrenheit) {
    return (5/9) * (fahrenheit-32);
}

document.getElementById("demo").innerHTML = toCelsius(77);


const car = {type:"Fiat", model:"500", color:"white"};

const person0 = {firstName:"John", lastName:"Doe", age:50, eyeColor:"blue"};

const person1 = {
    firstName: "John",
    lastName: "Doe",
    age: 50,
    eyeColor: "blue"
};

// Accessing Object Properties
// You can access object properties in two ways:
objectName.propertyName
objectName["propertyName"]

person.lastName;
person["lastName"];

