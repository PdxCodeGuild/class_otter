var nums = ['5', '0', '8', '3', '4', '1', '6'];
alert('Your Numbers are:' +nums);

// function sum (num) {
var add = 0;

for(var i=0; i < nums.length; i++){
    add += parseInt(nums[i]);
}
console.log(add);
alert('The Total is:' +add);


// x = sum(nums) //call the function
let avg = add / nums.length;
console.log(avg);
alert('The average is' +avg);


// var name = "John Doe";

// function myFunction() {
//   alert('Hello ' + name);
// }
// <button onclick="myFunction()">Checkout</button>

// nums = [5, 0, 8, 3, 4, 1, 6]

// def sum(nums): #defining the function 'sum' with one parameter 'numbers'
//     add = 0 
//     for num in nums:
//         add = add + num
//     return add

// x = sum(nums) #call the function
// avg = x / len(nums)
// print (avg)