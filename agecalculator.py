#IMPORTING DATE MODULES 
from datetime import date
                                       #ENTER THE YEAR OF THE USER WANT
year = int(input("Enter birth year: "))
                                       #ENTER THE MONTH OF USER WANT IN BETWEEN THE 1 TO 12 ONLY
month = int(input("Enter birth month (1-12): "))
                                       #ENTER THE DAY OF USER WANT IN BETWEEN THE 1 TO 31 ONLY
day = int(input("Enter birth day (1-31): "))
                                       #THE USER ENTERED DATE OF BIRTH PERINT IN THE CORRECT FORM
print("Entered date is:", year,month,day) 
                                       #BY DEFAULT THIS STATEMENT TAKEN THE PRESENT(TODAY) DATE
today = date.today()
                                       #PRINTS THE TODAY DATE
print("Today's date:", today)

birthdate = date(year,month,day)           #THIS IS THE USER ENTERES DATE CHANGE INTO THE DATE FORMATE
age = today.year - birthdate.year           #THE AGE IS CALCULATE BY DIFFERENCE BETWEEN THE YEAR
if (today.month, today.day) < (birthdate.month, birthdate.day):    #THE MONTH AND DAY ALSO CALCULATE THE DIFFERENCE 
    age -= 1                                   
print("Your age is:", age)                      #IT WILL PRINT THE AGE OF THE USER

