#!/usr/bin/env python
class Person:
    def greeting_msg(self, first_name=None, last_name=None):
        if first_name is not None and last_name is not None:
            print('Hello ' + first_name + ' ' + last_name)
        elif first_name is not None and last_name is None:
            print('Hello ' + first_name)
        elif first_name is None and last_name is not None:
            print('Hello ' + first_name)
        else:
            print('Hello ')


# Create instance
obj = Person()
# Call the method
obj.greeting_msg()
# Call the method with a parameter
obj.greeting_msg('John')
obj.greeting_msg('John', 'Porter')
