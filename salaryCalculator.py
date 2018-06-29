# coding=utf-8
"""
@author:FiaFia
@data:2018/6/16
@version:Python3.6
"""


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

    # 2016年社平工资7706，五险一金上限是社评三倍工资
    averageSalary = 7706   # 2016社评工资7706， 2017社评工资8467
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
    oldTax = taxRate(oldPayment)
    newPayment = salaryBeforeTax - totalInsurance - newThreshold
    newTax = taxRate(newPayment)

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
