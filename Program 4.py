# Program 4 – Data Summary

# This prints the number of cyclone and non-cyclone cases and displays key statistical values (like mean, min, max) for all features to understand the dataset’s distribution.

df.columns = df.columns.str.strip()
 df.fillna(df.mean(numeric_only=True), inplace=True)
 if 'Latitude' in df.columns:
    df.rename(columns={'Latitude':'LAT'}, inplace=True)
 print("Cleaned columns:", df.columns.tolist()
) print("Missing values:\n", df.isna().sum().head(5))
