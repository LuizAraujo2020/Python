# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar


def validateInputDayOfWeek(input):
    if type(input) == int:
        if input >= 0 and input <= 6:
            return True
    return False

def validateInputMonth(input):
    if type(input) == int:
        if input > 0 and input <= 12:
            return True
    return False

def validateInputYear(input):
    if type(input) == int and input > 0:
        return True
    return False

temp = ""
daysCount = 0
givenDay = 2
givenYear = 2023
givenMonth = 3

while temp !=  "exit":
    # Properties
    daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


    # Ask for the day of the week
    print("Which day the of the week do you want to count?")
    for d in range(0, 7):
        print(d, ":", daysOfWeek[d])
    temp = input("Or 'exit' to quit: ")

    if temp !=  "exit":
        try:
            givenDay = int(temp)
        except ValueError as e:
            print("Sorry, you entered an invalid option for the day of week. Try again.")
            continue
        
        # Ask for the year
        givenYear = int(input("Enter year:"))

        # Ask for the month
        givenMonth = int(input("Enter month:"))

        # print("Day:", givenDay)
        # print("Month:", givenMonth)
        # print("Year:", givenYear)

        if validateInputDayOfWeek(givenDay) == False:
            print("Sorry, you entered an invalid option for the day of week. Try again.")
            
        elif validateInputMonth(givenMonth) == False:
            print("Sorry, you entered an invalid input for Month (1~12). Try again.")
            
        elif validateInputYear(givenYear) == False:
            print("Sorry, you entered an invalid input for the year. Try again.")

        else:
            #  Count the number of days in the given month-year
            # date = date(givenYear, givenMonth, givenDay)
            month = calendar.monthcalendar(givenYear, givenMonth)
            # for w in range(0, len(month)):
            #     for d in range(1,7):
            #         if d == 2:
            #             daysCount += 1



            for w in range(0, len(month)):
                week = month[w]
                
                match givenDay:
                    case 0: 
                        if week[calendar.MONDAY] != 0:
                            daysCount += 1
                    case 1: 
                        if week[calendar.TUESDAY] != 0:
                            daysCount += 1
                    case 2: 
                        if week[calendar.WEDNESDAY] != 0:
                            daysCount += 1
                    case 3: 
                        if week[calendar.THURSDAY] != 0:
                            daysCount += 1
                    case 4:
                        if week[calendar.FRIDAY] != 0:
                            daysCount += 1
                    case 5: 
                        if week[calendar.SATURDAY] != 0:
                            daysCount += 1
                    case 6:  
                        if week[calendar.SUNDAY] != 0:
                            daysCount += 1
                    # case _:
                    #     print("Sorry, you entered an invalid input for the Day of Week. Try again.")
                    #     daysCount = -1

            if daysCount > 0:
                # print(month)
                print("There are", daysCount, "of those days in the month and year specified.")


