function viewImage(src){
    viewer = document.querySelector('#image-viewer');
    viewer.style.display = 'block';

    image = document.querySelector('#image-viewer-src')
    image.style.backgroundImage = "url('" + src + "')";
}

function closeViewer(){
    viewer = document.querySelector('#image-viewer');
    viewer.style.display = 'none';

    image = document.querySelector('#image-viewer-src')
    image.style.backgroundImage = "";
}