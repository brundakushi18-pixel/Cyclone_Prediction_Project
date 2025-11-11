# Program 5 – Summary statistics

# Here the cyclone parameters of the first five rows are displayed as reference for summarizing statistics in the uploaded Datasets.


if 'Cyclone_Formation' in df.columns:
    print("\nCyclone distribution (0=No, 1=Yes):")
    print(df['Cyclone_Formation'].value_counts())
    print("\nSummary statistics:\n", df.describe())
