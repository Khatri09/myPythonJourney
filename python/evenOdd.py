# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def compute_check_digit(identification_number):
    n = len(identification_number)
    even_sum = 0
    odd_sum = 0
    for i in range(n):
        if i % 2 == 0:
            even_sum = even_sum + int(identification_number[i])
        else:
            odd_sum = odd_sum + int(identification_number[i])

    # algorithm wanted to multiple even_sum by 3
    even_sum = even_sum * 3

    # algorithm wanted to add the above even_sum result to odd_sum
    odd_sum = even_sum + odd_sum

    # algorithm wanted to get the last digit from the above result. So converting integer into string.
    num_to_str = str(odd_sum)

    # calculating length of the above string because length - 1 will be our last digit.
    k = len(num_to_str)
    last_digit = int(num_to_str[k - 1])

    # algorithm wanted to subtract the last digit from 10.
    if last_digit != 0:
        result = 10 - last_digit
        print(result)
    else:
        print(last_digit)


num = input("please enter input= ")
compute_check_digit(num)
