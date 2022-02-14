function showAndHideItemsInNavBar()
{

    var $navbar = $(".navbar");
    var $items = $(".nav-items");
    var $admin = $(".admin");

    if($navbar.hasClass("span") && $items.hasClass("show-items") && $admin.hasClass("show-admin")){
        $navbar.toggleClass("span");
        $items.toggleClass("show-items");
        $admin.toggleClass("show-admin");
    } 
}

$(window).scroll(showAndHideItemsInNavBar);

$(".main-container").click(showAndHideItemsInNavBar);

$(".hamburguer").on("click", function(){

    $(".navbar").toggleClass("span");
    $(".nav-items").toggleClass("show-items");
    $(".admin").toggleClass("show-admin");
});