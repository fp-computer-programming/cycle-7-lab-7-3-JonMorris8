"""
Create a Python file named lab_7-3.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Copy your lab 7-1 code into the file
Add 4 test cases to the end of the file, with comments
Ensure your lab runs accurately

"""
# author Jon Morris

def greeting():

    #this finction prints "hello world!" on a line

    example:any
    greeting() #Output: hello world!

    print("Hello World!")
    return greeting.__doc__
greeting()



#test case 1, call the function and verify the output is "hello world!"
greeting() #output hello world!

#test case 2, call the function again to demonstrate the reusability of the function
greeting() #output, hello world!

#test case 3, assign the docstring to a variable and print it seperatly
docstring_var = greeting.__doc__
print(docstring_var) #output, this function prints "hello world!" on the line and returns the docstring

#test case 4, call the function wihtout printing to observe the behavior of not using returned docstring
greeting()