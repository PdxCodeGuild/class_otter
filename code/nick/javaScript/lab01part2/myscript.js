function creditCardvalidator(originalNumbers) {
    let arrayOfstring = originalNumbers.split(''); // turns the card to an array of strings
    let arrayOfnum = arrayOfstring.map(Number); // turns the array of string into an array of numbers
    let checkDigit =
        arrayOfnum.splice(-1, arrayOfnum.length);
    console.log(arrayOfnum);
    return originalNumbers
}


alert(creditCardvalidator('4556737586899855'))