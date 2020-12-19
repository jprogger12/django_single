

(function ($) {
    "use Strict";
    /*--------------------------
    1. Newsletter Popup
    ---------------------------*/

    /*----------------------------
    2. Mobile Menu Activation
    -----------------------------*/
    $("#mobile-menu-expander").click(function() {
        $("body").css("overflow","hidden");
    });

    $("#mobile-menu-closer").click(function() {
        $("body").css("overflow","auto");
        $(".mobile-menu-expand").collapse("hide");
    });

    /*----------------------------
    3 Checkout Page Activation
    -----------------------------*/
     $('.categorie-title').on('click', function () {
    $('.vertical-menu-list').slideToggle();
    });

    $('#showlogin').on('click', function () {
        $('#checkout-login').slideToggle();
    });
    $('#showcoupon').on('click', function () {
        $('#checkout_coupon').slideToggle();
    });
    $('#cbox').on('click', function () {
        $('#cbox_info').slideToggle();
    });
    $('#ship-box').on('click', function () {
        $('#ship-box-info').slideToggle();
    });

    /*----------------------------
    4. NivoSlider Activation
    -----------------------------*/
    $('#slider').nivoSlider({
        effect: 'random',
        animSpeed: 300,
        pauseTime: 9000,
        directionNav: false,
        manualAdvance: false,
        controlNavThumbs: false,
        pauseOnHover: true,
        controlNav: true,
        prevText: "<i class='zmdi zmdi-chevron-left'></i>",
        nextText: "<i class='zmdi zmdi-chevron-right'></i>"
    });

    
    /*----------------------------------------------------
    10. Brand Banner Activation
    -----------------------------------------------------*/
$('.brand-banner').on('changed.owl.carousel initialized.owl.carousel', function (event) {
        $(event.target)

                .find('.owl-item').removeClass('last')
                .eq(event.item.index + event.page.size - 1).addClass('last');

            $(event.target)
                .find('.owl-item').removeClass('first')
                .eq(event.item.index).addClass('first')


        }).owlCarousel({
        loop: false,
        nav: true,
        dots: false,
        smartSpeed: 1200,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        margin: 1,
        responsive: {
            0: {
                items: 1,
                autoplay:true
            },
            900: {
                items: 5
            },
        }
    })

    /*----------------------------------------------------
    11. Blog Activation
    -----------------------------------------------------*/
    $('.blog-active').owlCarousel({
        loop: false,
        nav: false,
        dots: false,
        smartSpeed: 1000,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        margin: 30,
        responsive: {
            0: {
                items: 1,
                autoplay: true,
                nav: true
            },
            900: {
                items: 3
            }
        }
    })


    /*----------------------------------------------------
    12. Certificate Activation
    -----------------------------------------------------*/

    $('.certificates').owlCarousel({
        loop: true,
        nav: true,
        dots: false,
        smartSpeed: 1000,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        margin:30,
        responsive:{
            0:{
                items: 1,
                autoplay: true,
            },
            900:{
                items: 4
            }
        }
    })


    

    $(document).ready(function() {        
        
        $(".single-cert a").fancybox({
            'hideOnContentClick': true
        });
        
    });


    /*----------------------------
    13. WOW Js Activation
    -----------------------------*/
    new WOW().init();

    /*----------------------------
    14. ScrollUp Activation
    -----------------------------*/
    $.scrollUp({
        scrollName: 'scrollUp', // Element ID
        topDistance: '550', // Distance from top before showing element (px)
        topSpeed: 1000, // Speed back to top (ms)
        animation: 'fade', // Fade, slide, none
        scrollSpeed: 900,
        animationInSpeed: 1000, // Animation in speed (ms)
        animationOutSpeed: 1000, // Animation out speed (ms)
        scrollText: '<i class="fa fa-angle-up"></i>', // Text for element
        activeOverlay: false // Set CSS color to display scrollUp active point, e.g '#00FFFF'
    });

    /*----------------------------
    15. Sticky-Menu Activation
    ------------------------------ */
    $(window).on('scroll', function () {
        if ($(this).scrollTop() > 150) {
            $('.header-sticky').addClass("sticky");
        } else {
            $('.header-sticky').removeClass("sticky");
        }
    });

    /*----------------------------
    16. Price Slider Activation
    -----------------------------*/
    $("#slider-range").slider({
        range: true,
        min: 0,
        max: 80,
        values: [0, 74],
        slide: function (event, ui) {
            $("#amount").val("$" + ui.values[0] + "  $" + ui.values[1]);
        }
    });
    $("#amount").val("$" + $("#slider-range").slider("values", 0) +
        "  $" + $("#slider-range").slider("values", 1));

    /*--------------------------------
    17. Testimonial Slick Carousel
    -----------------------------------*/
    $('.testext_active').owlCarousel({
        loop: false,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        margin: 15,
        smartSpeed: 1000,
        nav: true,
        dots: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    })

    /*----------------------------------------------------
    18. Best Seller Activation
    -----------------------------------------------------*/
    $('.best-seller-pro').on('changed.owl.carousel initialized.owl.carousel', function (event) {
        $(event.target)
                .find('.owl-item').removeClass('last')
                .eq(event.item.index + event.page.size - 1).addClass('last');
        }).owlCarousel({
        loop: false,
        nav: true,
        dots: false,
        smartSpeed: 1000,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        margin: 0,
        responsive: {
            0: {
                items: 1,
                autoplay:true
            },
            480: {
                items: 2
            },
            768: {
                items: 2
            },
            1000: {
                items: 1
            }
        }
    })
    /*----------------------------------------------------
    19. Best Product Activation
    -----------------------------------------------------*/
    $('.best-seller-pro-two')
        .owlCarousel({
            loop: false,
            nav: false,
            dots: false,
            smartSpeed: 1200,
            margin: 0,
            responsive: {
                0: {
                    items: 1,
                    autoplay:true
                },
                768: {
                    items: 3
                },
                1000: {
                    items: 1
                }
            }
        })
    
    /*-------------------------------------
    20. Blog Realted Post activation
    --------------------------------------*/
    $('.blog-related-post-active').owlCarousel({
        loop: false,
        margin: 30,
        smartSpeed: 1000,
        nav: false,
        dots: false,
        items: 2,
        responsive: {
            0: {
                items: 1,
                autoplay:true
            },
            480: {
                items: 1
            },
            768: {
                items: 2
            },
            992:{
                margin: 29,
                items: 2
            },
            1200: {
                items: 2
            }
        }
    })
    
    /*----------------------------------------------------
    21.Best Seller  Unique Activation
    -----------------------------------------------------*/
    $('.best-seller-unique').on('changed.owl.carousel initialized.owl.carousel', function (event) {
        $(event.target)
                .find('.owl-item').removeClass('last')
                .eq(event.item.index + event.page.size - 1).addClass('last');
        }).owlCarousel({
        loop: false,
        nav: true,
        dots: false,
        smartSpeed: 1000,
        navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        margin: 0,
        responsive: {
            0: {
                items: 1,
                autoplay:true
            },
            768: {
                items: 2
            },
            1000: {
                items: 1
            }
        }
    })
     
    
})(jQuery);