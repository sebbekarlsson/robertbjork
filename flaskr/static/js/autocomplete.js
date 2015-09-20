window.onload = function(){
    inputs = document.querySelectorAll('input')
    for(var i = 0; i < inputs.length; i++){
        inputs[i].setAttribute('autocomplete', 'off');
    }
}