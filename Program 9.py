# Program 9 – Confusion Matrix

# This visualizes how many predictions were correct or incorrect (Yes/No cyclones) using a blue-shaded confusion-matrix plot.

cm = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm, display_labels=['0(No)','1(Yes)']).plot(cmap='Blues')
plt.title("Confusion Matrix – Cyclone Prediction")
plt.show()
plt.figure(figsize=(3,2))
plt.scatter(range(len(y_test)), y_test, label='Actual', color='green', alpha=0.6)
plt.scatter(range(len(y_pred)), y_pred, label='Predicted', color='orange', alpha=0.6)
plt.yticks([0,1],['0(No)','1(Yes)'])
plt.legend(); plt.grid(True)
plt.title("Actual vs Predicted Cyclone Occurrence")
plt.show()
plt.hist(y_prob,bins=12,color='skyblue',edgecolor='black')
plt.title("Cyclone Probability Distribution")
plt.xlabel("Probability of Cyclone Next Month"); plt.ylabel("Frequency")
plt.grid(True); plt.show()

