#Python Mini Project
#Project Title: Employee Management & Payroll System (Console Based)

#mod-1:Employee Registration
def emp_det():
    emp_id = input("Enter employee ID:\n")
    name = input("Enter Name of the Employee:\n")
    age = int(input("Enter the age of the employee:\n"))
    dept = input("Enter the department:\n")
    sal = float(input("Enter the basic salary of the employee:\n"))
    if age >= 18 and sal > 0:
        print("Employee registered successfully!!")
    else:
        print("Error Message")
        return
    #mod-2:Attendance Management
    n = 5
    lst = []
    print("Enter the 5 days attendance (P or A):")
    for i in range(n):
        lst.append(input().upper())
    count = 0
    for i in lst:
        if i == "P":
            count += 1
    if count >= 4:
        print("Attendance Status: Regular")
    elif count == 3:
        print("Attendance Status: Warning")
    else:
        print("Attendance Status: Irregular")
    #mod-3:Salary Calculation
    def cal_sal(basic_salary, count):
        hra = basic_salary * 0.2
        da = basic_salary * 0.1
        pf = basic_salary * 0.12
        if count < 3:
            net_sal = basic_salary - pf
        else:
            net_sal = basic_salary + hra + da - pf
        print("Net Salary:", net_sal)
    cal_sal(sal, count)
    #mod-4:Performance Evaluation
    total=0
    for i in range(1,4):
        rate=int(input("Enter the performance rating (1-5):"))
        total+=rate
    avg=total/3
    print("Average Rating:",avg)
    if avg>=4:
        print("Excellent Performance!")
    elif avg>=3:
        print("Good Performance!")
    else:
        print("Needs Improvement")
    #mod-5:Login Authentication
    def login():
        username="dd_admin"
        password="dd@123"
        user=input("Enter the username:")
        pswd=input("Enter the password:")
        if user==username and pswd==password:
            print("Login Successful!!")
        else:
            print("Oops!! Access Denied!")
    login()
emp_det()
