let rot = {
    a: 'n', b: 'o', c: 'p', d: 'q', e: 'r', f: 's', 
    g: 't', h: 'u', i: 'v', j: 'w', k: 'x', l: 'y',
    m: 'z', n: 'a', o: 'b', p: 'c', q: 'd', r: 'e',
    s: 'f', t: 'g', u: 'h', v: 'i', w: 'j', x: 'k', 
    y: 'l', z: 'm',
    A: 'N', B: 'O', C: 'P', D: 'Q', E: 'R', F: 'S', 
    G: 'T', H: 'U', I: 'V', J: 'W', K: 'X', L: 'Y',
    M: 'Z', N: 'A', O: 'B', P: 'C', Q: 'D', R: 'E', 
    S: 'F', T: 'G', U: 'H', V: 'I', W: 'J', X: 'K', 
    Y: 'L', Z: 'M'
};

let schars = ['!', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.'];
let ciphered = '';
let input = prompt('enter text to be ciphered' );

for (let i = 0; i<input.length; i++) {
    if (input[i] === ' ') {
        ciphered += ' ';
    } else if (schars.includes(input[i])) {
        console.log(input[i])
        ciphered += input[i];
    } else {
    ciphered += rot[input[i]];
    }
}
alert(ciphered);