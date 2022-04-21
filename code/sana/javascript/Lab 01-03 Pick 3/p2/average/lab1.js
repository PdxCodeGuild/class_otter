let nlist = []
let add = document.getElementById('add');
let submit = document.getElementById('submit');
let input = document.getElementById('input');
let average = document.getElementById('average');
let ulist = document.getElementById('list');
let total = 0

function addToList(e) {
    nlist.push(' ' + parseInt(input.value));
    ulist.innerText = nlist
    input.value = '';
}
add.addEventListener('click', addToList);


input.addEventListener('keydown', function(i) {
    if (i.key === "enter") {
        addToList(input);
    }
});
submit.addEventListener('click', function() {
    for (let i=0; i<nlist.length; i++) {
        if (nlist[i]) {
            total += parseFloat(nlist[i])
        }
    }
    let final = total / nlist.length;
    average.innerText = `average is ${final}`
});


