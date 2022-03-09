let ones_dict = {
    0 : "zero",
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
};

let teens_dict = {
    10 : "ten",
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
};

let tens_dict = {
    20 : "twenty",
    30 : "thirty",
    40 : "forty",
    50 : "fifty",
    60 : "sixty",
    70 : "seventy",
    80 : "eightty",
    90 : "ninety"
};

let hunds_dict = {
    100 : "one-hundred",
    200 : "two-hundred",
    300 : "three-hundred",
    400 : "four-hundred",
    500 : "five-hundred",
    600 : "six-hundred",
    700 : "seven-hundred",
    800 : "eight-hundred",
    900 : "nine-hundred"
};

let number = prompt("0-999, choose a number: ");

let tens_digit1 = Math.floor(number / 10) % 10;
let tens_digit2 = tens_digit1 * 10;
let ones_digit = number % 10;
let hunds_digit1 = Math.floor(number / 100)
let hunds_digit2 = hunds_digit1 * 100;
let teens_digit = number % 100 ;

if (number < 100) {
    if (number in ones_dict) {
        console.log(ones_dict[number])
    }
    else if (number in teens_dict) {
        console.log(teens_dict[number])
    }
        
    else if (number in tens_dict) {
        console.log(tens_dict[number])
    }

    else if (tens_digit2 in tens_dict && ones_digit in ones_dict) {
        console.log(`${tens_dict[tens_digit2]}-${ones_dict[ones_digit]}`)
    }
}
else{
    if (number in hunds_dict) {
        console.log(hunds_dict[number])
    }
    else if (tens_digit1 == 0){
        console.log(`${hunds_dict[hunds_digit2]}-${ones_dict[ones_digit]}`)
    }
    else if (tens_digit1 == 1){
        console.log(`${hunds_dict[hunds_digit2]}-${teens_dict[teens_digit]}`)
    }
    else if (ones_digit == 0){
        console.log(`${hunds_dict[hunds_digit2]}-${tens_dict[tens_digit2]}`)
    }         
    else if (hunds_digit2 in hunds_dict && tens_digit2 in tens_dict && ones_digit in ones_dict){
        console.log(`${hunds_dict[hunds_digit2]}-${tens_dict[tens_digit2]}-${ones_dict[ones_digit]}`)
    }
}