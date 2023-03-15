# Start file for programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

import calendar

# Properties
daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

daysCount = 0
givenDay = 2
givenYear = 2023
givenMonth = 3

# Ask for the day of the week
print("Which day the of the week do you want to count?")
for d in range(0, 7):
    print(d, "{d}:", daysOfWeek[d])
print("Or 'exit' to quit")
givenDay = int(input())

# Ask for the year
givenYear = int(input("Enter year:"))

# Ask for the month
givenMonth = int(input("Enter month:"))

# print("Day:", givenDay)
# print("Month:", givenMonth)
# print("Year:", givenYear)

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
    

# print(month)
print("There are", daysCount, "of those days in the month and year specified.")