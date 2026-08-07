import pandas as pd
import os

file_path = "test_csv.csv"

if not os.path.isfile(file_path):
    raise FileNotFoundError(f"File not found: {file_path}")

try:
    # Read CSV with common useful options
    df = pd.read_csv(
        file_path,
        encoding="utf-8",     # Change if your file uses another encoding (e.g., "shift_jis")
        sep=",",              # Delimiter (default is comma)
        header=0,             # First row as column names
        na_values=["", "NA"], # Treat empty strings and "NA" as NaN
    )

except pd.errors.EmptyDataError:
    raise ValueError("The CSV file is empty.")
except pd.errors.ParserError as e:
    raise ValueError(f"Error parsing CSV: {e}")
except UnicodeDecodeError:
    raise ValueError("Encoding error. Try changing the 'encoding' parameter.")

df.to_html("./test_to_html.html")