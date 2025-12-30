from datetime import date
year = int(input("Enter birth year: "))
month = int(input("Enter birth month (1-12): "))
day = int(input("Enter birth day (1-31): "))
print("Entered date is:", year,month,day) 
today = date.today()
print("Today's date:", today)
birthdate = date(year,month,day)
age = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1
print("Your age is:", age)
