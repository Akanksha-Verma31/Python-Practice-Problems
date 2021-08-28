# Write a Python statement that calculates and prints the number of 	seconds in 7 hours, 21 minutes and 37 seconds.
hours = 7
mins = 21
secs = 37

# to convert all of them into seconds
converted_hours = hours * 3600
converted_mins = mins * 60
converted_sec = secs

# to print the converted values
print("7 Hours is equal to {} seconds" .format(converted_hours) )
print("21 Minutes is equal to {} seconds" .format(converted_mins) )
print("37 Seconds is equal to {} seconds" .format(converted_sec) )

# total time in seconds
print("Total time in seconds is ::", converted_hours+converted_mins+converted_sec, "sec")
