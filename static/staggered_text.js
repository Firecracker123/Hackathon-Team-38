staggeredTextOutput('Type in \'start\' to play')

function staggeredTextOutput(text){
    var text_elt = document.getElementById('description_text')
    text_elt.innerHTML = '>';
    for (let i = 0; i < text.length; i++){
        setTimeout(() =>{
        text_elt.innerHTML += text[i];
        }, i * 100)
    }
}