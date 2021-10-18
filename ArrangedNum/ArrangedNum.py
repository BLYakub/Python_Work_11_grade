def algorithm():
    num = check_input()
    tens_count = 0
    temp = num
    main_num_changed = False

    for main_index in range(6):
        num_two = check_input()
        tens_count += 1

        for sub_index in range(tens_count):
            if num_two >= (temp % 10):
                temp = append_to_big_num(num, temp, num_two, sub_index)
                main_num_changed = True
                break
            else:
                if temp > 9:
                    temp = int(temp / 10)

                main_index = sub_index

        if not main_num_changed:
            num += num_two * (10 ** (main_index + 1))
            temp = num
        else:
            num = temp

        main_num_changed = False

    print(num)


def append_to_big_num(prev_num, curr_num, num_to_add, exponent):
    return (((curr_num * 10) + num_to_add) * (10 ** exponent)) + (prev_num % (10 ** exponent))


def check_input():
    ask_phrase = "Enter a digit from 1 - 9:"
    num_input = input(f"{ask_phrase}\n")

    while (not num_input.isdigit()) or (int(num_input) > 9) or (int(num_input) < 1):
        num_input = input(f"Invalid input '{num_input}'! {ask_phrase}\n")

    return int(num_input)


algorithm()
