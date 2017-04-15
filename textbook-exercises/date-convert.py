#date-convert.py
#   Converts a date from "mm/dd/yyyy" to "month day, year"

def main:
    #get the date
    dateStr = input("Enter a date mm/dd/yyyy: ")

    #split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    #convert monthStr to the full month name
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    #output result in "month day, year" format

main()
