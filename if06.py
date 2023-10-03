def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    m=n%10
    k=0
    if n//10%10>m:
        m=n//10%10
        k=1
    elif n//100%10>m:
        m=n//100%10
        k=2
    elif n//1000%10>m:
        m=n//1000%10
        k=3
    elif n//10000%10>m:
        m=n//10000%10
        k=4
    elif n//100000%10>m:
        m=n//100000%10
        k=5
    return k
print(main(94856))