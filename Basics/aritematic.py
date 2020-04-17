# Write your code here
num = int(input("Number of days "))
years = num // 365
remain = num - (years*365)
weeks = remain // 7
remain = remain - (weeks*7)
days = remain 
print ("Years: ", years)
print ("Weeks: ", weeks)
print ("Days: ", days)
