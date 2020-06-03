def karatsuba(num1, num2):
    num1Str = str(num1)
    num2Str = str(num2)
    if (num1 < 10) or (num2 < 10):
        return num1 * num2

    maxLength = max(len(num1Str), len(num2Str))
    idx = maxLength // 2
    [high1, low1] = [int(num1Str[:-idx]), int(num1Str[-idx:])]
    [high2, low2] = [int(num2Str[:-idx]), int(num2Str[-idx:])]
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2 * 10 ** (2 * idx)) + ((z1 - z2 - z0) * 10 ** (idx)) + z0


def main():
    number1 = 3141592653589793238462643383279502884197169399375105820974944592
    number2 = 2718281828459045235360287471352662497757247093699959574966967627
    print(karatsuba(number1, number2))


if __name__ == '__main__':
    main()
