def isPrimo(num: int) -> bool:

    num = abs(num)

    if num in (0,1):
        return False
    
    for divisor in range(2, num):
        if num % divisor == 0:
            return False

    return True

def main():
    primos = []
    for i in range(1, 1001):
        if isPrimo(i):
            primos.append(i)
    print(primos)

if __name__ == "__main__":
    main()