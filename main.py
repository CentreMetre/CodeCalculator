def get_length():
    valid_input = False
    code_length = 0
    while valid_input == False:
        try:
            code_length = int(input())
            valid_input = True
        except ValueError:
            print("That's not a number.")

    return code_length

def get_digits():
    valid_input = False
    digits = 0000
    while valid_input == False:
        try:
            code_length = int(input())
            valid_input = True
        except ValueError:
            print("That's not a number.")
    return code_length

def int_to_list(number):
    number = str(number)
    number_list = list(number)
    return number_list

# returns the min number and the max number
def calculate_min_max(code_length):
    #code_length_string = str(code_length)
    max = ""
    min = ""
    for i in range(0, code_length - 1):
        min = min + "9"
    max = min + "9"
    min = int(min)
    min = min + 1
    return min, max

# marked_digits is the digits that the code has, code is the current code to check
def check_code_contains_digits(marked_digits, code_to_check):
    number_str = str(code_to_check)
    number_digits_set = set(number_str)

    # Create a set of the required digits as strings
    required_digits_set = set(str(digit) for digit in marked_digits)

    # Check if the set of number's digits matches the set of required digits
    return number_digits_set == required_digits_set


def test():
    total_count = 0
    marked_digits = [3]
    for i in range(1000, 10000):
        if check_code_contains_digits(marked_digits, i):
            print(i)
            total_count += 1
    print(total_count)

test()

code_length = 0

code_digits = 0000

print("How long is the code?")
code_length = get_length()

print("What are the numbers in the code. Type only each number once.")
code_digits = get_digits()

code_digits_list = int_to_list(code_digits)

min, max = calculate_min_max(code_length)

min = int(min)
max = int(max)

total_count = 0
marked_digits = [3]
for i in range(min, max):
    if check_code_contains_digits(code_digits_list, i):
        print(i)
        total_count += 1
print(f"Total amount of codes: {total_count}")
