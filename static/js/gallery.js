var imageNumber = 0;

//Currently only supports
    //-1, previous image.
    //0, no change.
    //1, next image.
//Other values may cause bound issues.
function changeImage(imageNumberChange) {
    var images = document.getElementsByClassName("hotelImg");
    imageNumber += imageNumberChange;

    if (imageNumber > images.length)
        imageNumber = 0;
    if (imageNumber < 0)
        imageNumber = images.length;

    for (i = 0; i < images.length; i++)
        images[i].style.display = "none";

    images[imageNumber].style.display = "block";
}