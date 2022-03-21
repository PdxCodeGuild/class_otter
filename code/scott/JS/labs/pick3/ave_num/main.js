
let nums = [5,0,8,3,4,1,6]

function sum(nums){
    total_sum = 0
    for (x of nums){
        total_sum += x
        console.log(x)
    }
    return total_sum
}
let result1 = sum(nums)
let avg1 = result1/nums.length
alert(`The average is ${avg1}`)


// let numberlist = []

// while (True){
//     let choice = promt('Enter a number or "done" to finish: ')
//     if (choice == 'done'){
//         break
//     }
//     else{
//         let choice = int(choice)
//         numberlist.append(choice)
//     }
// }
// let result = sum(numberlist)
// let avg = result / numberlist.length

// alert(`The average is ${avg}`)