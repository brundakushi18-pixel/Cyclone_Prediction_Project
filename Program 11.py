# Program 11  –  Generating Synthetic Dataset

# This creates a new artificial dataset for 2025-10 to 2026-12 with random but realistic weather values (temperature, pressure, humidity, etc.) to simulate cyclone conditions, also it allows user to enter the date, month and year to fetch cyclone parameters of the entered date.

# 🌊 Generate realistic synthetic dataset (Oct 2025–Dec 2026)
dates = pd.date_range("2025-10-01", "2026-12-31")
np.random.seed(42)
df = pd.DataFrame({
    'Date': dates.day, 'Month': dates.month, 'Year': dates.year,
    'SeaTemp': np.random.uniform(26, 32, len(dates)),
    'Pressure': np.random.uniform(980, 1015, len(dates)),
    'Humidity': np.random.uniform(60, 95, len(dates)),
    'WindShear': np.random.uniform(5, 25, len(dates)),
    'Vorticity': np.random.uniform(-1.5, 1.5, len(dates)),
    'OceanDepth': np.random.uniform(10, 100, len(dates)),
    'CoastProximity': np.random.uniform(0, 1, len(dates)),
    'Disturbances': np.random.randint(0, 2, len(dates))
})
df['Cyclone'] = ((df.SeaTemp>29)&(df.Pressure<995)&(df.Humidity>85)&(df.WindShear<15)).astype(int)

# 🌪 Train model
X, y = df.drop('Cyclone', axis=1), df['Cyclone']
X = pd.get_dummies(X, drop_first=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42).fit(Xtr, ytr)

# 📅 Predict for a given date
try:
    d, m, y = map(int, [input("Date: "), input("Month: "), input("Year: ")])
    sel = df[(df.Year==y)&(df.Month==m)&(df.Date==d)]
    if not sel.empty:
        print(f"\n🌪 Cyclone parameters for {d:02d}-{m:02d}-{y}:\n"); display(sel)
        s = pd.get_dummies(sel.drop('Cyclone', axis=1), drop_first=True).reindex(columns=X.columns, fill_value=0)
        pred, prob = model.predict(s), model.predict_proba(s)[:,1]
        print(f"\n🔹 Prediction (0=No,1=Yes): {pred.tolist()}")
        print(f"🔹 Probability of Cyclone: {np.round(prob*100,2)}%")
    else: print("⚠️ No data found for that date.")
except: print("⚠️ Enter valid numeric Date, Month, and Year.")

