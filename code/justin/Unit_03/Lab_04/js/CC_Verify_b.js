
class CC_Verify {
    constructor() { }

    run() {
        let number_to_validate = parseInt(document.getElementById('CC_number').value);
        
        let numbers_as_list = this.convert_to_int_list(number_to_validate);
        let separated_values = this.slice_check_digit(numbers_as_list);
        let check_digit = separated_values.checkDigit;
        numbers_as_list = separated_values.numberList;
        numbers_as_list.reverse();
        numbers_as_list = this.double_even_elements(numbers_as_list);
        numbers_as_list = this.reduce_to_single_digits(numbers_as_list);
        let number_list_sum = numbers_as_list.reduce((a, b) => a + b);

        document.getElementById('CC_valid').innerHTML = `${number_to_validate} is ${this.validate_sum(number_list_sum, check_digit) ? 'valid!' : 'invalid.'}`;
    }

    convert_to_int_list(value=4556737586899855) {
        let results = [];
        let value_as_string = String(value);
        for (let index in value_as_string) {
            let character = value_as_string[index];
            results.push(parseInt(character));
        }
        return results;
    }

    slice_check_digit(number_list) {
        let check_digit = number_list[number_list.length - 1];
        return { checkDigit: check_digit, numberList: number_list.slice(0, -1) };
    }

    double_even_elements(number_list) {
        for (let index = 0; index < number_list.length; index++) {
            if (index % 2 == 0) {
                number_list[index] *= 2;
            }
        }
        return number_list;
    }

    reduce_to_single_digits(number_list) {
        for (let index = 0; index < number_list.length; index++) {
            if (number_list[index] > 9) {
                number_list[index] -= 9;
            }
        }
        return number_list;
    }

    validate_sum(sum, check_digit) {
        if (sum > 99) {
            sum = sum / 10;
        }

        let digit_to_validate = sum % 10;

        return digit_to_validate == check_digit;
    }
}