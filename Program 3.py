# Program 3 – Cleaning the data

# It removes extra spaces in column names and fills missing values using column averages. Then it checks if any data is missing and renames the “Latitude” column (if present) for consistency.

import io
df = pd.read_csv(io.BytesIO(uploaded[filename]))
print("✅ Dataset loaded successfully!")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
df.head() 

