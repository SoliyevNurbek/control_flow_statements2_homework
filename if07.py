def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Use the elif statments.
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"
    Args:
        temp: Temperature in Celsius.
    Returns:
        str: return answer.
    """
    if temp<0:
        return "Freezing"
    elif temp>0 and temp<11 :
        return "Very Cold"
    elif temp>10 and temp<21 :
        return "Cold"
    elif temp>20 and temp<31 :
        return "Normal"
    elif temp>30 and temp<41 :
        return "Hot"
    elif temp>40 :
        return "Very Hot"
print(main(124))