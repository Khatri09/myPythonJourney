def computepay(h, r):
    if h <= 40:
        gross = h*r
        return gross
    elif h > 40:
        gross = 40*r +((h-40)*1.5*r)
        return gross

hrs = input("Enter Hours:")
rph = input("Enter Rate per Hour:")
h = float(hrs)
r = float(rph)

#try:
#    h = float(hrs)
#    r = float(rph)
#except:
#    print("Invalid entry! Please enter a numeric value"


p = computepay(h,r)
print("Pay", p)
