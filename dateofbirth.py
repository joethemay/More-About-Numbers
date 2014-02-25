from datetime import date as dat

def getYear():
    year = input("Please enter the year in which you were born. ")
    year = int (year)
    return year
    
def age(year0fBirth):
    today = dat.today()
    thisYear = today.year
    age = thisYear - year0fBirth
    return age
    
year = getYear()
print("You will be %s years old this year on your birthday" %age(year))
