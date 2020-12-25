numbers = [19, 2, 8, 9, 6, 7, 4, 5]
#smallest_num = 9999
smallest_num = numbers[0]
for i in numbers:
    if i < smallest_num:
        smallest_num = i
print(smallest_num)
