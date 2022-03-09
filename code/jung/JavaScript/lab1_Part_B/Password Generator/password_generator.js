let number = document.getElementById("number")
let getNums = document.getElementById("get_nums")
let result = document.getElementById("result")

let values = {
    lowercases: 'abcdefghijklmnopqrstuvwxyz',
    uppercases: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    numbers: '0123456789',
    symbols: "!@#$%^&*(){}[]=<>/,.",
};

function generatePassword() {
    container = "";

    let lowercase = window.confirm("Would you like to use lowercase letters?");
        if (lowercase) {
            container += values.lowercases;
        };

    let uppercase = window.confirm("Would you like to use uppercase letters?");
        if (uppercase) {
            container += values.uppercases;
        };

    let numbers = window.confirm("Would you like to use numbers?");
        if (numbers) {
            container += values.numbers;
        };

    let symbols = window.confirm("Would you like to use symbols?");
        if (symbols) {
            container += values.symbols;
        };

    result = "";
    
    for (let i = 0; i < length; i++) {
        result += container[Math.floor(Math.random()*container.length)]
    };
    return result;
}


getNums.addEventListener('click', function(){
    let answer = generatePassword()
    result.innerText = answer
})