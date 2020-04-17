distance = 150
time = 2
dmiles =  distance/1.6
dmeters = distance * 1000
time_seconds = time * 3600
speed_kmph = distance/time
speed_mph = dmiles/time
speed_mps = dmeters/time_seconds
print("The speed in kilometers per hour is: ",speed_kmph)
print("The speed in kilometers per hour is: ",speed_mph)
print("The speed in kilometers per hour is: ",speed_mps)
print(type(str(speed_kmph)))
