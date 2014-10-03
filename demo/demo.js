// chain call will be unjoined
$('.element').toggleClass('active').show().animate({height: '200px'}).find('.subelement').hide();

// chain call will be joined
$('.element').
  toggleClass('active').
  show().
  animate({height: '200px'});