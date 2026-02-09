# pylint: disable=invalid-name
# Module name uses camelCase per assignment spec (Req 4).
"""Compute descriptive statistics from a file of numbers."""

import sys
import time


# Square root without math library
def square_root(number):
    """Newton-Raphson square root."""
    if number < 0:
        return float('nan')
    if number == 0:
        return 0.0

    guess = number / 2.0
    for _ in range(200):
        better = (guess + number / guess) / 2.0
        if abs(better - guess) < 1e-15:
            break
        guess = better
    return guess


# Can't use built-in sort, so merge sort it is
def merge_sort(data):
    """Recursive merge sort."""
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return _merge(left, right)


def _merge(left, right):
    """Helper to merge two sorted halves."""
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Stats calculations
def compute_mean(numbers):
    """Sum all values and divide by count."""
    total = 0.0
    for n in numbers:
        total += n
    return total / len(numbers)


def compute_median(sorted_nums):
    """Middle value from sorted list."""
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 1:
        return sorted_nums[mid]
    return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2.0


def compute_mode(numbers):
    """Most repeated value, or #N/A if nothing repeats."""
    frequencies = {}
    for num in numbers:
        if num in frequencies:
            frequencies[num] += 1
        else:
            frequencies[num] = 1

    max_freq = 0
    for freq in frequencies.values():
        max_freq = max(max_freq, freq)

    if max_freq == 1:
        return "#N/A"

    # Pick the first one that matches
    for num in numbers:
        if frequencies[num] == max_freq:
            return num

    return "#N/A"


def compute_variance(numbers, mean):
    """Population variance: sum of squared diffs / N."""
    total = 0.0
    for num in numbers:
        diff = num - mean
        total += diff * diff
    return total / len(numbers)


# File handling
def read_numbers_from_file(filepath):
    """Read one number per line, skip bad data."""
    numbers = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                numbers.append(float(line))
            except ValueError:
                print(
                    f"WARNING: line {line_num} has invalid data: "
                    f"'{line}' - skipped",
                    file=sys.stderr,
                )

    return numbers


def format_value(value):
    """Drop the .0 for whole numbers."""
    if isinstance(value, str):
        return value
    if value == int(value):
        return str(int(value))
    return str(value)


def output_results(results):
    """Print to screen and save to StatisticsResults.txt."""
    output_file = "StatisticsResults.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for label, val in results.items():
            formatted = format_value(val)
            print(f"{label}: {formatted}")
            f.write(f"{label}: {formatted}\n")

    print(f"\nResults saved to {output_file}")


def main():
    """Read file, compute stats, print and save."""
    if len(sys.argv) < 2:
        print("Usage: python computeStatistics.py fileWithData.txt",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    start = time.time()

    numbers = read_numbers_from_file(input_file)

    if not numbers:
        print("ERROR: no valid numbers found in the file.",
              file=sys.stderr)
        sys.exit(1)

    sorted_nums = merge_sort(numbers)

    mean = compute_mean(numbers)
    median = compute_median(sorted_nums)
    mode = compute_mode(numbers)
    variance = compute_variance(numbers, mean)
    std_dev = square_root(variance)

    elapsed = time.time() - start

    results = {
        "COUNT": len(numbers),
        "MEAN": mean,
        "MEDIAN": median,
        "MODE": mode,
        "SD": std_dev,
        "VARIANCE": variance,
        "ELAPSED TIME": f"{elapsed:.6f} seconds",
    }

    output_results(results)


if __name__ == "__main__":
    main()
