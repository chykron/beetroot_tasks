def reverse(input_str: str) -> str:
    """
    Function returns reversed input string.
    reverse("hello") == "olleh"
    True
    reverse("o") == "o"
    True
    reverse("") == ""
    True
    """
    if input_str == "":
        return ""
    else:
        return input_str[-1] + reverse(input_str[:-1])
