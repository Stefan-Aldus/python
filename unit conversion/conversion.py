from time import sleep


def kmtomile():
    # Asks the user for the distance in KM
    distanceinkm = float(input("Enter the distance in kilometers: "))
    # Conversion
    distanceinmile = distanceinkm * 1.609344

    # Prints the result
    print("The distance in miles when the distance in km is %s is %s miles!" %
          (distanceinkm, float(distanceinmile)))
    sleep(2)


def milestofeet():
    # Asks the user for distance in Miles
    distanceinmile = float(input("Enter the distance in miles: "))
    # Conversion
    distanceinfeet = 5280 * distanceinmile

    # Prints the result
    print("The distance in feet when the distance in miles is %s is %s feet!" %
          (distanceinmile, float(distanceinfeet)))
    sleep(2)


def feettoinches():
    # Asks the user for the distance in Feet
    distanceinfeet = float(input("Enter the distance in feet: "))
    # Conversion
    dinstanceininches = distanceinfeet * 12

    # Prints the result
    print("The distance in inches when the distance in feet is %s is %s inches!" % (
        distanceinfeet, float(dinstanceininches)))
    sleep(2)


# Sets a counter to be used in the while loop
counter = 0

# While loop that keeps running until the program exits
while True:
    # Explains what the converter can do and then asks the user what they want to convert
    print("This converter converts the following: \n KM To Miles: Enter \"KmToMile\" \n Miles to Feet: Enter \"MilesToFeet\" \n Feet To Inches: Enter \"FeetToInches\" \n To exit the program enter \"Exit\"")
    conversion = input("Enter your choice: ")

    """ 
    Checks if the user entered a valid input, if not, add 1 to the counter to prevent too many bad attempts, if the counter reaches 10 the
    program will exit, if the user input is valid, calls the fumctions defined at the beginnign
    """
    if conversion.lower() == "kmtomile":
        kmtomile()
    elif conversion.lower() == "milestofeet":
        milestofeet()
    elif conversion.lower() == "feettoinches":
        feettoinches()
    elif conversion.lower() == "exit":
        quit("The program has been stopped by the user.")
    elif counter != 10:
        print("Invalid conversion entered")
        counter += 1
    else:``
        print("Too many wrong inputs entered by user, program is being stopped")
        quit("The program has been stopped with error code: 2")
