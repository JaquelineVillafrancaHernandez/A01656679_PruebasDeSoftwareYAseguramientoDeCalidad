# pylint: disable=invalid-name
# Module name uses camelCase per assignment spec (Req 4).
"""Convert numbers from a file to binary and hexadecimal bases."""

import sys
import time

# Two's complement widths (10-bit binary, 40-bit hex — same as Excel)
BINARY_BITS = 10
HEX_BITS = 40


# Conversion logic — can't use bin(), hex() or format()

def int_to_binary(number):
    """Successive division by 2, negatives in two's complement."""
    if number == 0:
        return "0"

    if number < 0:
        # Widen if the value doesn't fit in the default 10-bit range
        bit_width = BINARY_BITS
        while (1 << (bit_width - 1)) < abs(number):
            bit_width += 2
        number = (1 << bit_width) + number

    digits = []
    while number > 0:
        digits.append(str(number % 2))
        number = number // 2

    digits.reverse()
    return "".join(digits)


def int_to_hex(number):
    """Successive division by 16, negatives in two's complement."""
    hex_chars = "0123456789ABCDEF"

    if number == 0:
        return "0"

    if number < 0:
        bit_width = HEX_BITS
        while (1 << (bit_width - 1)) < abs(number):
            bit_width += 8
        number = (1 << bit_width) + number

    digits = []
    while number > 0:
        digits.append(hex_chars[number % 16])
        number = number // 16

    digits.reverse()
    return "".join(digits)


# File handling

def read_items_from_file(filepath):
    """Read one token per line, skip blank lines."""
    items = []
    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            token = line.strip()
            if token:
                items.append(token)
    return items


def parse_integer(token):
    """Try casting to int; returns (value, success_flag)."""
    try:
        return int(token), True
    except ValueError:
        return token, False


# Processing

def convert_items(items):
    """Run each item through the converters.

    Bad data gets '#VALUE!' and a warning on stderr.
    """
    results = []

    for idx, token in enumerate(items, start=1):
        value, valid = parse_integer(token)

        if valid:
            bin_str = int_to_binary(value)
            hex_str = int_to_hex(value)
        else:
            print(
                f"WARNING: item {idx} has invalid data: "
                f"'{token}' - skipped conversion",
                file=sys.stderr,
            )
            bin_str = "#VALUE!"
            hex_str = "#VALUE!"

        results.append((idx, token, bin_str, hex_str))

    return results


# Output

def output_results(results, elapsed):
    """Print conversion table and save to ConvertionResults.txt."""
    output_file = "ConvertionResults.txt"
    header = "ITEM\tVALUE\tBIN\tHEX"

    with open(output_file, "w", encoding="utf-8") as file:
        print(header)
        file.write(header + "\n")

        for idx, original, bin_str, hex_str in results:
            line = f"{idx}\t{original}\t{bin_str}\t{hex_str}"
            print(line)
            file.write(line + "\n")

        # Time goes at the very end (Req 7)
        time_line = f"\nELAPSED TIME: {elapsed:.6f} seconds"
        print(time_line)
        file.write(time_line + "\n")

    print(f"\nResults saved to {output_file}")


def main():
    """Read file, convert each number, print and save results."""
    if len(sys.argv) < 2:
        print(
            "Usage: python convertNumbers.py fileWithData.txt",
            file=sys.stderr,
        )
        sys.exit(1)

    input_file = sys.argv[1]
    start = time.time()

    items = read_items_from_file(input_file)

    if not items:
        print("ERROR: no data found in the file.", file=sys.stderr)
        sys.exit(1)

    results = convert_items(items)
    elapsed = time.time() - start

    output_results(results, elapsed)


if __name__ == "__main__":
    main()
