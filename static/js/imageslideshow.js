var imageNo = 1;
showImage(imageNo);

function changeImage(n) {
    
    showImage(imageNo += n);
    
}

function showImage(n) {

    var i;
    var images = document.getElementsByClassName("hotelimg");

    if (n > images.length) {
        imageNo = 1;
    }

    if (n < 1) {
        imageNo = images.length;
    }

    for (i = 0; i < images.length; i++) {
        images[i].style.display = "none";
    }

    images[imageNo - 1].style.display = "block";

}