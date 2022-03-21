function testFunction() {
    document.getElementById("demo").innerHTML="Bruce's JavaScript string";
}

let person = {
    firstName:"Earl",
    lastName:"Scheib",
    business:"Automotive Finishing",
    age:67
}

person.age += 1
person['age'] +=1
person.age -= 2

let fruits = ['apple', 'peach', 'orange']

let persons = [person]

let name = prompt("Please enter your name")
alert("Hello " + name + "! How are you today?")


// a++
// ++a

// 1 < 2 < 3 ????

// Python Ternary
// x if <condition> else y
// JavaScript Ternary
//
function min(a, b) {
    return (a < b)? a: b
}
