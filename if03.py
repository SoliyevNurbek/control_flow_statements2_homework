def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if (a-b>0 or b-a>0) and (a<c<b or a>c>b):
        return c
    if (c-b>0 or b-c>0) and (c<a<b or b>a>c):
        return a
    else :
        return b
print(main(140,80,25))