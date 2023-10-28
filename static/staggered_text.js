fetch('/description')
    .then(response => response.text())
    .then(data => {
        staggeredTextOutput(data)
})

function staggeredTextOutput(text){
    var text_elt = document.getElementById('description_text')
    text_elt.innerHTML = '>';
    for (let i = 0; i < text.length; i++){
        setTimeout(() =>{
        text_elt.innerHTML += text[i];
        if (i > 308 && i % 77 == 0) document.getElementById('description').scrollTo(0, 10000)
        }, i * 20)
    }
}