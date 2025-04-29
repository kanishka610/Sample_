import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1️⃣ Load the dataset
df = pd.read_csv("Obesity Classification.csv")  # Change filename accordingly

# Overview
print("\n🔍 Dataset Overview:")
print(df.info())
print("\n📊 Summary Statistics:")
print(df.describe())
print("\n❓ Missing Values:")
print(df.isnull().sum())

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 2️⃣ Data Preprocessing
df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill numeric NaNs with mean
df.fillna(df.mode().iloc[0], inplace=True)  # Fill categorical NaNs with mode

# Encode categorical columns
cat_cols = df.select_dtypes(include=['object']).columns
encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))
    encoders[col] = le

# Set your numerical target column for regression
target_column = "BMI"  # 🔁 Change this to your regression target

if target_column not in df.columns:
    print(f"❌ ERROR: Column '{target_column}' not found in dataset!")
else:
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 3️⃣ Regression Model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4️⃣ Evaluation
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"\n📈 Mean Squared Error (MSE): {mse:.2f}")
    print(f"📉 Root Mean Squared Error (RMSE): {rmse:.2f}")
    print(f"🔁 Mean Absolute Error (MAE): {mae:.2f}")
    print(f"🔢 R-squared Score: {r2:.2f}")

    # Scatter plot of predictions
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # ideal line
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Actual vs Predicted")
    plt.show()
