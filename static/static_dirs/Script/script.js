$("document").ready(function(){
    
    
    $(".news-article").click(function(){
        $(".article-information-box").slideToggle(); 
    });
    
    $(".article-exit").click(function(){
        $(".article-information-box").slideToggle(); 
        $("body").css("overflow","auto");
    });

    
    $('a[href*="#"]').not('[href="#"]').not('[href="#0"]').click(function(event) {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            // Figure out element to scroll to
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            // Does a scroll target exist?
            if (target.length) {
                // Only prevent default if animation is actually gonna happen
                event.preventDefault();
                $('html, body').animate({
                    scrollTop: target.offset().top
                }, 1000, function() {
                    // Callback after animation
                    // Must change focus!
                    var $target = $(target);
                    
                });
            }
        }
    });
    
    

    $('#menu-test').click(function(){
       $('#test-menu').slideToggle();
    });
    
    $("#menu-cross").click(function(){
       $('#test-menu').slideToggle();
    });
    
     $('.about-requirements button').on('click', function(){
        val = $(this).attr('data-key');
        $('div[data-key='+val+']').slideToggle();
    });
    
})