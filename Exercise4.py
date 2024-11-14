print("Enter your salary")
salary = float(input())

if salary <15000:
    salary = salary * 0/100
    print("Your iva is",salary) 
elif salary >= 15000 and salary<30000:
    salary = salary *15/100
    print("Your iva is",salary)
elif salary >= 30000 and salary <60000:
    salary = salary * 21/100
    print("Your iva is",salary)
else :
    print("Iva not defined")