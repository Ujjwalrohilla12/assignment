import pandas as pd

def load_and_validate_excel(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Handling missing values by filling them with 'Unknown'
    df.fillna("Unknown", inplace=True)
    
    # Example: Ensure correct data types (e.g., converting a column to float)
    if 'price' in df.columns:
        df['price'] = df['price'].astype(float)

    # Implement data validation
    if 'price' in df.columns and (df['price'] < 0).any():
        raise ValueError("Negative values found in the 'price' column!")

    # Return the validated dataframe
    return df

# Example usage
if __name__ == "__main__":
    file_path = "test_data.xlsx"
    try:
        df = load_and_validate_excel(file_path)
        print("Data read and validated successfully!")
        print(df.head())  # Display the first few rows of the dataframe
    except Exception as e:
        print(f"Error: {e}")
