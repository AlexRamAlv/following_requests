const menu = document.querySelector(".menu-icon");
const navbar = document.querySelector(".navigation-bar");
const arrow = document.querySelector(".close-navbar");
const arrow_cont = document.querySelector(".close-icon");
const ul = document.querySelector("ul");

menu.addEventListener("click", () => {
    navbar.classList.toggle("spread");
});

window.addEventListener("click", function(e){
    if(navbar.classList.contains("spread") && e.target != navbar 
        && e.target != menu && e.target != ul && e.target != arrow_cont){
        navbar.classList.toggle("spread");
    }
});

window.addEventListener("scroll", function(e){
    if(navbar.classList.contains("spread") && e.target != navbar 
        && e.target != menu && e.target != ul && e.target != arrow_cont){
        navbar.classList.toggle("spread");
    }
});

arrow.addEventListener("click", () => {
    navbar.classList.toggle("spread");
});