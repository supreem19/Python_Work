def decorator_test(func):
    def addon_func():
        print('We are about to test number')
        func()
        print('We have tested number')

    return addon_func


@decorator_test
def check_num(num):
    # num = 5
    if num % 2 == 0:
        print('Even')
    else:
        print('Odd')


# f1 = check_num
# del check_num
# f1()

# Using decorator way to get control
check_num(5)

# Normal way to execute a function
#check_num()
#a = decorator_test(check_num)
#a()
