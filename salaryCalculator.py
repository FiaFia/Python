def taxRate(base):
    if base < 0:
        tax = 0
    elif base <= 1500:
        tax = base * 0.03
    elif base > 1500 and base <= 4500:
        tax = base * 0.1 - 105
    elif base > 4500 and base <= 9000:
        tax = base * 0.2 - 555
    elif base > 9000 and base <= 35000:
        tax = base * 0.25 - 1005
    elif base > 35000 and base <= 55000:
        tax = base * 0.3 - 2755
    elif base > 55000 and base <= 80000:
        tax = base * 0.35 - 5505
    elif base > 80000:
        tax = base * 0.45 - 13505

    print('Tax of salary is : %d' % tax)

    return tax

def salaryAfterTax(salary_before_tax):

    #免征点3500 ,个人五险一金比率，养老8%，医疗2%，失业0.2%，公积金12%
    threshold = 3500
    old_age_rating = 0.08
    medical_rating = 0.02
    unemployment_rating = 0.002
    housing_fund_rating = 0.12

    # 2016年社平工资7706，五险一金上限是社评三倍工资
    average_salary = 7706
    triple_average_salary = 3 * average_salary

    if salary_before_tax < triple_average_salary:
        total_insurance = salary_before_tax * (old_age_rating + medical_rating + unemployment_rating + housing_fund_rating)
        housing_fund = salary_before_tax * housing_fund_rating
    else:
        total_insurance = triple_average_salary * (
            old_age_rating + medical_rating + unemployment_rating + housing_fund_rating)
        housing_fund = triple_average_salary * housing_fund_rating   #公积金封顶
        #housing_fund = salary_before_tax * housing_fund_rating     #公司给补超额公积金部分

    # 纳税额
    payment = salary_before_tax - total_insurance - threshold
    tax = taxRate(payment)

    # 税后工资
    salary_after_tax = salary_before_tax - total_insurance - tax
    actual_income = salary_after_tax + housing_fund * 2

    print('Housing Fund is : %d' % housing_fund)
    print('Total insurance is : %d ' % total_insurance)
    print('Tax of salary is : %d' % tax)
    print('Salary after tax is : %d' % salary_after_tax)
    print('Actual income including housing fund is : %d ' % actual_income)
    print('Actual income Percent is : %.2f %%' % float(actual_income*100/salary_before_tax))

    return salary_after_tax

if __name__ == '__main__':
    salary = int(input('Please input your Salary before tax:'))
    salaryAfterTax(salary)



