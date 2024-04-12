
def getBondPrice_Z(face, couponRate, times, yc):
    # Calculate the coupon payment
    coupon_payment = face * couponRate
    
    # Initialize the bond price
    bond_price = 0
    
    # Iterate over each time period and corresponding yield curve rate
    for t, y in zip(times, yc):
        # Cash flow is the coupon payment unless it's the last time period
        cash_flow = coupon_payment if t < times[-1] else coupon_payment + face
        
        # Present value of cash flow, discounted by the yield curve rate for time t
        pv = cash_flow / (1 + y) ** t
        
        # Add the present value to the bond price
        bond_price += pv
        
    return bond_price
