//Used to delete a booking from the CSV based on it's index.
function deleteBooking(index)
{
    console.debug("deleting booking " + index);
    var xhttp = new XMLHttpRequest(); //Create a new XMLHttpRequest object.
    xhttp.open("DELETE", "/bookings/" + index.toString(), true); //Open a web request to delete the booking.
    xhttp.send(); //Send the request.
}

//Used to toggle confirmation of a booking in the CSV based on it's index.
function toggleConfirmed(index)
{
    console.debug("toggling confirmation of booking " + index);
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/bookings/" + index.toString() + "/toggleConfirmed", true);
    xhttp.send();
}

//Used to delete a review from the CSV based on it's index.
function deleteReview(index)
{
    console.debug("deleting review " + index);
    var xhttp = new XMLHttpRequest();
    xhttp.open("DELETE", "/reviews/" + index.toString(), true);
    xhttp.send();
}