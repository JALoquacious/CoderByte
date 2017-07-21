"""Using the Python language, have the function LetterCountI(str) take the str parameter
being passed and return the first word with the greatest number of repeated letters. For
example: "Today, is the greatest day ever!" should return greatest because it has 2 e's
(and 2 t's) and it comes before ever which also has 2 e's. If there are no words with
repeating letters return -1. Words will be separated by spaces. """


t1 = "Today is the greatest day ever!" #Output = "greatest"
t2 = "Hello apple pie" #Output = "Hello"
t3 = "No words" #Output = -1

def LetterCount(string):
    dct = {}
    count = 0
    string = [word.lower() for word in string.split()]
    for word in string:
        for char in range(len(word)):
            if word[char] in word[char+1:]:
                count+=1
                dct[word] = count
        count = 0
    print(dct) # DEBUG
    if dct == {}: return -1
    else: return max(dct, key=lambda k: dct[k])
    
print(LetterCount(t1))
print(LetterCount(t2))
print(LetterCount(t3))
