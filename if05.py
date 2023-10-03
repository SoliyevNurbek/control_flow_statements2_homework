def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    m=n%10
    if n//10%10>m:
        m=n//10%10
    elif n//100%10>m:
        m=n//100%10
    elif n//1000%10>m:
        m=n//1000%10
    elif n//10000%10>m:
        m=n//10000%10
    elif n//100000%10>m:
        m=n//100000%10
    return m
print(main(84956))