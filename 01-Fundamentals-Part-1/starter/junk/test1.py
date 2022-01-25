def addBonus(salary):

    for i in range (0,len(salary)):

        salary[i] += 500.0

    return salary

def salary_calc():

    employ_salary = [2400,2500,2600]

    addBonus(employ_salary)

    print("employ salary", employ_salary[0])

salary_calc()