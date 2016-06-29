function checkScroll(){
    var startY = $('.navbar').height() * 2;

    if ($(window).scrollTop() > startY) {
         $('.navbar').addClass("scrolled");
    } else {
         $('.navbar').removeClass("scrolled");
    }
}

if($('.navbar').length > 0){
    $(window).on("scroll load resize", function(){
        checkScroll();
    });
}

$(document).ready(function(){

    $("#showlogin").click(function(){
        $("#loginModal").modal('show');
    });


    $('.thumb').hover(function(){
        $(this).find('.caption').css('opacity','1');
    }, function(){
        $(this).find('.caption').css('opacity','0');
    });

    $('.carousel').carousel({
        interval: 1800
    });

    $('.carousel').carousel('cycle');

});
