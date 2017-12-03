"""Booking related functions."""
from datetime import datetime

from src.io.csv_helper import readcsv

def are_booking_dates_available(arrival_date, departure_date, room):
    """Validates a booking timespan.
    Returns an error message if the timespan is errornous.
    Returns an empty string if there are no problems."""
    #Check that the arrival date is in the future.
    if arrival_date <= datetime.now():
        return "The arrival date must be in the future."
    #Check that the departure date is after the arrival date.
    if arrival_date >= departure_date:
        return "Departure date must be after arrival date."
    #Prevent double booking.
    bookings_list = readcsv("db\\bookings.csv")
    for booking in bookings_list:
        if room == booking[5] and booking[6].lower() == "true":
            booked_arrival_date = datetime.strptime(booking[0], "%Y-%m-%d")
            booked_departure_date = datetime.strptime(booking[1], "%Y-%m-%d")
            if not(arrival_date < booked_departure_date and booked_arrival_date > departure_date):
                return "Room " + booking[5] + " is already booked during this timespan!"
    #No errors.
    return ""
