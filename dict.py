def dictionary(student1):
    print("Name = ",student1["Name"])
    print("Phone No. = ",student1["Phone No."])
    print(student1.items())
    print(student1.keys())
    print(student1.values())

if "__main__":
    student1={
        "Name":"Rahul",
        "Branch":"AI&DS",
        "Location":"Jaipur",
        "Phone No.":"12345xxxxx"
    }
    input("Press enter to get Student details")
    dictionary(student1)
    student1["Class"]="12th"
    print(student1["Class"])
    student1["Name"]="Rehana"
    print(student1)
    
