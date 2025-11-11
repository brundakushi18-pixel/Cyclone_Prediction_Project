# Program 10 – Result Visualization

# It plots the actual vs predicted cyclone outcomes and a histogram showing how likely cyclones are (probability distribution).

importance = model.feature_importances_
feat_imp = pd.DataFrame({'Feature':X.columns,'Importance':importance}).sort_values(by='Importance', ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x='Importance',y='Feature',data=feat_imp,palette='viridis')
plt.title("Feature Importance in Cyclone Prediction")
plt.tight_layout();
plt.show()
print("FeatureImportance Scores:\n")
print(feat_imp)

