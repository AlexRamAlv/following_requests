/* --------------- Manipulating the DOM for views for requester -----------*/
// variables for the navigation bar
const menu = document.querySelector(".menu-icon");
const navbar = document.querySelector(".navigation-bar");
const arrow = document.querySelector(".close-navbar");
const arrow_cont = document.querySelector(".close-icon");
const ul = document.querySelector("ul");

// adding click event for the menu icon
menu.addEventListener("click", () => {
    navbar.classList.toggle("spread");
});
// listening events in any part of the document HTML
window.addEventListener("click", function(e){
    if(navbar.classList.contains("spread") && e.target != navbar 
        && e.target != menu && e.target != ul && e.target != arrow_cont){
        navbar.classList.toggle("spread");
    }
});
// adding scroll event for the menu icon
window.addEventListener("scroll", function(e){
    if(navbar.classList.contains("spread") && e.target != navbar 
        && e.target != menu && e.target != ul && e.target != arrow_cont){
        navbar.classList.toggle("spread");
    }
});
// adding click event for closing the avigation bar
arrow.addEventListener("click", () => {
    navbar.classList.toggle("spread");
});

/* ----------------------------- JQuery codes ----------------------------------*/

$("requester-card").on("click", ".requester-card .edit-icon", function(){

    alert("edit");
});

$("requester-card").on("click", ".requester-card .delete-icon", function(){

    alert("delete");
})