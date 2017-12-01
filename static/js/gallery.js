var imageNumber = 1;

//Currently only supports:
    //-1, previous image.
    //0, no change.
    //1, next image.
//Other values may cause bound issues.
function changeImage(imageNumberChange) {

    if(imageNumberChange > 1 || imageNumberChange < -1)
    console.warn("Image number change out of bounds. This may cause issues.")

    var images = document.getElementsByClassName("hotelImg");
    imageNumber += imageNumberChange;

    if (imageNumber > images.length)
        imageNumber = 1;
    if (imageNumber < 1)
        imageNumber = images.length;

    console.debug("Changing to image " + imageNumber);

    for (i = 0; i < images.length; i++)
        images[i].style.display = "none";

    images[imageNumber - 1].style.display = "block";
}