function fadeOut(element) {
    var op = 1;  // initial opacity
    var timer = setInterval(function () {
        if (op <= 0.1){
            clearInterval(timer);
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op -= 0.05;
    }, 50);
}

function fadeIn(element) {
    var op = 0;  // initial opacity
    element.style.filter = 'alpha(opacity=' + op * 100 + ")";
    var timer = setInterval(function () {
        if (op >= 1.0){
            console.log('ready')
            clearInterval(timer);
        }
        element.style.opacity = op;
        element.style.filter = 'alpha(opacity=' + op * 100 + ")";
        op += 0.05;
    }, 50);
}

function flip(e){

    fadeIn(e)

    images = e.getAttribute('images').split(',');
    image_id = parseInt(e.getAttribute('image-id'));
    new_image_id = 1;

    console.log(images[i]);
    
    if(image_id < images.length-2){
        new_image_id = image_id + 1;
    }else{
        new_image_id = 0;
    }

    e.setAttribute('image-id', new_image_id)
    e.style.backgroundImage = "url('" + images[new_image_id] + "')";

    //fadeOut(e)
}

var sliders = document.querySelectorAll('.image-slider');
for(var i = 0; i < sliders.length; i++){
        fadeIn(sliders[i])

        sliders[i].setAttribute('image-id', 0)

        images = sliders[i].getAttribute('images').split(',');

        sliders[i].style.backgroundImage = "url('" + images[0] + "')";


}

setInterval(function(){
    for(var i = 0; i < sliders.length; i++){
        flip(sliders[i])
    }
}, 7000);
