/* --------------- Manipulating the DOM for views for requester -----------*/
// variables for the navigation bar

// Showing and hiding modal form that add users by AJAX

const openModal = document.querySelector("#openModal");
const modalContainer = document.querySelector(".modal-container");
const closeModal = document.querySelector("#close-modal");

openModal.addEventListener("click", () =>{
    modalContainer.classList.add("show-modal");
});

closeModal.addEventListener("click", () =>{
    modalContainer.classList.remove("show-modal");
});

window.addEventListener("click", (event)=>{

    if (event.target == modalContainer) {
        modalContainer.classList.remove("show-modal");
    }
})


/* ----------------------------- JQuery codes ----------------------------------*/

$("requester-card").on("click", ".requester-card .edit-icon", function(){
    var $grandParent = this.parentElement.parentElement
    var $userInfo = $grandParent.children
    var name =  $userInfo[1].children[0].textContent
    console.log("edit " + name)
});

$("requester-card").on("click", ".requester-card .delete-icon", function(){

    alert("delete");
});