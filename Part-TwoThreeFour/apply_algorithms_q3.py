import os
import json
from closest_pair_q2_p1 import closest_pair
from karatsuba_q2_p2 import karatsuba


# APPLY CLOSEST PAIR ALGORITHM 
def run_closest_pair_tests():
    input_folder = "inputs_closest"
    output_results = []

    print("\n=== Running Closest Pair Tests ===\n")
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".txt"):
            filepath = os.path.join(input_folder, filename)

       
            points = []
            with open(filepath, "r") as f:
                for line in f:
                    x, y = map(int, line.split())
                    points.append((x, y))

            # Apply algorithm
            dist = closest_pair(points)

            print(f"{filename} -> Closest Distance = {dist:.4f}")

            output_results.append({
                "file": filename,
                "closest_distance": dist
            })

    return output_results


#  APPLY INTEGER MULTIPLICATION ALGORITHM 
def run_integer_multiplication_tests():
    input_folder = "integer_multiplication_inputs"
    output_results = []

    print("\n=== Running Integer Multiplication Tests ===\n")
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith(".txt"):
            filepath = os.path.join(input_folder, filename)

            with open(filepath, "r") as f:
                x, y = map(int, f.read().splitlines())

            # Apply Karatsuba multiplication
            result = karatsuba(x, y)

            print(f"{filename} -> {len(str(result))} digits product")

            output_results.append({
                "file": filename,
                "x_digits": len(str(x)),
                "y_digits": len(str(y)),
                "product_digits": len(str(result)),
            })

    return output_results


def save_results(cp_results, mult_results):
    os.makedirs("results", exist_ok=True)

    with open("results/closest_pair_results.json", "w") as f:
        json.dump(cp_results, f, indent=4)

    with open("results/integer_multiplication_results.json", "w") as f:
        json.dump(mult_results, f, indent=4)

    print("\nResults saved to /results folder.")


if __name__ == "__main__":
    cp_results = run_closest_pair_tests()
    mult_results = run_integer_multiplication_tests()
    save_results(cp_results, mult_results)
