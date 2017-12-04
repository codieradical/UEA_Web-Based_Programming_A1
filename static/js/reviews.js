function validateForm()
{
    //Get the from object.
    var form = document.forms["reviewForm"];
    
    //make sure the form is full.
    if(form["firstName"].value == "" || form["lastName"].value == "" ||
       form["text"].value == "" || form["rating"].value == "")
    {
        alert("Please fill all fields of the review form.");
        return false;
    }

    //Make sure the rating is a number.
    rating = 0;
    rating = parseFloat(form["rating"].value);

    //If not alert the user.
    if(isNaN(rating) || rating < 1 || rating > 5)
    {
        alert("Invalid rating number.");
        return false;
    }

    //Round the value to one decimal place, so a rating can be 4.5, but not 4.55.
    document.reviewForm.rating.value = (Math.round(rating * 10) / 10).toString();

    return true;
}