let hum_btn = document.getElementById('hum')
let links = document.getElementById('links')

//code that show navigation links when user clicks the hum-burger button.
hum_btn.addEventListener('click', function(e){
    e.preventDefault()
    if( hum_btn.classList == 'opn' || links.style.display == 'block'){
        links.style.display = 'none'
        hum_btn.classList.remove('opn')
    }
    else{
        links.style.display = 'block'
        hum_btn.classList.toggle('opn')
    }    

})

//code that minimize the navbar when the user scroll.
window.addEventListener('scroll',function(){
    let head = document.getElementById('navbar')
    head.classList.toggle('sticky',this.window.scrollY > 0)
})
