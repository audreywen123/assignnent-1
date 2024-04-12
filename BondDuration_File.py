def getBondDuration(y, face, couponRate, m, ppy=1):
    # Initialize the bond duration variable
    bondDuration = 0
    
    # Calculate the coupon payment
    coupon = face * couponRate / ppy
    
    # Calculate the present value of each cash flow and its time-weighted value
    for t in range(1, m * ppy + 1):
        # Present value of the cash flow at time t
        pv = coupon / ((1 + y/ppy) ** t)
        # Time-weighted present value
        weighted_pv = pv * t
        # Add to the bond duration
        bondDuration += weighted_pv
    
    # Add the present value of the face value at maturity
    pv_face = face / ((1 + y/ppy) ** (m * ppy))
    weighted_pv_face = pv_face * m * ppy
    bondDuration += weighted_pv_face
    
    # Divide by the total present value of the bond to get the duration
    total_pv = sum(coupon / ((1 + y/ppy) ** t) for t in range(1, m * ppy + 1)) + pv_face
    bondDuration /= total_pv
    
    return bondDuration
