"""Hotel site API"""
from flask import Flask, render_template, request, Response
from datetime import datetime

from server.src.io.csv_helper import readcsv, writecsv
from server.src.auth.admin import requires_admin
from server.src.hotel.bookings import are_booking_dates_available

reviews_csv_path = "server\\db\\reviews.csv"
bookings_csv_path = "server\\db\\bookings.csv"

#A custom templates path is used to keep the project files organized.
app = Flask(__name__, template_folder="server\\src\\templates", static_url_path="/static", static_folder='client\\static')

@app.route("/")
#The "err" keyword can be used to show an erorr dialogue to the user.
def index(err=""):
    """Index Route (/)"""
    return render_template("index.html", err=err)

@app.route("/attractions")
def attractions(err=""):
    """Attractions Page Route ("/attractions")"""
    return render_template("attractions.html", err=err)

@app.route("/reviews/<index>", methods=["DELETE"])
def deletereview(index):
    #Read the reviews list csv.
    reviews_list = readcsv(reviews_csv_path)
    #Delete the chosen review from the list.
    del reviews_list[int(index)]
    #Write the edited list to the csv file.
    writecsv(reviews_list, reviews_csv_path)
    #Give a basic success response. This route is meant for AJAX, so no HTML response is needed.
    return Response('Deleted review.', 200, {})

@app.route("/reviews", methods=["POST"])
def addreview():
    """Add Review Route (POST:/reviews)"""
    #Read the reviews list csv.
    reviews_list = readcsv(reviews_csv_path)
    #Gather data from the review form.
    first_name = request.form[("firstName")]
    last_name = request.form[("lastName")]
    text = request.form[("text")]
    rating = request.form[("rating")]
    date_created = datetime.now().strftime("%A, %d %B %Y - %H:%M")

    #Validate form input
    if(not text or not rating
       or not first_name or not last_name):
        return reviews(err="Please fill in all form fields.")

    #Create a new review.
    new_review = [first_name, last_name, text, rating, date_created]
    #Add the new review to the list.
    reviews_list.append(new_review)
    #Write the edited list to the csv file.
    writecsv(reviews_list, reviews_csv_path)
    #Show the user the /reviews page.
    return reviews()

@app.route("/reviews")
def reviews(err=""):
    """Reviews Page Route (/reviews)"""
    #Read the reviews list csv.
    reviews_list = readcsv(reviews_csv_path)
    #Show the reviews page, with the reviews list data on the page.
    return render_template("reviews.html", reviews_list=reviews_list, err=err)

@app.route("/bookings/<index>/toggleConfirmed", methods=["GET"])
def confirmbooking(index):
    #Read the bookings list csv.
    bookings_list = readcsv(bookings_csv_path)
    #Toggle the confirmed boolean in the booking.
    bookings_list[int(index)][6] = not bookings_list[int(index)][6].lower() == "true"
    #Write the edited list to the csv file.
    writecsv(bookings_list, bookings_csv_path)
    return Response('Toggled Confirmation.', 200, {})

@app.route("/bookings/<index>", methods=["DELETE"])
def deletebooking(index):
    #Read the bookings list csv.
    bookings_list = readcsv(bookings_csv_path)
    #Delete the chosen booking from the list.
    del bookings_list[int(index)]
    #Write the edited list to the csv file.
    writecsv(bookings_list, bookings_csv_path)
    #Give a basic success response. This route is meant for AJAX, so no HTML response is needed.
    return Response('Deleted booking.', 200, {})

@app.route("/bookings", methods=["POST"])
def addbooking():
    """Add Booking Route (POST:/bookings)"""
    #Read the bookings list csv.
    bookings_list = readcsv(bookings_csv_path)
    #Gather new booking details from the form
    arrival_date = request.form[("arrivalDate")]
    departure_date = request.form[("departureDate")]
    first_name = request.form[("firstName")]
    last_name = request.form[("lastName")]
    email = request.form[("email")]
    room = request.form[("room")]
    booking_confirmed = False  #Booking confirmation must be set to true by the admin. 
    date_created = datetime.now().strftime("%Y-%m-%dT%H:%MZ")

    #Validate form input
    if(not arrival_date or not departure_date
       or not first_name or not last_name
       or not email or not room):
        return bookings(err="Please fill in all form fields.")

    #Validate dates.
    arrival_date_datetime = datetime.strptime(arrival_date, "%Y-%m-%d")
    departure_date_datetime = datetime.strptime(departure_date, "%Y-%m-%d")
    err = are_booking_dates_available(arrival_date_datetime, departure_date_datetime, room)
    if err != "":
        return bookings(err=err)

    #Create a new booking
    new_booking = [arrival_date, departure_date, first_name,
                   last_name, email, room, booking_confirmed, date_created]
    #Add the new booking to the list.
    bookings_list.append(new_booking)
    #Write the edited list to the csv file.
    writecsv(bookings_list, bookings_csv_path)
    #Show the user the /bookings page.
    return bookings()

@app.route("/bookings")
def bookings(err=""):
    """Bookings Page Route (/bookings)"""
    #Read the bookings list csv.
    bookings_list = readcsv(bookings_csv_path)

    displayed_bookings_list = []

    #Remove bookings that haven't been confirmed or are in the past.
    for booking in bookings_list:
        #If the booking is confirmed and in the future.
        if (booking[6].lower() == "true" and
                datetime.strptime(booking[1], "%Y-%m-%d") > datetime.now()):
            #Add it to the display list.
            displayed_bookings_list.append(booking)

    #Show the bookings page with the bookings list data on the page.
    return render_template("bookings.html", bookings_list=displayed_bookings_list, err=err)

@app.route("/admin")
@requires_admin #Requires admin authentication.
def admin(err=""):
    """Admin Page Route (/admin)"""
    #Read bookings and reviews and pass them to the template, so the admin can view and edit them.
    bookings_list = readcsv(bookings_csv_path)
    reviews_list = readcsv(reviews_csv_path)
    return render_template("admin.html",
                           bookings_list=bookings_list, reviews_list=reviews_list, err=err)

if __name__ == "__main__":
    app.run(debug=True)
