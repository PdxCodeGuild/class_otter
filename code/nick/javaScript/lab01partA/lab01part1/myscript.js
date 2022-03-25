nums = [5, 0, 8, 3, 4, 1, 6];

function sumofNums(sum, num) {
    return sum + num;
}
let sum = nums.reduce(sumofNums);
let amountofNums = (nums.length);

console.log(nums);
console.log('average ' + sum / amountofNums)