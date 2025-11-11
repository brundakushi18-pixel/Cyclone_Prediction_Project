# Program 1 – Install and import Python libraries
# This program installs and imports all the essential python libraries needed for this project - such as Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn and confirms that they've been loaded successfully for data analysis and machine learning tasks.



import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
sns.set(style="whitegrid", font_scale=1.05)
print("✅ Libraries loaded successfully!")