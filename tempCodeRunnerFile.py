
def filter_negatives(matrix):
    """Filters out negative numbers (noise) from a 2D list using filter() and lambda."""
    return [list(filter(lambda x: x >= 0, row)) for row in matrix]

def transform_matrix(matrix, transform_func):
    """Applies a transformation function to all elements in a 2D list using map()."""
    return [list(map(transform_func, row)) for row in matrix]

def sort_records(records, sort_index, descending=False):
    """Sorts a list of tuples based on a custom key index using sorted() and lambda."""
    return sorted(records, key=lambda x: x[sort_index], reverse=descending)

def main():
    print("="*55)
    print(" FUNCTIONAL DATA FILTERING & TRANSFORMATION SUITE")
    print("="*55)

    raw_matrix = [
        [15, -4, 8, 21],
        [-1, 0, -8, 7],
        [44, -99, 32, -5]
    ]
    print("\n1. Original Raw Matrix (with negative noise):")
    for row in raw_matrix: print(f"   {row}")

    cleaned_matrix = filter_negatives(raw_matrix)
    print("\n   Cleaned Matrix (Negatives filtered out):")
    for row in cleaned_matrix: print(f"   {row}")


    squared_matrix = transform_matrix(cleaned_matrix, lambda x: x ** 2)
    print("\n2. Transformed Matrix (Cleaned values squared via map):")
    for row in squared_matrix: print(f"   {row}")

    data_sequences = [
        (401, 88.5, "Delta"),
        (402, 94.2, "Alpha"),
        (403, 71.8, "Gamma"),
        (404, 91.1, "Beta")
    ]
    
    print("\n3. Original Data Sequences (Tuples):")
    for record in data_sequences: print(f"   {record}")

    sorted_by_measurement = sort_records(data_sequences, sort_index=1, descending=True)
    print("\n   Sorted by Measurement (Descending using sorted & lambda):")
    for record in sorted_by_measurement: print(f"   {record}")

    sorted_by_category = sort_records(data_sequences, sort_index=2)
    print("\n   Sorted by Category Name (Alphabetical using sorted & lambda):")
    for record in sorted_by_category: print(f"   {record}")

if __name__ == "__main__":
    main()