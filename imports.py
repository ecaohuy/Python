import calendar
# Print calendar of Apr 2023
print(calendar.month(2023, 4))
# Print today's date
#print(calendar.today())
#import calendar

# Check if 2020 is a leap year
for i in range(2020, 2050):
    if calendar.isleap(i):
        print(i, "is a leap year")
