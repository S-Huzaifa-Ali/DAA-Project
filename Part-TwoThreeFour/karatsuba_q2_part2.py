import os
import random


def karatsuba(x, y):
    """Perform multiplication using Karatsuba's divide-and-conquer algorithm."""

    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half = n // 2

    x_high, x_low = divmod(x, 10 ** half)
    y_high, y_low = divmod(y, 10 ** half)

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba(x_low + x_high, y_low + y_high)
    z2 = karatsuba(x_high, y_high)

    return (z2 * 10 ** (2 * half)) + ((z1 - z2 - z0) * 10 ** half) + z0



def generate_inputs():
    """Generate 10 input files, each containing two large integers."""
    os.makedirs("integer_multiplication_inputs", exist_ok=True)

    for i in range(1, 11):
        digits = random.randint(100, 200)  
        x = random.randint(10**(digits - 1), 10**digits - 1)
        y = random.randint(10**(digits - 1), 10**digits - 1)

        with open(f"integer_multiplication_inputs/input_{i}.txt", "w") as f:
            f.write(f"{x}\n{y}\n")

    print("Generated 10 input files for Integer Multiplication.\n")



def run_integer_multiplication():
    """Run Karatsuba multiplication on all generated input files."""
    print("Integer Multiplication Results\n")

    folder = "integer_multiplication_inputs"

    for file in sorted(os.listdir(folder)):
        with open(os.path.join(folder, file), "r") as f:
            x, y = map(int, f.read().splitlines())

        result = karatsuba(x, y)

        print(f"{file} → Product length = {len(str(result))} digits")

    print()


if __name__ == "__main__":
    print("Integer Multiplication using Karatsuba Algorithm\n")

    generate_inputs()
    run_integer_multiplication()

    print("Completed Integer Multiplication Execution.")
