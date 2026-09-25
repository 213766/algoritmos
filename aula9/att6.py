def isPrimo(num: int) -> bool:

    num = abs(num)

    if num in (0,1):
        return False
    
    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True

print(isPrimo(73))