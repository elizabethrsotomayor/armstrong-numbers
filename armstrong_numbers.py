def is_armstrong_number(number: int):
    num_string = str(number)
    final_num = 0
    for num in num_string:
        final_num += int(num) ** len(num_string)

    return final_num == number
