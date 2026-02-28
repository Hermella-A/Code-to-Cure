let pswd_input =  document.getElementById('password')
let phone_input =  document.getElementById('phone_number')
let role = document.getElementById('roles')
let opt = ['Staff','Patient']



role.addEventListener('change', function(){
    if (role.value == opt[0]){
        document.getElementById('text').innerHTML = 'Choose your role'
        pswd_input.style.display = 'block'
        phone_input.style.display = 'none'
    }
    else if (role.value == opt[1]){
        document.getElementById('text').innerHTML = "Fill the spaces"
        pswd_input.style.display = 'none'
        phone_input.style.display = 'block'
    }
})