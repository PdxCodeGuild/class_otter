let user_num_list = []

while (true) {

    let user_num = prompt ("\nWelcome to the averaging tool, enter your number or 'done' to quit:\n")
    // console.log(user_num)
    if (user_num === "done") {

        let sum_user_num_list = 0

        for (let i = 0; i < user_num_list.length; i++) {
            sum_user_num_list += user_num_list[i]
            console.log(sum_user_num_list)
        }

        let answer = sum_user_num_list/user_num_list.length

        alert(`The average is : ${answer}`)

        break


    } else {

        user_num_list.push(parseInt(user_num))
        console.log(user_num_list)
        console.log(user_num)
    }
}