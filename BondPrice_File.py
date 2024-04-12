
def getBondPrice(y, face, couponRate, m, ppy=1):
    couponpay = face * couponRate / ppy
    bp = 0
    
    for i in range(1, m * ppy +1):
        bp += couponpay / ((1 +y /ppy) ** i)
   
    bp += face / ((1+y / ppy) ** (m * ppy))
    return bp
