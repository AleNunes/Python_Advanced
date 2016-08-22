var slides, json, speed = 'fast';

var modal = (function() {
  var method = {}, $overlay, $modal, $content, $close;

  method.center = function() {
    var top, left;

    top = Math.max($(window).height() - $modal.outerHeight(), 0) / 2;
    left = Math.max($(window).width() - $modal.outerWidth(), 0) / 2;

    $modal.css({
      top : top + $(window).scrollTop(),
      left : left + $(window).scrollLeft()
    });
  };

  // Open the modal
  method.open = function(settings) {
    $content.empty().append(settings.content);

    $modal.css({
      width : settings.width || 'auto',
      height : settings.height || 'auto'
    });

    method.center();
    $(window).bind('resize.modal', method.center);
    $modal.show();
    $overlay.show();
  };

  method.close = function() {
    $modal.hide();
    $overlay.hide();
    $content.empty();
    $(window).unbind('resize.modal');
  };

  $overlay = $('<div id="overlay"></div>');
  $modal = $('<div id="modal"></div>');
  $content = $('<div id="content"></div>');
  $close = $('<a id="close" href="#">close</a>');

  $modal.hide();
  $overlay.hide();
  $modal.append($content, $close);

  $(document).ready(function() {
    $('body').append($overlay, $modal);
  });

  $close.click(function(e) {
    e.preventDefault();
    method.close();
  });

  return method;
}());

Slider = {
  now : '',
  total : '',
  slideContainer : '',
  nextSlide : function() {
    if (this.now < (this.total - 1)) {
      this.now++;
      $(".ativo").fadeOut(speed).removeClass("ativo").next()
          .fadeIn(speed).addClass("ativo");
      this.tratarBotoes();

    }
  },
  prevSlide : function() {
    if (this.now > 0) {
      this.now--;
      $(".ativo").fadeOut(speed).removeClass("ativo").prev()
          .fadeIn(speed).addClass("ativo");
      this.tratarBotoes();
    }
  },
  irPara : function(slide) {
    slide = slide-1;
    if (slide >= 0 && slide <= (this.total - 1)) {
      this.now = slide;
      $(".ativo").fadeOut(speed).removeClass("ativo");
      $('.slider img[alt="slide'+slide+'"]').fadeIn(speed).addClass("ativo");
      this.tratarBotoes();
    } else {
      alert('Slide inválido');
    }
  },
  tratarBotoes : function() {
    $('button[data="terminal"]').attr('disabled', !json[this.now].terminal);
    $('button[data="notas"]').attr('disabled', !json[this.now].notas);
  },
  loadDOM : function(dados) {
    console.log(dados);
  },
  init : function(dados) {

    // Load total of slides
    this.total = dados.length;

    // Define slider container
    this.slideContainer = $('.slider');

    // Make your slide in the first position
    this.now = 0;

    // Generate images in DOM
    for ( var i = 0; i < this.total; i++) {
      var img = document.createElement('img');
      img.src = dados[i].imgURL;
      img.setAttribute('alt', 'slide' + i);
      this.slideContainer.append(img);
    }

    // Load Slider and show the first image
    $(".slider img:first").fadeIn(speed).addClass("ativo");

    this.tratarBotoes();
  }
}

// Function to get KeyCode of your Keyboard
function getKey(event) {
  var key = event;

  switch (key) {
  case 37:
    Slider.prevSlide();
    break;
  case 39:
    Slider.nextSlide();
    break;
  }
}

jQuery(document).ready(function($) {

  // Load ressources from Json ressource
  $.ajax({
    dataType : 'JSON',
    type : 'GET',
    url : 'slides.json',

    success : function(data) {
      json = data;

      // Init Slider
      Slider.init(data);
    }
  });

  // Navigation by Keyboard
  $(document).keydown(function(event) {
    getKey(event.keyCode);
  });

  // Navation by Link
  $('.controllers').find('button').on('click', function() {

    var command = $(this).attr('data');

    switch (command) {
    case 'home':
      $('button[data="terminal"]').attr('disabled', true);
      $('button[data="notas"]').attr('disabled', true);
      Slider.now = 0;
      $(".ativo").removeClass("ativo");
      $(".slider img:first").fadeIn(speed).addClass("ativo");
      break;
    case 'prev':
      Slider.prevSlide();
      break;
    case 'next':
      Slider.nextSlide();
      break;
    case 'terminal':
      $.ajax({
        type : 'GET',
        url : './slides/terminal' + Slider.now + '.html',

        success : function(data) {
          modal.open({
            content : data
          });
        }
      });
      break;
    case 'notas':
      $.ajax({
        type : 'GET',
        url : './slides/notas' + Slider.now + '.html',

        success : function(data) {
          modal.open({
            content : data
          });
        }
      });
      break;
    case 'goto':
      var ir_para = prompt('Digite o numero do slide que você deseja ir (de 1 a '+ json.length +')');

      if (ir_para) {
        Slider.irPara(ir_para);
      }
      break;
    }
  });
});
