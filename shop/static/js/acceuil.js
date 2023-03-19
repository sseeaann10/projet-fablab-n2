$(".carousel").swipe({

  swipe: function(event, direction, distance, duration, fingerCount, fingerData) {

    if (direction == 'left') $(this).carousel('next');
    if (direction == 'right') $(this).carousel('prev');

  },
  allowPageScroll:"vertical"

});


const menu = document.querySelector(".toggle-menu");
    const nav = document.querySelector(".navbar");
    const con = document.querySelector(".content");

    menu.addEventListener("click", () => {
        nav.classList.toggle('open');

    })
    
    $(document).ready(function(){
      var height = $('.footer').height();
      $('.sect-t-footer').css('height', height);
    });



