def power4(number):
    if number <= 0:
        return False
    # keep dividibng the number by 4 while its divisible
    while number % 4 == 0:
        number = number // 4
    return number == 1
    
n = int(input("enter a number:"))
if power4(n):
    print("\nThe number is divisible by 4")
else:
    print("\nThe number is not divisible by 4")

    