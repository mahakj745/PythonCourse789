score = 100
submitted_project = False
if score >= 90 and submitted_project:
    print ("A+")
elif score >= 90:
    print ("A")
elif score >= 80:
    print ("B")
elif score >= 60 or submitted_project:
    print ("C")        
else:
    print ("F")

