def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    m=a
    if m<b:
        m=b
    if m<c:
        m=c
    elif a==b==c:
        m=a
    return m
print(main(2,8,11))