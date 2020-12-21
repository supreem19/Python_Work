# Python program to count number of characters(repetition count of character ) in a string.
# str = "elephant"
str = "geeksforgeeks"

mydic = dict()
for i in str:
    if i in mydic.keys():
        mydic[i] = int(mydic.get(i)) + 1
    else:
        mydic[i] = 1
print(mydic)
