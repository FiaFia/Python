# coding=utf-8
"""
@author:FiaFia
@data:2018/7/6
@version:Python3.6
"""
from Tax import Tax


class Main():
    @staticmethod
    def salaryAfterTax(salary):
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

        if salary < tripleAverageSalary:
            totalInsurance = salary * (oldAgeRating + medicalRating + unemployRating + housingFundRating)
            housingFund = salary * housingFundRating
        else:
            totalInsurance = tripleAverageSalary * (
                oldAgeRating + medicalRating + unemployRating + housingFundRating)
            housingFund = tripleAverageSalary * housingFundRating   #公积金封顶
            #housingFund = salaryBeforeTax * housingFundRating     #如果公司给补超额公积金部分，则用这个计算

        # 纳税额
        oldPayment = salary - totalInsurance - oldThreshold
        oldTax = Tax.oldTaxRate(oldPayment)
        newPayment = salary - totalInsurance - newThreshold
        newTax = Tax.newTaxRate(newPayment)

        # 税后工资
        oldSalaryAfterTax = salary - totalInsurance - oldTax
        oldActualIncome = oldSalaryAfterTax + housingFund * 2
        newSalaryAfterTax = salary - totalInsurance - newTax
        newActualIncome = newSalaryAfterTax + housingFund * 2
        Gap = newActualIncome - oldActualIncome

        print('***Total insurance is %d and Housing fund is %d***' % (totalInsurance, housingFund))
        print('New salaryAfterTax is %d (tax is %d) and current salaryAfterTax is %d (tax is %d), receive more %d' % (newSalaryAfterTax,newTax,oldSalaryAfterTax, oldTax,  Gap))
        print('New income with housing fund is %d and current income with housing fund is %d ' % (newActualIncome, oldActualIncome))
        print('New Actual income Percentage is : %.2f %%' % float(newActualIncome * 100 / salary))
        print('Current Actual income Percentage is : %.2f %%' % float(oldActualIncome * 100 / salary))

        return oldSalaryAfterTax, newSalaryAfterTax


if __name__ == '__main__':
    salary = int(input('Please input your Salary before tax:'))
    Main.salaryAfterTax(salary)
