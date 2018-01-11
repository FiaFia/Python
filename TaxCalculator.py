salary_before_tax = int(input('Please input your Salary before tax:'))
threshold = 3500  #免征点

#个人五险一金比率，养老8%，医疗2%，失业0.2%，公积金12%
old_age_rating = 0.08
medical_rating = 0.02
unemployment_rating = 0.002
housing_fund_rating = 0.12

# 2016年社平工资7706，五险一金的上限是社评三倍工资为基数
average_salary = 7706
triple_average_salary = 3 * average_salary

if salary_before_tax < triple_average_salary:
    total_insurance = salary_before_tax * (old_age_rating + medical_rating + unemployment_rating + housing_fund_rating)
else:
    total_insurance = triple_average_salary * (old_age_rating + medical_rating + unemployment_rating + housing_fund_rating)

# 纳税额
payment = salary_before_tax - total_insurance - threshold

if payment <= 1500:
    tax = payment * 0.03
elif payment > 1500 and payment <= 4500:
    tax = payment * 0.1 - 105
elif payment > 4500 and payment <= 9000:
    tax = payment * 0.2 - 555
elif payment > 9000 and payment <= 35000:
    tax = payment * 0.25 - 1005
elif payment > 35000 and payment <= 55000:
    tax = payment * 0.3 - 2755
elif payment > 55000 and payment <= 80000:
    tax = payment * 0.35 - 5505
elif payment > 80000:
    tax = payment * 0.45 - 13505
    
# 税后工资
salary_after_tax = salary_before_tax - total_insurance - tax

print('Salary after tax is %d' % salary_after_tax)
