score = input("Enter Score: ")
s = float(score)
try:
    if s >= 0.9:
        print('A')
    elif s >= 0.8:
        print('B')
    elif s >= 0.7:
        print('C')
    elif s >= 0.6:
        print('D')
    elif s < 0.6:
        print('F')
except:
    print('Input is out of range. Please enter an input between 0.0 and 1.0')
