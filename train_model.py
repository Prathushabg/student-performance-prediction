import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("📂 Loading dataset...")

# Load dataset
data = pd.read_csv("dataset/students.csv")

print("✅ Dataset Loaded Successfully!")

# ---------------- Encode Categorical Columns ---------------- #

categorical_columns = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course"
]

encoders = {}

for col in categorical_columns:
    encoder = LabelEncoder()
    data[col] = encoder.fit_transform(data[col])
    encoders[col] = encoder

# ---------------- Features & Target ---------------- #

X = data.drop("math score", axis=1)
y = data["math score"]

# ---------------- Split Dataset ---------------- #

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------- Train Model ---------------- #

print("🤖 Training Random Forest Model...")

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------- Evaluate ---------------- #

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Performance")
print("-----------------------------")
print(f"MAE : {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")

# ---------------- Save Model ---------------- #

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/student_model.pkl")
joblib.dump(encoders, "model/encoders.pkl")

print("\n✅ Model saved successfully!")
print("✅ Encoders saved successfully!")