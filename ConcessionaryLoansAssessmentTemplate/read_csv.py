"""
Example of reading CSV output from the extract_tables.py script
and converting it into a dictionary using pandas.
"""


import pandas as pd

CSV_FILE = "output/ProjectDetails.csv"


def assemble_dict_from_csv(csv_path, key_column="Field"):
    """
    Reads a CSV file and returns a dictionary where each
    key is taken from the specified key_column (ignoring
    rows with NaN in that column) and each value is a
    dictionary of the remaining columns (with NaN values
    omitted).

    Parameters:
        csv_path (str): Path to the CSV file.
        key_column (str): The column name to use as keys
        in the output dictionary.

    Returns:
        dict: A dictionary with keys from `key_column`
        and values as dictionaries of the other columns.
    """
    # Read the CSV file into a DataFrame.
    df = pd.read_csv(csv_path)

    # Check that the key_column exists
    if key_column not in df.columns:
        raise ValueError(
            f"Key column '{key_column}' not found in CSV columns: {list(df.columns)}"
        )

    result = {}

    # Iterate over each row in the DataFrame.
    for _, row in df.iterrows():
        key_value = row[key_column]
        # Skip rows where the key is NaN.
        if pd.isna(key_value):
            continue

        # Build a dictionary for this row with the remaining columns,
        # skipping any NaN values.
        row_dict = {}
        for col in df.columns:
            if col == key_column:
                continue
            value = row[col]
            if pd.notna(value):
                row_dict[col] = value

        result[key_value] = row_dict

    return result


# Example usage:
if __name__ == "__main__":
    project_details = assemble_dict_from_csv(CSV_FILE)
    print(project_details)
