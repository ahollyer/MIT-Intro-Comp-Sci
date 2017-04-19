def main():
    # Get the date
    date_str = input("Enter a date (mm/dd/yyy): ")

    # Split into components
    month_str, day_str, year_str = date_str.split("/")

    # Convert month_str to the month name
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_str = months[int(month_str) - 1]

    # Output result in month day, year format
    print("The converted date is:", month_str, day_str+",", year_str)
    
main()
