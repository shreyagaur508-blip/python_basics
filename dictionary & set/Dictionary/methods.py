student = {
    "name" : "Shreya",
    "Subjects" : {
        "Chem" : 98,
        "phy" :89,
        "coding" : 90
        },
    "College" : "Sharnabasva University"
    }

#keys() method
print(list(student.keys()))
print(len(student))

#values() method
print(list(student.values()))

#items() method
print(list(student.items()))

#get() method
print(student.get("name")) #noerror if key is not present   

#update() method
student.update({"name":"Shreya V"})
print(student)