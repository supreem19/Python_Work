# The map() function executes a specified function for each item in an iterable.
# The item is sent to the function as a parameter.
def myfunc(n):
    return len(n)


x = map(myfunc, ('apple', 'banana', 'cherry'))

# convert the map into a list, for readability:
print(list(x))


# Example 2
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# convert the map into a list, for readability:
print(list(x))