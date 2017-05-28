"""
Using the Python language, have the function CountingMinutes(str) take the str
parameter being passed which will be two times (each properly formatted with a
colon and am or pm) separated by a hyphen and return the total number of minutes
between the two times. The time will be in a 12 hour clock format. For example:
if str is 9:00am-10:00am then the output should be 60. If str is 1:00pm-11:00am
the output should be 1320.
"""

def CountingMinutes(string): 
    array = string.replace("-"," ").replace(":"," ").split()
    for i in range(len(array)):
        if "pm" in array[i]:
            array[i-1] = (int(array[i-1])+12) * 60
        elif "am" in array[i]:
            if array[i-1] == "12":
                array[i-1] = 0
            else: array[i-1] = int(array[i-1]) * 60
        array[i] = int(array[i][:2])
    time1, time2 = sum(array[0:2]), sum(array[2:4])
    if time1 < time2:
        return time2 - time1
    else: return (time2 - time1) + 1440

print(CountingMinutes("12:30pm-12:00am")) # 690
print(CountingMinutes("1:23am-1:08am")) # 1425
print(CountingMinutes("9:00am-10:00am")) # 60
print(CountingMinutes("1:00pm-1:00am")) # 1320
