function flip(e){
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
}

var sliders = document.querySelectorAll('.image-slider');
for(var i = 0; i < sliders.length; i++){
        sliders[i].setAttribute('image-id', 0)

        images = sliders[i].getAttribute('images').split(',');

        sliders[i].style.backgroundImage = "url('" + images[0] + "')";
}

setInterval(function(){
    for(var i = 0; i < sliders.length; i++){
        flip(sliders[i])
    }
}, 5000);
