from flask import Flask, render_template,request
import csv

app = Flask(__name__)     

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/attractions')
def attractions(): 
    return render_template('attractions.html')

@app.route('/reviews', methods = ['GET'])
def reviews():
    #read the reviews list from file
    fileName = 'static\\reviews.csv'
    reviewsList = readFile(fileName)
    return render_template('reviews.html',reviewsList=reviewsList)
	
@app.route('/reviews', methods = ['POST'])
def addReview():
    #read the reviews list from file
    fileName = 'static\\reviews.csv'
    reviewsList = readFile(fileName)
    # add an entry to the reviews list
    newReview = request.form[('review')]
    newRating = request.form[('rating')]
    newEntry=[newReview, newRating]
    reviewsList.append(newEntry)
    #save the reviews list to the file
    writeFile(reviewsList, fileName)
    return render_template('reviews.html',reviewsList=reviewsList)
	
def readFile(aFile):
#read a file and return a list
    with open(aFile, 'r') as inFile: 
        reader = csv.reader(inFile)
        aList = [row for row in reader]
    return aList

def writeFile(aList, aFile):
#write a list to file
    with open(aFile, 'w', newline='') as outFile:
        writer = csv.writer(outFile)
        print(aList)
        writer.writerows(aList)      
    return
	
@app.route('/bookings')
def bookings():
#read the bookings list from file
    fileName = 'static\\bookings.csv'
    bookingsList = readFile(fileName)
    return render_template('bookings.html',bookingsList=bookingsList)

@app.route('/bookings', methods = ['POST'])
def addContact():
    #read the bookings list from file
    fileName = 'static\\bookings.csv'
    bookingsList = readFile(fileName)
    # add an entry to the reviews list
    firstName = request.form[('fName')]  
    lastName = request.form[('lName')]
    tel = request.form[('tel')] 
    email = request.form[('email')] 
    newContact=[firstName,lastName,tel,email]
    bookingsList.append(newContact)
    #save the bookings list to the file
    writeFile(bookingsList, fileName)
    return render_template('bookings.html',bookingsList=bookingsList)
	
if __name__ == '__main__':
    app.run(debug = True)