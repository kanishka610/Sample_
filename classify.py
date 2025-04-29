import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score

# 1️⃣ Load and explore the dataset
df = pd.read_csv("resume_data.csv")  # Change filename accordingly

# Display basic dataset info
print("\n🔍 Dataset Overview:")
print(df.info())
print("\n📊 Summary Statistics:")
print(df.describe())
print("\n❓ Missing Values:")
print(df.isnull().sum())

# Plot correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.select_dtypes(include=['number']).corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# 2️⃣ Data Preprocessing

# Fill missing values
df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill numeric columns with mean
df.fillna(df.mode().iloc[0], inplace=True)  # Fill categorical columns with mode

# Encode categorical columns
cat_cols = df.select_dtypes(include=['object']).columns
encoders = {}  # Store label encoders for inverse transform (optional)
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col].astype(str))  # Convert to string before encoding
    encoders[col] = le

# Set the correct target column name
target_column = "skills"  # Change this to the actual target column name
if target_column not in df.columns:
    print(f"❌ ERROR: Column '{target_column}' not found in DataFrame!")
else:
    # Split dataset into features (X) and target (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Train-test split (80-20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Feature Scaling (Standardization)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # 3️⃣ Implement Classification Model (Random Forest)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 4️⃣ Evaluate Model Performance
    y_pred = model.predict(X_test)

    # Accuracy Score
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n✅ Model Accuracy: {accuracy:.2f}")

    # F1 Score
    f1 = f1_score(y_test, y_pred, average='weighted')  # Use 'macro' or 'micro' if needed
    print(f"\n🎯 F1 Score: {f1:.2f}")

    # Classification Report
    print("\n📌 Classification Report:")
    print(classification_report(y_test, y_pred))

    # Print first 10 actual and predicted labels
    print("Actual Labels:", list(y_test[:10].values))  
    print("Predicted Labels:", list(y_pred[:10]))

    # Confusion Matrix
    plt.figure(figsize=(6,4))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
    plt.title("📊 Confusion Matrix")
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.show()
