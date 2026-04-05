#generate_synthetic_data.py
# Import pandas to create and manipulate tabular data
# pandas is a popular data analysis library (must be installed via pip)
import pandas as pd  # Used for DataFrame creation and CSV export

# Import numpy to generate random numeric values
# numpy is a scientific computing library (must be installed via pip)
import numpy as np  # Used for random number generation

# Import pathlib to handle file paths safely
from pathlib import Path  # Standard library module for filesystem paths


# Define a function to generate synthetic credit application data
def generate_synthetic_data(num_records: int = 50):
    # Create a dictionary where each key is a column name and each value is a list of generated values

    data = {
        # Generate random credit scores between 500 and 800
        "credit_score": np.random.randint(500, 800, num_records),

        # Generate random income values between 40k and 150k
        "income": np.random.randint(40000, 150000, num_records),

        # Generate random utilization percentages between 0% and 100%
        "utilization": np.random.randint(0, 100, num_records),

        # Generate random delinquency flags (True/False)
        "delinquency_flag": np.random.choice([True, False], num_records),

        # Generate random requested amounts between 1k and 20k
        "requested_amount": np.random.randint(1000, 20000, num_records),
    }

    # Convert the dictionary into a pandas DataFrame
    df = pd.DataFrame(data)

    # Build the output path using Path for OS-independent behavior
    output_path = Path("data/synthetic/synthetic_data.csv")

    # Ensure the parent directory exists (create if missing)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the DataFrame to a CSV file without the index column
    df.to_csv(output_path, index=False)

    # Print a confirmation message to the console
    print(f"Synthetic data generated and saved to: {output_path}")


# Run the generator when this script is executed directly
if __name__ == "__main__":
    # Call the function with default 50 records
    generate_synthetic_data()
