window.onload = function(){
    editables = document.querySelectorAll('.editable')
    for(var i = 0; i < editables.length; i++){
        editable = editables[i]
        editable.clicked = false;
        editable.addEventListener("click", function(){
            if(this.clicked == false){
                text = this.innerText;
                this.innerHTML = "<input type='text' value='" + text + "' >";
                this.clicked = true;
            }
        });
    }
}