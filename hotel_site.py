"""Hotel site API"""
from flask import Flask, render_template, request
from datetime import datetime

from src.io.csv_helper import readcsv, writecsv
from src.auth.admin import requires_admin
from src.hotel.bookings import are_booking_dates_available

#A custom templates path is used to keep the project files organized.
app = Flask(__name__, template_folder="src\\templates")

@app.route("/")
def home(err=""):
    """Index Route (/)"""
    return render_template("home.html", err=err)

@app.route("/attractions")
def attractions(err=""):
    """Attractions Page Route ("/attractions")"""
    return render_template("attractions.html", err=err)

@app.route("/reviews", methods=["POST"])
def addreview(err=""):
    """Add Review Route (POST:/reviews)"""
    #Read the reviews list csv.
    reviews_list = readcsv("db\\reviews.csv")
    #Add an entry to the list.
    first_name = request.form[("firstName")]
    last_name = request.form[("lastName")]
    text = request.form[("text")]
    rating = request.form[("rating")]
    date_created = datetime.now().strftime("%A, %d %B %Y - %H:%M")

    #Validate form input
    print(first_name)
    if(not text or not rating
       or not first_name or not last_name):
        return reviews(err="Please fill in all form fields.")

    new_review = [first_name, last_name, text, rating, date_created]
    reviews_list.append(new_review)
    #Write the edited list to the csv file.
    writecsv(reviews_list, "db\\reviews.csv")
    #Show the user the /reviews page.
    return reviews()

@app.route("/reviews")
def reviews(err=""):
    """Reviews Page Route (/reviews)"""
    #Read the reviews list csv.
    reviews_list = readcsv("db\\reviews.csv")
    #Show the reviews page, with the reviews list data on the page.
    return render_template("reviews.html", reviews_list=reviews_list, err=err)

@app.route("/bookings/<index>/toggleConfirmed", methods=["GET"])
def confirmbooking(index):
    #Read the bookings list csv.
    bookings_list = readcsv("db\\bookings.csv")
    #Toggle the confirmed boolean in the booking.
    bookings_list[int(index)][6] = not bookings_list[int(index)][6].lower() == "true"
    #Write the edited list to the csv file.
    writecsv(bookings_list, "db\\bookings.csv")
    return Response('Toggled Confirmation.', 200, {})

@app.route("/bookings/<index>", methods=["DELETE"])
def deletebooking(index):
    #Read the bookings list csv.
    bookings_list = readcsv("db\\bookings.csv")
    #Delete the chosen booking from the list.
    del bookings_list[int(index)]
    #Write the edited list to the csv file.
    writecsv(bookings_list, "db\\bookings.csv")
    #Give a basic success response. This route is meant for AJAX, so no HTML response is needed.
    return Response('Deleted booking.', 200, {})

@app.route("/reviews/<index>", methods=["DELETE"])
def deletereview(index):
    #Read the reviews list csv.
    reviews_list = readcsv("db\\reviews.csv")
    #Delete the chosen review from the list.
    del reviews_list[int(index)]
    #Write the edited list to the csv file.
    writecsv(reviews_list, "db\\reviews.csv")
    #Give a basic success response. This route is meant for AJAX, so no HTML response is needed.
    return Response('Deleted review.', 200, {})

@app.route("/bookings", methods=["POST"])
def addbooking(err=""):
    """Add Booking Route (POST:/bookings)"""
    #Read the bookings list csv.
    bookings_list = readcsv("db\\bookings.csv")
    #Add an entry to the bookings list.
    arrival_date = request.form[("arrivalDate")]
    departure_date = request.form[("departureDate")]
    first_name = request.form[("firstName")]
    last_name = request.form[("lastName")]
    email = request.form[("email")]
    room = request.form[("room")]
    booking_confirmed = False
    date_created = datetime.now().strftime("%Y-%m-%d - %H:%M")

    #Validate form input
    print(first_name)
    if(not arrival_date or not departure_date
       or not first_name or not last_name
       or not email or not room):
        return bookings(err="Please fill in all form fields.")

    #Validate dates.
    arrival_date_datetime = datetime.strptime(arrival_date, "%Y-%m-%d")
    departure_date_datetime = datetime.strptime(departure_date, "%Y-%m-%d")
    err = are_booking_dates_available(arrival_date_datetime, departure_date_datetime, room)
    print(err)
    if err != "":
        return bookings(err=err)

    new_booking = [arrival_date, departure_date, first_name,
                   last_name, email, room, booking_confirmed, date_created]
    bookings_list.append(new_booking)
    #Write the edited list to the csv file.
    writecsv(bookings_list, "db\\bookings.csv")
    #Show the user the /bookings page.
    return bookings()

@app.route("/bookings")
def bookings(err=""):
    """Bookings Page Route (/bookings)"""
    #Read the bookings list csv.
    bookings_list = readcsv("db\\bookings.csv")

    displayed_bookings_list = []

    #Remove bookings that haven't been confirmed or are in the past.
    for booking in bookings_list:
        if(booking[6].lower() == "true" and datetime.strptime(booking[1], "%Y-%m-%d") > datetime.now()):
            displayed_bookings_list.append(booking)
    #Show the bookings page with the bookings list data on the page.
    return render_template("bookings.html", bookings_list=displayed_bookings_list, err=err)

@app.route("/admin")
@requires_admin
def admin(err=""):
    """Admin Page Route (/admin)"""
    bookings_list = readcsv("db\\bookings.csv")
    reviews_list = readcsv("db\\reviews.csv")
    return render_template("admin.html",
                           bookings_list=bookings_list, reviews_list=reviews_list, err=err)

if __name__ == "__main__":
    app.run(debug=True)
