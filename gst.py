def gst(v):
    return v*0.05
    
def qst(v):
    return gst(v)*0.085

def calc_c(amount):
    g= gst(amount)
    q= qst(amount + g)
    total=amount+g+q
    print amount
    print g
    print q
    print total
    
