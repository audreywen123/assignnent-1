
def getBondPrice_E(face, couponRate, m, yc):
    # Calculate the coupon payment
    coupon_payment = face * couponRate
    
    # Initialize the bond price
    bond_price = 0
    
    # Calculate the present value of each cash flow considering the yield curve
    for t, y in enumerate(yc, start=1):
        # Calculate the cash flow (coupon payment for all periods, plus face value at maturity)
        cash_flow = coupon_payment if t < m else coupon_payment + face
        
        # Calculate the present value of the cash flow
        pv = cash_flow / (1 + y) ** t
        
        # Add the present value to the bond price
        bond_price += pv
        
    return bond_price
