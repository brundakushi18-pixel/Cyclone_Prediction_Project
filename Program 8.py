# Program 8  –  Model Building and Prediction

# A Random Forest Classifier is created to predict cyclone occurrences. It trains the model, makes predictions, calculates accuracy (~85%), and prints a detailed performance report.

model = RandomForestClassifier(
 n_estimators=400, max_depth=16,
 min_samples_split=3, min_samples_leaf=1, 
max_features='sqrt', random_state=42)
 model.fit(X_train, y_train)
 y_pred = model.predict(X_test)
 y_prob = model.predict_proba(X_test)[:,1]
 print("\n🔹 Predicted Cyclone Outcomes (0=No,1=Yes):", y_pred[:15])
 print("🔹 Predicted Probabilities:", np.round(y_prob[:10],2)) 
acc = accuracy_score(y_test, y_pred) 
print(f"\n📊 Model Accuracy: {acc*100:.2f}%")
 print("\nClassification Report:\n", classification_report(y_test,y_pred, target_names=['No Pre-Existing', 'Pre-Existing']))

