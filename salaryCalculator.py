# coding=utf-8
"""
@author:FiaFia
@data:2018/6/16
@version:Python3.6
"""


def oldTaxRate(base):
    '''
旧的税率表及速扣数
速扣数的公式（本档次税率-上档次税率）*上档次最高应纳税工资薪金的金额+上档次的速算扣除数
纳税额          税率    速扣数
<1500           3%      0
1500-4500       10%     105
4500-9000       20%     555
9000-35000      25%     1005
35000-55000     30%     2755
55000-80000     35%     5505
>80000          45%     13505
'''  
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

    #print('Tax of salary is : %d' % tax)

    return tax

def newTaxRate(base):
'''
新的税率表及速扣数
速扣数的公式（本档次税率-上档次税率）*上档次最高应纳税工资薪金的金额+上档次的速算扣除数
纳税额          税率    速扣数
<3000           3%      0
3000-12000      10%     210
12000-25000     20%     1410
25000-35000     25%     2660
35000-55000     30%     4410
55000-80000     35%     7160
>80000          45%     15160
'''    
    if base < 0:
        tax = 0
    elif base <= 3000:
        tax = base * 0.03
    elif base > 3000 and base <= 12000:
        tax = base * 0.1 - 210
    elif base > 12000 and base <= 25000:
        tax = base * 0.2 - 1410
    elif base > 25000 and base <= 35000:
        tax = base * 0.25 - 2660
    elif base > 35000 and base <= 55000:
        tax = base * 0.3 - 4410
    elif base > 55000 and base <= 80000:
        tax = base * 0.35 - 7160
    elif base > 80000:
        tax = base * 0.45 - 15160

    #print('Tax of salary is : %d' % tax)

    return tax

def salaryAfterTax(salaryBeforeTax):

    #旧个税免征点3500，新个税免征点5000,个人五险一金比率，养老8%，医疗2%，失业0.2%，公积金12%
    oldThreshold = 3500
    newThreshold = 5000
    oldAgeRating = 0.08
    medicalRating = 0.02
    unemployRating = 0.002
    housingFundRating = 0.12

    # 五险一金上限是社评三倍工资
    averageSalary = 8467   # 2016社平工资7706， 2017社平工资8467
    tripleAverageSalary = 3 * averageSalary

    if salaryBeforeTax < tripleAverageSalary:
        totalInsurance = salaryBeforeTax * (oldAgeRating + medicalRating + unemployRating + housingFundRating)
        housingFund = salaryBeforeTax * housingFundRating
    else:
        totalInsurance = tripleAverageSalary * (
            oldAgeRating + medicalRating + unemployRating + housingFundRating)
        housingFund = tripleAverageSalary * housingFundRating   #公积金封顶
        #housingFund = salaryBeforeTax * housingFundRating     #如果公司给补超额公积金部分，则用这个计算

    # 纳税额
    oldPayment = salaryBeforeTax - totalInsurance - oldThreshold
    oldTax = oldTaxRate(oldPayment)
    newPayment = salaryBeforeTax - totalInsurance - newThreshold
    newTax = newTaxRate(newPayment)

    # 税后工资
    oldSalaryAfterTax = salaryBeforeTax - totalInsurance - oldTax
    oldActualIncome = oldSalaryAfterTax + housingFund * 2
    newSalaryAfterTax = salaryBeforeTax - totalInsurance - newTax
    newActualIncome = newSalaryAfterTax + housingFund * 2
    Gap = newActualIncome - oldActualIncome

    print('Total insurance is %d and Housing fund is %d' % (totalInsurance, housingFund))
    print('New tax is %d and Previous tax is %d, could save more %d' % (newTax, oldTax, Gap))
    print('New net income is %d and Previous net income is %d' % (newSalaryAfterTax, oldSalaryAfterTax))
    print('New income with housing fund is %d and Previous income with housing fund is %d ' % (newActualIncome, oldActualIncome))
    print('New Actual income Percent is : %.2f %%' % float(newActualIncome * 100 / salaryBeforeTax))
    print('Previous Actual income Percent is : %.2f %%' % float(oldActualIncome * 100 / salaryBeforeTax))

    return salaryAfterTax


if __name__ == '__main__':
    salary = int(input('Please input your Salary before tax:'))
    salaryAfterTax(salary)
