def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    a = len(s)
    if a > n:
        return s[n]
    else:
        return False
print(main('coder', 5))