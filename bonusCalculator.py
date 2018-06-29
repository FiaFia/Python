# coding=utf-8
"""
@author:FiaFia
@data:2018/3/7
@version:Python3.6
"""

def bonusTaxRate(bonus,thirteen_month_salary):

    total = bonus + thirteen_month_salary
    base = total/12

    if base < 0:
        bonus_tax = 0
    if base <= 1500:
        bonus_tax = total * 0.03
    elif base > 1500 and base <= 4500:
        bonus_tax = total * 0.1 - 105
    elif base > 4500 and base <= 9000:
        bonus_tax = total * 0.2 - 555
    elif base > 9000 and base <= 35000:
        bonus_tax = total * 0.25 - 1005
    elif base > 35000 and base <= 55000:
        bonus_tax = total * 0.3 - 2755
    elif base > 55000 and base <= 80000:
        bonus_tax = total * 0.35 - 5505
    elif base > 80000:
        bonus_tax = total * 0.45 - 13505

    print('Bonus tax payable is : %d' % bonus_tax)

    return bonus_tax


def bonusAfterTax(bonus, thirteen_month_salary):
    #纳税额
    tax = bonusTaxRate(bonus,thirteen_month_salary)

    #税后bonus
    bonus_after_tax = bonus + thirteen_month_salary - tax

    print('Bonus after tax is : %d' % bonus_after_tax)
    print('bonus_after_tax percentage is : %.2f %%' % float(bonus_after_tax * 100 / (bonus + thirteen_month_salary)))
    print('                 ')

    return bonus_after_tax



def newBonusTaxRate(bonus, thirteen_month_salary):
    '''
    假设税法改成把速扣数也相应扩大12倍，计算应扣税
    '''
    total = bonus + thirteen_month_salary
    base = total / 12

    # 速扣数相应增大12倍
    if base < 0:
        bonus_tax = 0
    if base <= 1500:
        bonus_tax = total * 0.03
    elif base > 1500 and base <= 4500:
        bonus_tax = total * 0.1 - 105 * 12
    elif base > 4500 and base <= 9000:
        bonus_tax = total * 0.2 - 555 * 12
    elif base > 9000 and base <= 35000:
        bonus_tax = total * 0.25 - 1005 * 12
    elif base > 35000 and base <= 55000:
        bonus_tax = total * 0.3 - 2755 * 12
    elif base > 55000 and base <= 80000:
        bonus_tax = total * 0.35 - 5505 * 12
    elif base > 80000:
        bonus_tax = total * 0.45 - 13505 * 12

    print('New bonus tax payable is : %d' % bonus_tax)

    return bonus_tax


def newBonusAfterTax(bonus, thirteen_month_salary):
    '''
    假设速扣数相应扩大12倍后，计算应扣税
    '''
    total = bonus + thirteen_month_salary

    # 纳税额
    new_bonus_tax = newBonusTaxRate(bonus,thirteen_month_salary)

    # 税后bonus
    bonus_after_tax = total - new_bonus_tax

    print('New Bonus after tax is : %d' % bonus_after_tax)
    print('New bonus_after_tax percentage is : %.2f %%' % float(bonus_after_tax * 100 / total))
    print('                ')

    return bonus_after_tax

if __name__ == '__main__':
    bonus_before_tax = int(input('Please input your Bonus before tax:'))
    thirteen_month_salary = int(input('Please input your 13rd Salary before tax:'))
    bonusAfterTax(bonus_before_tax, thirteen_month_salary)
    newBonusAfterTax(bonus_before_tax, thirteen_month_salary)
