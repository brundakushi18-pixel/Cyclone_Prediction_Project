# Program 2 – Uploading the Dataset

# This program uploads your cyclone dataset file into Google Colab and loads it into a pandas DataFrame. It shows the shape (rows × columns) and lists all column names to confirm successful upload.



from google.colab import files, drive
uploaded = files.upload()
filename = list(uploaded.keys())[0]
print(f"✅ '{filename}' uploaded successfully!")
