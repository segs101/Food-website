let input = document.querySelector('.input')
let show = document.querySelector('.show')

show.addEventListener('click', ()=>{
    show.classList.toggle('hide')
    if(input.type === 'password'){
        input.type = 'text';
    }
    else{
        input.type = 'password'
    }
})

function myFunction() {
  var x = document.getElementById("nav-links");
  if (x.className === "nav-link") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}