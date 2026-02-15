# pylint: disable=invalid-name
# The module is named computeSales (camelCase) as required by Req 4.
"""
computeSales.py

Reads a product catalogue and a sales record (both JSON files),
then computes and prints the total cost of all sales.
"""

import json
import sys
import time


def load_json(path):
    """Open a JSON file and return the parsed data."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: file '{path}' not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: '{path}' is not valid JSON – {e}",
              file=sys.stderr)
        sys.exit(1)


def build_price_map(products):
    """Turn the product list into a {title: price} dictionary."""
    prices = {}
    for i, item in enumerate(products):
        try:
            prices[item["title"]] = float(item["price"])
        except (KeyError, TypeError, ValueError) as e:
            print(f"Warning: bad product at index {i} ({e}), skipped.",
                  file=sys.stderr)
    return prices


def compute_total(prices, sales):
    """Walk through every sale, look up the price and accumulate."""
    total = 0.0

    for i, sale in enumerate(sales):
        # Try to read the product name and quantity
        try:
            name = sale["Product"]
            qty = int(sale["Quantity"])
        except (KeyError, TypeError, ValueError) as e:
            print(f"Warning: bad sale at index {i} ({e}), skipped.",
                  file=sys.stderr)
            continue

        # Check that the product actually exists in the catalogue
        if name not in prices:
            print(f"Warning: '{name}' not in catalogue "
                  f"(sale index {i}), skipped.",
                  file=sys.stderr)
            continue

        total += prices[name] * qty

    return round(total, 2)


def save_and_print(total, elapsed):
    """Show the results on screen and write them to SalesResults.txt."""
    report = (
        "========================================\n"
        "         SALES RESULTS REPORT\n"
        "========================================\n"
        f"  TOTAL: ${total:,.2f}\n"
        "----------------------------------------\n"
        f"  Time elapsed: {elapsed:.6f} seconds\n"
        "========================================\n"
    )

    # Print to console
    print(report, end="")

    # Write the same thing to a file
    with open("SalesResults.txt", "w", encoding="utf-8") as f:
        f.write(report)

    print("\nResults saved to SalesResults.txt")


def main():
    """Main entry point – validates args, runs the computation."""
    if len(sys.argv) != 3:
        print("Usage: python computeSales.py "
              "priceCatalogue.json salesRecord.json",
              file=sys.stderr)
        sys.exit(1)

    catalogue_path = sys.argv[1]
    sales_path = sys.argv[2]

    start = time.time()

    # Load both JSON files
    products = load_json(catalogue_path)
    sales = load_json(sales_path)

    # Build a quick-lookup price map and compute the grand total
    prices = build_price_map(products)
    total = compute_total(prices, sales)

    elapsed = time.time() - start

    save_and_print(total, elapsed)


if __name__ == "__main__":
    main()
