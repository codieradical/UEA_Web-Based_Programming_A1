"""Hotel site API"""
from flask import Flask, render_template, request
from src.io.csv_helper import readcsv, writecsv
from datetime import datetime

#A custom templates path is used to keep the project files organized.
app = Flask(__name__, template_folder="src\\templates")

@app.route("/")
def home():
    """Index Route (/)"""
    return render_template("home.html")

@app.route("/attractions")
def attractions():
    """Attractions Page Route ("/attractions")"""
    return render_template("attractions.html")

@app.route("/reviews", methods=["POST"])
def addreview():
    """Add Review Route (POST:/reviews)"""
    #Read the reviews list csv.
    reviews_list = readcsv("db\\reviews.csv")
    #Add an entry to the list.
    text = request.form[("text")]
    rating = request.form[("rating")]
    date_created = datetime.now().strftime("%A, %d %B %Y - %H:%M")
    new_review = [text, rating, date_created]
    reviews_list.append(new_review)
    #Write the edited list to the csv file.
    writecsv(reviews_list, "db\\reviews.csv")
    #Show the user the /reviews page.
    return reviews()

@app.route("/reviews")
def reviews():
    """Reviews Page Route (/reviews)"""
    #Read the reviews list csv.
    reviews_list = readcsv("db\\reviews.csv")
    #Show the reviews page, with the reviews list data on the page.
    return render_template("reviews.html", reviews_list=reviews_list)

@app.route("/bookings", methods=["POST"])
def addbooking():
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
    date_created = datetime.now().strftime("%A, %d %B %Y - %H:%M")
    new_booking = [arrival_date, departure_date, first_name,
                   last_name, email, room, booking_confirmed, date_created]
    bookings_list.append(new_booking)
    #Write the edited list to the csv file.
    writecsv(bookings_list, "db\\bookings.csv")
    #Show the user the /bookings page.
    return bookings()

@app.route("/bookings")
def bookings():
    """Bookings Page Route (/bookings)"""
    #Read the bookings list csv.
    bookings_list = readcsv("db\\bookings.csv")
    #Show the bookings page with the bookings list data on the page.
    return render_template("bookings.html", bookings_list=bookings_list)

if __name__ == "__main__":
    app.run(debug=True)
