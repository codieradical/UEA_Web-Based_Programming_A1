from flask import Flask, render_template, request
from src.io.csvHelper import readCsv, writeCsv

#A custom templates path is used to keep the project files organized.
templatesPath = "src\\templates"

app = Flask(__name__, template_folder=templatesPath)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/attractions")
def attractions():
    return render_template("attractions.html")

@app.route("/reviews", methods = ["POST"])
def addReview():
    #Read the reviews list csv.
    reviewsList = readCsv("db\\reviews.csv")
    #Add an entry to the list.
    reviewText = request.form[("review")]
    reviewRating = request.form[("rating")]
    newReview=[reviewText, reviewRating]
    reviewsList.append(newReview)
    #Write the edited list to the csv file.
    writeCsv(reviewsList, fileName)
    #Show the user the /reviews page.
    return reviews()

@app.route("/reviews")
def reviews():
    #Read the reviews list csv.
    reviewsList = readCsv("db\\reviews.csv")
    #Show the reviews page, with the reviews list data on the page.
    return render_template("reviews.html", reviewsList=reviewsList)
	
@app.route("/bookings", methods = ["POST"])
def addBooking():
    #Read the bookings list csv.
    bookingsList = readCsv("db\\bookings.csv")
    #Add an entry to the bookings list.
    arrivalDate = request.form[("arrivalDate")]  
    departureDate = request.form[("departureDate")]
    firstName = request.form[("firstName")]
    lastName = request.form[("lastName")] 
    email = request.form[("email")]
    room = request.form[("room")]
    bookingConfirmed = False
    newBooking=[arrivalDate, departureDate, firstName, lastName, email, room, bookingConfirmed]
    bookingsList.append(newBooking)
    #Write the edited list to the csv file.
    writeCsv(bookingsList, fileName)
    #Show the user the /bookings page.
    return bookings()

@app.route("/bookings")
def bookings():
    #Read the bookings list csv.
    bookingsList = readCsv("db\\bookings.csv")
    #Show the bookings page with the bookings list data on the page.
    return render_template("bookings.html", bookingsList=bookingsList)

if __name__ == "__main__":
    app.run(debug = True)