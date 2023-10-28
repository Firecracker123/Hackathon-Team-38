document.getElementById('description').scrollTo(0, 1000000)

const delay = ms => new Promise(res => setTimeout(100, 100))
function staggeredTextOutput(){
    text = ">This is a description"
    var text_elt = document.getElementById('description_text')
    for (let i = 0; i < text.length; i++){
        setTimeout(() =>{
        text_elt.innerHTML += text[i]
        }, i * 100)
    }
}