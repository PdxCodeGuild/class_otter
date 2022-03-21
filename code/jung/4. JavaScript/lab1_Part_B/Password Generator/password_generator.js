let number = document.getElementById("number")
let getNums = document.getElementById("get_nums")
let result = document.getElementById("result")
let lowercase = document.getElementById('lowercase')
let uppercase = document.getElementById('uppercase')
let numbers = document.getElementById('numbers')
let symbols = document.getElementById('symbols')

let values = {
    lowercases: 'abcdefghijklmnopqrstuvwxyz',
    uppercases: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    numbers: '0123456789',
    symbols: "!@#$%^&*(){}[]=<>/,.",
};
// console.log(lowercase.value)
function generatePassword() {
    let container = "";

    if (lowercase.value === "1") {
        container += values.lowercases;
    };

    if (uppercase.value === "1") {
        container += values.uppercases;
    };

    if (numbers.value === "1") {
        container += values.numbers;
    };

    if (symbols.value === "1") {
        container += values.symbols;
    };

    let outcome = "";
    
    for (let i = 0; i < number.value; i++) {
        outcome += container[Math.floor(Math.random()*container.length)]
    };
    return outcome;

}


getNums.addEventListener('click', function(){
    let answer = generatePassword()
    result.innerText = answer
})