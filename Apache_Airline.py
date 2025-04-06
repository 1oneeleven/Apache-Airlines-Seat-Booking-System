# The following code is the Apache airlines seat booking system for FC723 Project assessment 5

print ("Apache Airlines")

print ("")

#create a class for the apache airplane booking system 
class ApacheAirlines:
    
    def __init__(self):                         #Set seat map for the Burak 757 airplane
        self.seat_map = [
    
                            [" 1A  ", " 1B ", "  1C ", " |X| ", "  1D  ", " 1E ", "  1F "],
                            [" 2A  ", " 2B ", "  2C ", " |X| ", "  2D  ", " 2E ", "  2F "],
                            [" 3A  ", " 3B ", "  3C ", " |X| ", "  3D  ", " 3E ", "  3F "],
                            [" 4A  ", " 4B ", "  4C ", " |X| ", "  4D  ", " 4E ", "  4F "],
                            [" 5A  ", " 5B ", "  5C ", " |X| ", "  5D  ", " 5E ", "  5F "],
                            
            ]
        
        for row_num in range(10, 70):                    #Fill in remaining rows between row 10 to row 75
            self.seat_map.append([
                f" {row_num}A ", f" {row_num}B ", f" {row_num}C ", "|X| ", f" {row_num}D", f"  {row_num}E ", f" {row_num}F"
                ])
        for row_num in range(71, 75):                    #Fill in remaining rows between row 10 to row 75
            self.seat_map.append([
                f"B-{row_num}A", f"B-{row_num}B", f"B-{row_num}C", "|X| ", f"B-{row_num}D", f"B-{row_num}E", f"B-{row_num}F"
                ])

#Adding the special last 5 rows 76 to 80 to include storage for the Burak 757 airplane
        self.seat_map.append(["F-76A", "F-76B", "F-76C", "|X| ", "  S  ", "  S  ", "  S  " ])
        self.seat_map.append(["F-77A", "F-77B", "F-77C", "|X| ", "  S  ", "  S  ", "  S  " ])
        self.seat_map.append(["F-78A", "F-78B", "F-78C", "|X| ", "  S  ", "  S  ", "  S  " ])
        self.seat_map.append(["F-79A", "F-79B", "F-79C", "|X| ", "F-79D", "F-79E", "F-79F"])
        self.seat_map.append(["F-80A", "F-80B", "F-80C", "|X| ", "F-80D", "F-80E", "F-80F"])
    
#_______________________________functions_______________________________


#function to display seat map 
def display_seats(seats):
    for row in seats:           #for loop to loop through every seat
        print(" ".join(row))    #print the seats in from the list in a row pattern


#check if the seat is available
def check_availability(seats, row, col):
    return seats[row][col] == "F"

#function to book seats
def book_seat(seats, row, col):
    
    if check_availability(seats, row, col):             #checks if the seat is availble 
        seats[row][col] = "R"
        print("Seat booked successfully!")
    else:
        print("Seat is already booked or unavailable.") #displays error if seat is unavailable

#function to free booked seat
def free_seat(seats, row, col):
    
    if seats[row][col] == "R":          
        seats[row][col] = "F"           #reassignes the seat from "R" to "F"
        print("Seat freed successfully!")
    else:                               #displays that the seat is not 
        print("Seat is not booked.")



#_______________________________main screen_______________________________
    
#Main menu function to display different options for the user
def main():
    
    #access the seat map from the instance
    airline = ApacheAirlines()
    seats = airline.seat_map
    while True:
        print ("\n Welcome to Apache Airlines Seat Booking System !")
        print ("1. Check availability of seat")
        print ("2. Book a seat")
        print ("3. Free a seat")
        print ("4. Show booking status")
        print ("5. Exit")
        print ("") 
        choice = input ("Enter your choice: ")
        
        
        #if statement to check seat availability after calling check_availability function
        if choice == "1":
            row, col = map (int, input('Enter row and column - please note that seats starting with "F -" are first clas seats and "B -.." are business class seats (e.g., 0 1): ').split())
            if check_availability(seats, row, col):
                print ("Seat is available.")
            else:
                print ("Seat is not available.")
                
        #call function to book a seat 
        elif choice == "2":
            row, col = map (int, input("Enter row and column to book: ").split())
            book_seat(seats, row, col)
            
        #call function to free a booked seat
        elif choice == "3":
            row, col = map (int, input("Enter row and column to free: ").split())
            free_seat(seats, row, col)
            
        #calls function to display the seat map with status
        elif choice == "4":
            display_seats(seats)
            
        #choice to exit the booking system
        elif choice == "5":
            print ("Exiting system... thank you for visiting Apache Airlines:)")
            
            break
        else:
            print ("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()