import random
import math
import os

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def brute_force(points):
    min_val = float("inf")
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            min_val = min(min_val, dist(points[i], points[j]))
    return min_val


def strip_closest(strip, d):
    min_val = d
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_val:
                break
            min_val = min(min_val, dist(strip[i], strip[j]))

    return min_val

def closest_pair(points):
    points.sort()
    return closest_pair_rec(points)


def closest_pair_rec(points):
    if len(points) <= 3:
        return brute_force(points)

    mid = len(points) // 2
    mid_point = points[mid]

    dl = closest_pair_rec(points[:mid])
    dr = closest_pair_rec(points[mid:])
    d = min(dl, dr)

    strip = [p for p in points if abs(p[0] - mid_point[0]) < d]

    return min(d, strip_closest(strip, d))

def generate_inputs():
    os.makedirs("inputs_closest", exist_ok=True)

    for i in range(1, 11):
        n = random.randint(100, 300)
        points = [(random.randint(0, 10000), random.randint(0, 10000)) for _ in range(n)]

        with open(f"inputs_closest/closest_points_{i}.txt", "w") as f:
            for x, y in points:
                f.write(f"{x} {y}\n")

    print("Generated 10 input files for Closest Pair.\n")


def run_closest_pair():
    print("Closest Pair Results\n")

    folder = "inputs_closest"

    for file in sorted(os.listdir(folder)):
        path = os.path.join(folder, file)

        points = []
        with open(path, "r") as f:
            for line in f:
                x, y = map(int, line.split())
                points.append((x, y))

        d = closest_pair(points)
        print(f"{file} → Closest distance = {d:.4f}")

    print()


if __name__ == "__main__":
    generate_inputs()
    run_closest_pair()
    print("Completed Closest Pair Execution.")
