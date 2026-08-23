#Practice 8
roll_numbers = {101,102,103,104,105,106,107,101,102}
print(roll_numbers)

employee = [
      (101, "Sakshi" , 200000),
      (102, "Akanksha" , 150000),
      (103, "Sanika" , 120000)

]
id = int(input("Enter Employee ID : "))

for emp in employee:
    if emp[0] == id:
        print(emp)
        break
else:
    print("Employee not found")   




