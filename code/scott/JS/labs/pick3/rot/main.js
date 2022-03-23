let rot = { 'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm' }

let form = document.querySelector('#form')

let string = document.querySelector('#string')

let results = document.querySelector('#results')

form.addEventListener('submit', function (event) {
    event.preventDefault()
    let user = string.value
    // let user = prompt('Enter your string')
    let password = ''
    for (let i = 0; i < user.length; i++) {
        let letter = user[i]
        password += rot[letter]
    }
    console.log(password)
    console.log(user)
    results.innerHTML = password
})