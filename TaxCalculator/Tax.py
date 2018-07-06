# coding=utf-8
"""
@author:FiaFia
@data:2018/6/16
@version:Python3.6
"""


class Tax():
    @staticmethod
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

        return tax

    @staticmethod
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

        return tax
