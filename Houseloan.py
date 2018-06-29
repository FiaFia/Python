# coding=utf-8
"""
@author:FiaFia
@data:2018/3/16
@version:Python3.6
"""


def monthlyPayment(principal, annual_interest_rate, year_duration):
    """
    计算每个月房贷中还的利息和本金比
    """
    monthly_rate = annual_interest_rate / (12 * 100)   # convert 4.9 to 0.049 and  monthly interest rate
    month_amounts =  year_duration * 12

    # 每月月供
    monthly_payment = (principal * monthly_rate * (1 + monthly_rate) ** month_amounts) / (
    (1 + monthly_rate) ** month_amounts - 1)
    #总利息
    total_interest_payable = monthly_payment * month_amounts - principal
    print('-----------------------------------')
    print ('Total interest payable is %.2f ' % total_interest_payable)

    for i in range(1, month_amounts + 1):
        #每月应还利息
        monthly_interest_payable = principal * monthly_rate * ((1 + monthly_rate) ** month_amounts - (1 + monthly_rate) ** (i - 1 ))/ ((1 + monthly_rate) ** month_amounts -1)
        #每月应还本金
        monthly_principal_payable = principal * monthly_rate * (1 + monthly_rate) ** (i - 1)/ ((1 + monthly_rate) ** month_amounts -1)
        #每月利息占比
        monthly_interest_percentage = monthly_interest_payable * 100 / monthly_payment

        print('-----------------------------------')
        print('%dth monthly payment is : %.2f (Interest: %.2f and Principal: %.2f)' % (i, monthly_payment,monthly_interest_payable,monthly_principal_payable))
        print('%dth month interest percentage is %.2f %%' % (i,monthly_interest_percentage))

    return


if __name__ == '__main__':
    principal = int(input('Please input your loan amounts:'))
    annual_interest_rate = float(input('Please input Annual Loan Interest Rate:(such as input 4.9,it means 4.9%)'))
    year_duration = int(input('Please input Loan Year Duration:'))
    monthlyPayment(principal, annual_interest_rate, year_duration)

