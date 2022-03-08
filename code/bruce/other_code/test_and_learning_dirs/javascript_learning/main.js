// setTimeout(hide_element, 750)
// setTimeout(show_element, 1500)

function hide_element() {
    document.getElementById('element-to-hide').style.display='none'
}
function show_element() {
    document.getElementById('element-to-hide').style.display='block'
}

function externalChangeText() {
    document.getElementById('external-js-change-id').innerHTML="The new test!"
}

function externalChangeTextBack() {
    document.getElementById('external-js-change-id').innerHTML="Initial text"
}


function promptThenAddTwoNumbers() {
    first_number = prompt("First number:");
    second_number = prompt("second number:");
    result = parseFloat(first_number) + parseFloat(second_number);
    document.getElementById('add-two-numbers').innerHTML = result;
    // Display result and user clicks 'OK' or presses 'Enter'.
    window.alert(result);
    // alert(result)
    console.log(result);
    // window.print(result);
}


// Keyword	Description
// var	Declares a variable
// let	Declares a block variable
// const	Declares a block constant
// if	Marks a block of statements to be executed on a condition
// switch	Marks a block of statements to be executed in different cases
// for	Marks a block of statements to be executed in a loop
// function	Declares a function
// return	Exits a function
// try	Implements error handling to a block of statements

function waitTime(thingToDisplay, time) {
    setTimeout(document.getElementById("loop-for-5").innerHTML=thingToDisplay, time)
}

function cycleNumbers() {
    let i = 0;
    while (i < 6) {
        waitTime(i, 1000)
    }
    i++
}

// Display numbers in window.alert()
function promptAndContinue() {
    i = 0
    while (i < 6) {
        number = prompt("Enter a number:")
        window.alert(number)
    }
    i++
}

let length = 16;                               // Number
let lastName = "Johnson";                      // String
let x = {firstName:"John", lastName:"Doe"};    // Object