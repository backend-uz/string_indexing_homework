def main(s):
    """
    A string of five numbers is given. Find the sum of its numbers.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    n1 = s%10
    s = s//10
    n2 = s%10
    s = s//10
    n3 = s%10
    s = s//10
    n4 = s%10
    s = s//10
    return n1+n2+n3+n4+s
print(main(2360))