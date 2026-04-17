# "968-Maria, ( D@t@ Engineer ) ;; 27 y  "
# name: maria | role: data engineer | age: 27

row = "968-Maria, ( D@t@ Engineer ) ;; 27 y  "


name, role, age = row.replace("@", "a").replace("(", "|").replace(")", "|")\
            .replace(";","").replace("y","").replace(",","")\
            .lower().strip().split("-")[1]\
            .split("|")

name = name.strip()
age = age.strip()
role = role.strip()

print(f"name: {name} | role: {role} | age: {age}")