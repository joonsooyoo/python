from math import pi

def list_of_range_num(num):

    es = ''

    for item in list(range(1, num+1)):

        str_item = str(item)
        es = es + str_item + ' '

    return es.split()

# asks user how many digits he/she wants to see
print("You can only see 15 digits of PI")

while True:

    pi_digit = input("For a number PI, how many decimal points do you want to see? ")

    # input should be positive integer bounded by 15
    if pi_digit in list_of_range_num(15):

        break;

    else:
        print("input should be positive integer bounded by 15")

pi_digit = int(pi_digit)

# this will return the result
print("Result is {}".format(round(pi * (10 ** pi_digit)) / 10 ** pi_digit))

