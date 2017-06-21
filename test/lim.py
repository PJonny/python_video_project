from decimal import *
iValue = 10
sum_n = []
getcontext().prec = 101
for i in xrange(50):
    sum_n.append(((1+Decimal(1)/Decimal(iValue))**2 - 1**2)/(Decimal(1)/Decimal(iValue)))
    iValue *= 10
for i in xrange(50):
    print sum_n[i]
