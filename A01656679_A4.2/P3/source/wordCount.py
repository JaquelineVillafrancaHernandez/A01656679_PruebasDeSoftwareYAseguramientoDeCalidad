# pylint: disable=invalid-name
# Module name uses camelCase per assignment spec (Req 4).
"""Count distinct words and their frequency from a text file."""

import sys
import time


# Can't use built-in sort, so merge sort it is
def merge_sort(pairs):
    """Recursive merge sort for (word, count) tuples."""
    if len(pairs) <= 1:
        return pairs

    mid = len(pairs) // 2
    left = merge_sort(pairs[:mid])
    right = merge_sort(pairs[mid:])
    return _merge(left, right)


def _merge(left, right):
    """Merge two sorted halves by (-count, word)."""
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        left_key = (-left[i][1], left[i][0])
        right_key = (-right[j][1], right[j][0])

        if left_key <= right_key:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Word counting
def count_words(filepath):
    """Read words from file, return frequencies dict and total count."""
    frequencies = {}
    total = 0

    with open(filepath, "r", encoding="utf-8") as f:
        for line_num, raw_line in enumerate(f, start=1):
            stripped = raw_line.strip()

            if not stripped:
                print(
                    f"WARNING: line {line_num} is empty - skipped",
                    file=sys.stderr,
                )
                continue

            tokens = stripped.split()
            for word in tokens:
                total += 1
                if word in frequencies:
                    frequencies[word] += 1
                else:
                    frequencies[word] = 1

    return frequencies, total


# Output
def output_results(sorted_pairs, total, elapsed):
    """Print to screen and save to WordCountResults.txt."""
    output_file = "WordCountResults.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        for word, count in sorted_pairs:
            line = f"{word}\t{count}"
            print(line)
            f.write(line + "\n")

        total_line = f"Grand Total\t{total}"
        print(total_line)
        f.write(total_line + "\n")

        time_line = f"ELAPSED TIME\t{elapsed:.6f} seconds"
        print(time_line)
        f.write(time_line + "\n")

    print(f"\nResults saved to {output_file}")


def main():
    """Read file, count words, print and save."""
    if len(sys.argv) < 2:
        print("Usage: python wordCount.py fileWithData.txt",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    start = time.time()

    frequencies, total = count_words(input_file)

    if not frequencies:
        print("ERROR: no valid words found in the file.",
              file=sys.stderr)
        sys.exit(1)

    # Sort by frequency desc, then alphabetically
    pairs = []
    for word, count in frequencies.items():
        pairs.append((word, count))
    sorted_pairs = merge_sort(pairs)

    elapsed = time.time() - start

    output_results(sorted_pairs, total, elapsed)


if __name__ == "__main__":
    main()
