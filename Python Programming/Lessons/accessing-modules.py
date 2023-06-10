import calendar
import sys

locations = sys.path

for l in locations:
    print(l)


ld = calendar.leapdays(1990, 2023)
print("\n", ld)

ly = calendar.isleap(1990)
print(ly)
