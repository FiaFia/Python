pre_salary = input('Please input your salary before raise : ')
pre_salary = float(pre_salary)

pre_salary_months = input('Please input the months of salary before raise: ')
pre_salary_months = int(pre_salary_months)

current_salary = input('Please input your current salary : ')
current_salary = float(current_salary)

current_salary_months = 12 - pre_salary_months
current_salary_months = int(current_salary_months)

work_years = input('Please input your working years N ( N + n ): ')
work_years = float(work_years)

n = input('Please input n number( N + n): ')
n = float(n)

bonus = input('Please input your Bonus before tax: ')
bonus = float(bonus)

left_vacation = input('Please input your left vacation: ')
left_vacation = float(left_vacation)

unpaid_days = input('Please input unpaid days in this month:')
unpaid_days = float(unpaid_days)

insurance = input('Please input the five insurance and housing fund need to pay: ')
insurance = float(insurance)

daily_salary = current_salary / 21.75

# 赔偿金按N+n算， N乘以去年所有收入/12 的平均工资，n乘以当月税前工资,加上年假折现，减去多发工资(默认当月离开时发全工资，多发部分从赔偿金里扣 )
severance_before_tax = ((
                        pre_salary * pre_salary_months + current_salary * current_salary_months + bonus) / 12) * work_years \
                       + current_salary_months * n + (left_vacation - unpaid_days) * daily_salary

# 2016北京社平年工资是92472

average_salary = 92472
triple_average_salary = 3 * average_salary

# 个税免征点
threshold = 3500

# 若赔偿金没超社平三倍，不扣税，否则扣个税
# 经济补偿金个税 ={[ (经济补偿金总数 - 当地上年职工平均工资3倍 - 实际缴纳的社保和公积金)/本单位的工作年限 - 个税免征额3500] *适用税率 - 速算扣除额} * 本单位的实际工作年限

if severance_before_tax < triple_average_salary:
    final_severance = severance_before_tax
else:
    payment = (severance_before_tax - triple_average_salary - insurance) / work_years

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

    total_tax = tax * work_years
    final_severance = severance_before_tax - total_tax

# print('Severance which before tax is %.2f' % severance_before_tax)
print('Severance before tax is %d' % severance_before_tax)
print('Monthly severance is %d' % payment)
print('Total tax is %d' % total_tax)
print('Final Severance is %d' % final_severance)
