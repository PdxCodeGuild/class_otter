// let numbers = [5,0,8,3,4,1,6]

// function sum(numbers){
//     total_sum = 0
//     for (x of numbers){
//         total_sum += x
//         console.log(x)


//     }
//     return total_sum
// }
// let result = sum(numbers)
// let avg = result/numbers.length
// alert(`The average is ${avg}`)

let addNumberButton = document.querySelector('#add-number')
let numberInput = document.querySelector('#number-input')
let findAverageButton = document.querySelector('#find-average')
let output = document.querySelector('#output')
let numberList = []

addNumberButton.addEventListener('click', function(){
    let userInput = numberInput.value 
    numberList.push(userInput)
    console.log(numberList)

})
findAverageButton.addEventListener('click', function(){
    function sum(numbers){
            total_sum = 0
            for (x of numbers){
                total_sum += parseInt(x)
                console.log(typeof x)
        
        
            }
            return total_sum
        }
        let result = sum(numberList)
        let avg = result/numberList.length
        output.innerText = `The average is ${avg}`

})


// function findAverage()
// while (True){
//     let choice = alert('Enter a number or "done" to finish: ')
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

// event.preventDefault() - prevent page from reloading
// alert(`The average is ${avg}`)