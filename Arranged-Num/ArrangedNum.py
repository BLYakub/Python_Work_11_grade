def algorithm():
    num_two = check_input()  # The first input goes into the variable 'num_two' as well as all of the rest of the inputs
    num = 0       # The number that will store the sorted digits
    arranged_chars = ""     # String where the chars will be sorted
    tens_count = 0      # The amount of digits that are in 'num'
    inserted_num = False    # Check if 'num_two' was inserted into 'num'
    num_zeros = 0

    # To check if 'num_two' is a digit, char, or zero and insert it into the correct variable
    if not num_two.isdigit():
        arranged_chars += num_two
    elif num_two == 0:
        num_zeros += 1
    else:
        num = int(num_two)

    temp = num

    # A loop that gets 6 inputs and arranges them in the right order
    for main_index in range(6):
        num_two = check_input()

        # If 'num_two' is a char, it goes into this function which sorts the chars into 'arranged_chars'
        if num_two.isalpha():
            arranged_chars = arrange_string(arranged_chars, num_two)
        elif num_two == '0':
            num_zeros += 1
        else:  # Else it gets added to the arranged digits operation
            num_two = int(num_two)
            tens_count += 1

            # A loop that is 'tens_count" (the amount of digits in 'num')
            for sub_index in range(tens_count):

                # if 'num_two'(input) is smaller than 'temp' digit it gets added and arranged into 'temp'
                # then breaks out of the loop
                if num_two >= (temp % 10):
                    temp, inserted_num = append_to_big_num(num, temp, num_two, sub_index)
                    break
                elif temp > 9:
                    temp = int(temp / 10)

            # If 'num_two' hasn't been inserted, it will be add to the back of 'num'
            if not inserted_num:
                num += num_two * (10 ** (sub_index + 1))
                temp = num
            else:
                num = temp

            inserted_num = False

    # A loop that prints '0' 'num_zeros' times
    for print_zero in range(num_zeros):
        print("0", end='')

    # If 'num' doesn't equal 0 it prints the arranged number
    # Then it prints the arranged chars
    if num != 0:
        print(num, end='')
    print(arranged_chars)


# A function that gets 'num', 'temp', 'num_two'(input), and 'sub_index' and returns and arranged number and a True bool
def append_to_big_num(prev_num, curr_num, num_to_add, exponent):
    return (((curr_num * 10) + num_to_add) * (10 ** exponent)) + (prev_num % (10 ** exponent)), True


# A function that gets 'arranged_chars' and 'num_two'(input) and returns an arranged string
def arrange_string(str_one, char_one):
    new_string = ""
    added_char = False
    # If the 'str_one'('arranged_chars') is empty it just adds 'char_one' and returns the string
    if str_one == "":
        new_string += char_one
        return new_string

    # A loop that goes for the amount of chars in 'str1'
    for char_two in str_one:
        if char_one <= char_two and not added_char:
            new_string += (char_one + char_two)
            added_char = True
        else:
            new_string += char_two

    # If 'add_char' == False it adds 'char1' to the end of 'new_string'
    if not added_char:
        new_string += char_one
    return new_string


# A function that gets an input, checks it, corrects it if needed, and then returns the input
def check_input():
    ask_phrase = "Enter a char or a digit from 1 - 9:"
    input_two = input(f"{ask_phrase}\n")

# While 'input_two' isn't a digit and it isn't an alphabetic string, or the length is bigger than 1,
# it asks for a re-input
    while (not input_two.isdigit()) and (not input_two.isalpha()) or len(input_two) > 1:
        input_two = input(f"Invalid input '{input_two}'! {ask_phrase}\n")

    return input_two


algorithm()
