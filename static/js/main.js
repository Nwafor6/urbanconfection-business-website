document.querySelector("#navOpen").addEventListener("click", ()=> {
    document.querySelector(".nav-links-holder").style.top = "390%"
    document.querySelector("#navOpen").style.display = "none"
    document.querySelector("#navClose").style.display = "block"
    document.querySelector("#bb").style.overflow = "hidden"
})

document.querySelector("#navClose").addEventListener("click", ()=> {
    document.querySelector(".nav-links-holder").style.top = "-390%"
    document.querySelector("#navOpen").style.display = "block"
    document.querySelector("#navClose").style.display = "none"
})

const button = document.querySelector('button');
button.addEventListener('click', () =>{
    document.querySelector("#success-msg").style.display="none"
}
    )



// setInterval(()=>document.location.reload(), 5000 ) 