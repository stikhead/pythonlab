import pandas as pd
import os

def process_dataset(input_filepath, output_filepath, filter_col, filter_threshold):
    """
    Analyzes a CSV/TSV dataset, inspects its structure, filters rows based on a 
    numerical condition, and exports the result.
    """
    print(f"--- Analyzing Dataset: {input_filepath} ---")
    
    try:
        separator = '\t' if input_filepath.endswith('.tsv') else ','
        df = pd.read_csv(input_filepath, sep=separator)
        
        rows, cols = df.shape
        print(f"\n[+] Structural Dimensions:")
        print(f"    Total Rows: {rows}")
        print(f"    Total Columns: {cols}")
        
        print(f"\n[+] Data Types Summary:")
        print(df.dtypes)
        
        if filter_col in df.columns:
            filtered_df = df[df[filter_col] > filter_threshold]
            filtered_rows = filtered_df.shape[0]
            print(f"\n[+] Filtering Data:")
            print(f"    Condition: '{filter_col}' > {filter_threshold}")
            print(f"    Rows retained after filtering: {filtered_rows} (Dropped {rows - filtered_rows})")
            
            filtered_df.to_csv(output_filepath, index=False)
            print(f"\n[+] Success: Cleaned dataset exported to '{output_filepath}'")
        else:
            print(f"\n[!] Error: Column '{filter_col}' not found in the dataset.")
            
    except FileNotFoundError:
        print(f"\n[!] Error: The file '{input_filepath}' was not found.")
    except Exception as e:
        print(f"\n[!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    sample_input = "sample_data.csv"
    sample_output = "cleaned_data.csv"
    
    if not os.path.exists(sample_input):
        dummy_data = pd.DataFrame({
            'ID': [1, 2, 3, 4, 5],
            'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
            'Score': [85, 92, 45, 78, 60]
        })
        dummy_data.to_csv(sample_input, index=False)
        print(f"Created sample dataset: {sample_input}\n")

    process_dataset(
        input_filepath=sample_input, 
        output_filepath=sample_output, 
        filter_col='Score', 
        filter_threshold=70
    )