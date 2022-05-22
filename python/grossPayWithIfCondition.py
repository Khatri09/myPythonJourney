hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter Rate per Hour:")
r = float(rph)
if h<=40:
    gross=h*r
    print(gross)
elif h>40:
    gross=(40*r)+((h-40)*r*1.5)
    print(gross)
