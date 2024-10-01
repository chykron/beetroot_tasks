def sum_of_digits(digit_string: str) -> int:
    """
    Returns the sum of the digits in the input string.
    sum_of_digits('26') == 8
    True
    sum_of_digits('test')
    ValueError("input string must be digit string")
    """
    if digit_string == "":
        return 0

    if not digit_string[0].isdigit():
        raise ValueError("input string must be digit string")

    return int(digit_string[0]) + sum_of_digits(digit_string[1:])

