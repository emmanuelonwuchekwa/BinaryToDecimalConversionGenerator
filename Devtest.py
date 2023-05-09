import random

def generate_random_binary():
    binary_digits = [str(random.randint(0, 1)) for _ in range(4)]
    binary_number = ''.join(binary_digits)
    return binary_number

def convert_to_decimal(binary_number):
    decimal_number = 0
    power = 0
    for digit in binary_number[::-1]:
        decimal_number += int(digit) * (2 ** power)
        power += 1
    return decimal_number

def main():
    random_binary = generate_random_binary()
    decimal = convert_to_decimal(random_binary)
    print(f"Random binary number: {random_binary}")
    print(f"Decimal equivalent: {decimal}")

if __name__ == "__main__":
    main()
