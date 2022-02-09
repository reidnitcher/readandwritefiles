import csv



employee = open('EmployeePay.csv', 'r')

employee_file = csv.reader(employee, delimiter = ',')

next(employee_file)


for record in employee_file:
    print('First Name:', record[1])
    print('Last Name:' , record[2])
    print("Salary", record[3])
    bonus = record[3] * record[4]
    print("Bonus", bonus)
    total = record[3] + bonus
    print('Total pay', total)



    

