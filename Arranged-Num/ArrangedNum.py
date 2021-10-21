def algorithm():
    num_two = check_input()  # The first input goes into the variable 'num_two' as well as all of the rest of the inputs
    num = int(0)        # 'num' is the number that will get the sorted digits
    arranged_chars = ""     # 'arranged_chars' is the string where the chars will be sorted
    tens_count = 0      # 'tens_count' the amount of digits that are in 'num'
    inserted_num = False    # 'inserted_num' bool to check if 'num_two' was inserted into 'num'
    num_zeros = 0       # 'num_zeros' the amount of zeros inputted

    if not num_two.isdigit():  # To check if 'num_two' is a digit, char, or zero and insert it into the correct variable
        arranged_chars += num_two
    elif num_two == 0:
        num_zeros += 1
    else:
        num = int(num_two)

    temp = num

    for main_index in range(6):  # A loop that gets 6 inputs and arranges them in the right order
        num_two = check_input()

        if num_two.isalpha():  # If 'num_two' is a char, it goes into this function which sorts the chars into 'arranged_chaes'
            arranged_chars = arrange_string(arranged_chars, num_two)
        elif num_two == '0':  # Else if it is zero, 'num_zeros' adds 1
            num_zeros += 1
        else:  # Else it gets added to the arranged digits operation
            num_two = int(num_two)
            tens_count += 1

            for sub_index in range(tens_count):  # A loop that is 'tens_count" (the amount of digits in 'num')
                if num_two >= (temp % 10):  # if 'num_two'(input) is smaller than 'temp' digit it gets added and arranged into 'temp'
                    temp, inserted_num = append_to_big_num(num, temp, num_two, sub_index)  # Returns an arranged number and a true bool
                    break  # breaks out of the loop
                elif temp > 9:  # Else if 'temp' is bigger than 9, temp gets divided by 10
                    temp = int(temp / 10)

            if not inserted_num:  # If 'inserted_num' == False 'num_two'(input) will be add to the back of num
                num += num_two * (10 ** (sub_index + 1))
                temp = num
            else:
                num = temp

            inserted_num = False

    for print_zero in range(num_zeros):  # A loop that prints '0' 'num_zeros' times
        print("0", end='')
    if num != 0: # If 'num' doesn't equal 0 it prints the arranged number
        print(num, end='')
    print(arranged_chars)  # Then it prints the arranged chars


# A function that gets 'num', 'temp', 'num_two'(input), and 'sub_index' and returns and arranged number and a True bool
def append_to_big_num(prev_num, curr_num, num_to_add, exponent):
    return (((curr_num * 10) + num_to_add) * (10 ** exponent)) + (prev_num % (10 ** exponent)), True


# A function that gets 'arranged_chars' and 'num_two'(input) and returns an arranged string
def arrange_string(str1, char1):
    new_string = ""
    add_char = False
    if str1 == "":  # If the 'str1'('arranged_chars') is empty it just adds 'char1' and returns the string
        new_string += char1
        return new_string

    for char2 in str1:  # A loop that goes for the amount of chars in 'str1'
        if char1 <= char2 and not add_char:  # If 'char1' is smaller than 'char2' it adds 'char1' before 'char2'
            new_string += (char1 + char2)
            add_char = True
        else:  # Else it just adds 'char2'
            new_string += char2

    if not add_char:  # If 'add_char' == False it adds 'char1' to the end of 'new_string'
        new_string += char1
    return new_string


# A function that gets an input, checks it, corrects it if needed, and then returns the input
def check_input():
    ask_phrase = "Enter a char or a digit from 1 - 9:"
    input2 = input(f"{ask_phrase}\n")

# While 'input2' isn't a digit and it isn't an alphabetic string, or the length is bigger than 1, it asks for a re-input
    while (not input2.isdigit()) and (not input2.isalpha()) or len(input2) > 1:
        input2 = input(f"Invalid input '{input2}'! {ask_phrase}\n")

    return input2


algorithm()
