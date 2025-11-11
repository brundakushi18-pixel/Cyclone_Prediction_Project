# Program 7 - Data Splitting for Model Training

# Here, the data is split into training and testing sets (75% train, 25% test) so that the machine-learning model can be trained and later evaluated on unseen data.

target = 'Pre_Existing_Disturbance'
 X = df.drop(columns=[target])
 y = df[target] X = pd.get_dummies(X, drop_first=True)
 X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)
 print("✅ Data split complete.")