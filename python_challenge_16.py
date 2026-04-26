score = 85
submitted_project = False

if score >= 90:
    print ("High Score")
else:
    print ("Low Score")   

if submitted_project:
    print ("Project is submitted")
else:
    print ("Project is not submitted")

    #inline if
grade = ("A" if score >= 90 else "F")
print (grade)

grade = ("A" if score >= 90 else "B" if score >= 80 else "F")
print (grade)
