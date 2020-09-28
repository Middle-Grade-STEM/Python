"""
Middle Grade Stem - Python
Assignment 4.7

INSTRUCTIONS:
Given a list:
example_list = ["Hello", "guys", "what", "is", "going", "on?"]
Print out the result of doing example_list.pop()
Remove the word "what" in the list, and then print it out.
Print out the index of the word "is"

EXAMPLE OUTPUT:
on?
['Hello', 'guys', 'is', 'going']
2

"""

example_list = ["Hello", "guys", "what", "is", "going", "on?"]
print(example_list.pop())
example_list.remove("what")
print(example_list)
print(example_list.index("is"))
