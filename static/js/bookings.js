//Used to validate form input before submitting to the server.
//Reduces bad requests to the server.
function validateForm()
{
    var form = document.forms["bookingRequestForm"];
    
    //make sure the form is full.
    if(form["arrivalDate"].value == "" || form["departureDate"].value == "" ||
    form["firstName"].value == "" || form["lastName"].value == "" ||
    form["email"].value == "" || form["room"].value == "")
    {
        alert("Please fill all fields of the booking request form.");
        return false;
    }

    //Try to read the dates. If the dates are invalid, let the user know.
    try
    {
        var arrivalDate = new Date(form["arrivalDate"].value);
        var departureDate = new Date(form["departureDate"].value);
        //If the arrival date is before or equal to today,
        //tell the user this is invalid.
        if(arrivalDate <= new Date())
        {
            alert("Arrival date must be in the future.");
            return false;
        }
        //If the arrival date is after the departure date,
        //tell the user this is invalid.
        else if(arrivalDate >= departureDate)
        {
            alert("Departure date must be after arrival date.");
            return false;
        }
    }
    catch(ex)
    {
        alert("Invalid date(s)")
        return false;
    }

    return true;
}