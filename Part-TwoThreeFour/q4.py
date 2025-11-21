import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import math


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

def run_closest_pair(file_path):
    points = []
    with open(file_path, "r") as f:
        for line in f:
            x, y = map(int, line.split())
            points.append((x, y))
    d = closest_pair(points)
    return f"Closest Pair distance: {d:.4f}"


def karatsuba(x, y):
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

def run_karatsuba(file_path):
    with open(file_path, "r") as f:
        x, y = map(int, f.read().splitlines())
    result = karatsuba(x, y)
    return f"Product length: {len(str(result))} digits"


def select_file():
    global filename
    filename = filedialog.askopenfilename(title="Select a file")
    if filename:
        file_label.config(text=f"Selected File: {filename}")
        preview_file()

def preview_file():
    try:
        with open(filename, "r") as f:
            content = f.read()
        file_preview.config(state='normal')
        file_preview.delete(1.0, tk.END)
        file_preview.insert(tk.END, content)
        file_preview.config(state='disabled')
    except:
        file_preview.config(state='normal')
        file_preview.delete(1.0, tk.END)
        file_preview.insert(tk.END, "Cannot preview file")
        file_preview.config(state='disabled')

def run_algorithm1():
    if not filename:
        messagebox.showwarning("No file", "Please select a file first!")
        return
    try:
        output = run_closest_pair(filename)
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, output)
        output_text.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Closest Pair: {e}")

def run_algorithm2():
    if not filename:
        messagebox.showwarning("No file", "Please select a file first!")
        return
    try:
        output = run_karatsuba(filename)
        output_text.config(state='normal')
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, output)
        output_text.config(state='disabled')
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Karatsuba: {e}")


root = tk.Tk()
root.title("Algorithm GUI")
root.geometry("700x500")
root.resizable(False, False)

filename = None


file_frame = tk.Frame(root, bd=2, relief='groove', padx=10, pady=10)
file_frame.pack(pady=10, fill='x', padx=10)

tk.Label(file_frame, text="Step 1: Select Input File", font=("Arial", 12, "bold")).pack(anchor='w')
select_button = tk.Button(file_frame, text="Select File", command=select_file, width=20, bg="#4CAF50", fg="white")
select_button.pack(pady=5)
file_label = tk.Label(file_frame, text="No file selected")
file_label.pack(anchor='w')

tk.Label(file_frame, text="File Preview:", font=("Arial", 10, "italic")).pack(anchor='w', pady=(10,0))
file_preview = scrolledtext.ScrolledText(file_frame, height=5, width=80, state='disabled')
file_preview.pack()


algo_frame = tk.Frame(root, bd=2, relief='groove', padx=10, pady=10)
algo_frame.pack(pady=10, fill='x', padx=10)

tk.Label(algo_frame, text="Step 2: Run Algorithm", font=("Arial", 12, "bold")).pack(anchor='w')
algo1_button = tk.Button(algo_frame, text="Run Closest Pair", command=run_algorithm1, width=20, bg="#2196F3", fg="white")
algo1_button.pack(side='left', padx=10, pady=5)
algo2_button = tk.Button(algo_frame, text="Run Karatsuba Multiplication", command=run_algorithm2, width=25, bg="#FF5722", fg="white")
algo2_button.pack(side='left', padx=10, pady=5)


output_frame = tk.Frame(root, bd=2, relief='groove', padx=10, pady=10)
output_frame.pack(pady=10, fill='both', expand=True, padx=10)

tk.Label(output_frame, text="Algorithm Output:", font=("Arial", 12, "bold")).pack(anchor='w')
output_text = scrolledtext.ScrolledText(output_frame, height=10, width=80, state='disabled')
output_text.pack(fill='both', expand=True)

root.mainloop()
