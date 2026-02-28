// grabbing the content
let users = document.getElementById('users')
let reg = document.getElementById('reg')
let reg_f = document.getElementById('reg_f')
let appoint = document.getElementById('appoint')
let welcome = document.getElementById('welcome')



let home_btn = document.getElementById('home')
let register_btn = document.getElementById('registerd')
let booked_btn = document.getElementById('booked')
let reg_f_btn = document.getElementById('reg_f_btn')

// code for displaying each page

home_btn.addEventListener('click', function(e){
    e.preventDefault()
    welcome.style.display = 'flex'
    users.style.display = 'block'
    reg.style.display = 'none'
    appoint.style.display = 'none'
    reg_f.style.display = 'none'
})

register_btn.addEventListener('click', function(e){
    e.preventDefault()
    users.style.display = 'none'
    reg.style.display = 'block'
    appoint.style.display = 'none'
    welcome.style.display = 'none'
    reg_f.style.display = 'none'
})

booked_btn.addEventListener('click', function(e){
    e.preventDefault()
    users.style.display = 'none'
    reg.style.display = 'none'
    appoint.style.display = 'block'
    welcome.style.display = 'none'
    reg_f.style.display = 'none'
})

reg_f_btn.addEventListener('click', function(e){
    e.preventDefault()
    users.style.display = 'none'
    reg.style.display = 'none'
    appoint.style.display = 'none'
    welcome.style.display = 'none'
    reg_f.style.display = 'block'
})

