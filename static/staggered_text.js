document.getElementById('description').scrollTo(0, 1000000)

const delay = ms => new Promise(res => setTimeout(100, 100))

function staggeredTextOutput(){
    text = ">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    var text_elt = document.getElementById('description_text')
    for (let i = 0; i < text.length; i++){
        setTimeout(() =>{
        text_elt.innerHTML += text[i]
        }, i * 100)
    }
}