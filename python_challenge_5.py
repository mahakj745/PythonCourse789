#whitespace cleanup

text = " Engineering"
print (len(text))
print (len(text.strip()))
number_of_spaces = len (text) - len (text.strip())
is_clean = len(text) == len(text.strip())
print ("number_of_spaces:", number_of_spaces)
print ("Is my data clean?", is_clean)

