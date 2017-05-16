"""Using the Python language, have the function AdditivePersistence(num) take
the num parameter being passed which will always be a positive integer and
return its additive persistence which is the number of times you must add the
digits in num until you reach a single digit. For example: if num is 2718 then
your program should return 2 because 2 + 7 + 1 + 8 = 18 and 1 + 8 = 9 and you
stop at 9."""

def split(num):
    return [int(n) for n in str(num)]

def add_pers(num):
    counter = 0
    while len(split(num)) > 1:
        num = sum(split(num))
        counter += 1
    return counter

print(add_pers(999999999999999999999)) #0
print(add_pers(19)) #2
print(add_pers(2718)) #2
print(add_pers(10)) #1
print(add_pers(4)) #0
