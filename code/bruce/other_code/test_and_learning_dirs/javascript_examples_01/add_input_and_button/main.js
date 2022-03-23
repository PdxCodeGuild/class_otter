// Demonstrate how to add an <input>, a <h1>, and a <button> to the document.body.
// The 'document.body' represents the <body> element in the html page, which we are adding elements to.
// When we add elements (via 'appendChild' or similar), they will show up in the rendered HTML on the web page.

// Beginning page has stuff above and below the <body> but we are only adding stuff within it.
// I almost forgot the add the <script> tag to 'index.html' to run 'main.js'.

// Current <body> rendered on page:

// <!DOCTYPE html>
// <html lang="en">
// <head>
//     <meta charset="UTF-8">
//     <meta http-equiv="X-UA-Compatible" content="IE=edge">
//     <meta name="viewport" content="width=device-width, initial-scale=1.0">
//     <title>Document</title>
// </head>
// <body>
//     <script src="main.js"></script>
// </body>
// </html>

// From now on, we'll only show the contents of the <body>.

// Create an input box and place it in the <body>.
// Step 01: Create an <input> object (an HTMLInputElement):
let theInputBox = document.createElement('input')
// Step 02: Add ('appendChild') 'theInputBox' to the document.body:
document.body.appendChild(theInputBox)
// Does the <input> show in page HTML? Yes.

{/* 
<body>
    <script src="main.js"></script>
    <input>
</body>
*/}
