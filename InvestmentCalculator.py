def calculateReturn(sAge:int=25, mInvestment:int=150, sYReturnRate:float=0.10, eAge:int=65):
    eYReturnRate = sYReturnRate
    mGains = 0
    tGains = 0
    tInvestment = 0
    tMoney = 0

    for i in range(sAge, eAge):
        for j in range(12):
            mGains = (tMoney+mInvestment)*(eYReturnRate/12)
            tGains += mGains
            tInvestment += mInvestment
            tMoney = tMoney+mInvestment+mGains
        eYReturnRate -= 0.001 # returns will decrease 0.01% per year

    print("From Age:", sAge, " To Age: ", eAge)
    print("Starting rate of yearly compound gains: %.2f" % (sYReturnRate*100), "Terminal rate of return: %.2f" % (eYReturnRate*100))
    print("Monthly Investment: $%.2f," % mInvestment, " Total Investment: $%.2f" % tInvestment)
    print("Total Gains: $%.2f" % tGains)
    print("Total Money $%.2f" % tMoney)

calculateReturn(25, 300)