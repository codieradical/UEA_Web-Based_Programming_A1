from flask import Flask, render_template, request
from src.io.csvHelper import readCsv, writeCsv

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
    #read the reviews list from file
    fileName = "db\\reviews.csv"
    reviewsList = readCsv(fileName)
    # add an entry to the reviews list
    reviewText = request.form[("review")]
    reviewRating = request.form[("rating")]
    newReview=[reviewText, reviewRating]
    reviewsList.append(newReview)
    #save the reviews list to the file
    writeCsv(reviewsList, fileName)
    return reviews()

@app.route("/reviews")
def reviews():
    #read the reviews list from file
    fileName = "db\\reviews.csv"
    reviewsList = readCsv(fileName)
    return render_template("reviews.html", reviewsList=reviewsList)
	
@app.route("/bookings", methods = ["POST"])
def addBooking():
    #read the bookings list from file
    fileName = "db\\bookings.csv"
    bookingsList = readCsv(fileName)
    # add an entry to the reviews list
    arrivalDate = request.form[("arrivalDate")]  
    departureDate = request.form[("departureDate")]
    firstName = request.form[("firstName")]
    lastName = request.form[("lastName")] 
    email = request.form[("email")]
    room = request.form[("room")]
    #The false at the end is the booking confirmation field.
    #This has to be set to true by the hotel owner in Excel in order to confirm bookings.
    newBooking=[arrivalDate, departureDate, firstName, lastName, email, room, False]
    bookingsList.append(newBooking)
    #save the bookings list to the file
    writeCsv(bookingsList, fileName)
    return bookings()

@app.route("/bookings")
def bookings():
#read the bookings list from file
    fileName = "db\\bookings.csv"
    bookingsList = readCsv(fileName)
    return render_template("bookings.html", bookingsList=bookingsList)

if __name__ == "__main__":
    app.run(debug = True)