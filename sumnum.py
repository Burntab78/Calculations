# Author: Bryan Burnett
# Date: 11/24/23
# About: this is a progream to determine cost based on set hourly time use.

# import libraries
import math

# define what to calculate
def calculateTotalFee(hours, minutes):
    return hours+":"+minutes

# get user inputs
hours = int(input("how many hours?: \n"))
minutes = int(input("how many minutes?: \n"))

# fee math
hfee = 1 
mfee = 1

# price codes
fee1 = int(hours * hfee)
fee2 = int(minutes * mfee)

# create printable conditions.
if fee1 == 0 and fee2 <= 15 :
    print ('0')
    print ("no charge")
elif fee1 >= 0 and fee1 < 2 and fee2 >= 15:
    print ('your charge is $1')
elif fee1 >= 2 and fee1 < 5:
    print ('your charge is $5')
elif fee1 >= 5:
    print ('your charge is $', fee1+10)
