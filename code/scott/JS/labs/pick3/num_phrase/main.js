
// Translate from Python
// Number to Phrase

const num_to_phrase_ones = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "",
}
const num_to_phrase_tens = {
    1: "teen ",
    2: "twenty ",
    3: "thirty ",
    4: "forty ",
    5: "fifty ",
    6: "sixty ",
    7: "seventy ",
    8: "eighty ",
    9: "ninety ",
    0: "",
}

const num_to_phrase_hund = {
    1: "one hundred ",
    2: "two hundred ",
    3: "three hundred ",
    4: "four hundred ",
    5: "five hundred ",
    6: "six hundred ",
    7: "seven hundred ",
    8: "eight hundred ",
    9: "nine hundred ",
    0: "",
}

function num_to_phrase(num){
    num = num.toString();
    if (num.length<2) {
        num ="00" + num;
    }
    if (num.length<3) {
        num = "0" + num;
    }
    let ones_digit = num[2];
    let tens_digit = num[1];
    let hund_digit = num[0];
    let ones_phrase = num_to_phrase_ones[ones_digit];
    let tens_phrase = num_to_phrase_tens[tens_digit];
    let hund_phrase = num_to_phrase_hund[hund_digit];
    console.log(hund_phrase + tens_phrase + ones_phrase);
    if (tens_digit == "1") {
        if (num[0] == "0"){
            if (ones_digit == "0") {
                tens_phrase = "ten";
                if (num[0] == "0"){
                    return ones_phrase + tens_phrase
                } else {    
                    return hund_phrase + "and " + ones_phrase + tens_phrase
                }
            }else 
                return ones_phrase + tens_phrase
        }else {
            return hund_phrase + "and " + ones_phrase + tens_phrase;
    } 
    } else if (num[1] == "0" && num[2] =="0" ){
        return hund_phrase
    } else if (num[0] == "0" && num[1] =="0" ){
        return ones_phrase
    } else if (num[0] == "0"){
        return tens_phrase + ones_phrase
    } else {
        return hund_phrase + "and " + tens_phrase + ones_phrase;
    }
    
}
let num = prompt("enter a number:")
alert(num_to_phrase(num));