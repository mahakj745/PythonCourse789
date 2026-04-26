#convert the full country names into 2- letter abbreviations
#match case

country = "Egypt"
if country == "United States":
    print ("US")
elif country == "India":
    print ("IN")
elif country == "Egypt":
    print ("EG")
elif country == "Germany":
    print ("DE")
else:
    print ("Unknown Country")


match country:
    case "United States":
        print ("US")
    case "India":
         print ("IN")
    case "Egypt":
        print ("EG")
    case "Germany":
        print ("DE")
    case _:
        print ("Unknown Country")