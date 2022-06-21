document.querySelector("#navOpen").addEventListener("click", ()=> {
    document.querySelector(".nav-links-holder").style.top = "45%"
    document.querySelector("#navOpen").style.display = "none"
    document.querySelector("#navClose").style.display = "block"
    document.querySelector("#bb").style.overflow = "hidden"
})

document.querySelector("#navClose").addEventListener("click", ()=> {
    document.querySelector(".nav-links-holder").style.top = "-45%"
    document.querySelector("#navOpen").style.display = "block"
    document.querySelector("#navClose").style.display = "none"
})

// setInterval(()=>document.location.reload(), 5000 ) 