def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.find('*'):
        return s.index('*')
    else:
        return False
print(main('ds*jd'))