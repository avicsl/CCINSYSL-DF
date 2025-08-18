import pandas as pd

# Load the cleaned evidence data
df = pd.read_csv("cleaned_evidence.csv", parse_dates=["timestamp"])

# Feature 1: Extract hour of the day
df["hour_of_day"] = df["timestamp"].dt.hour

# Feature 2: Extract day of the week as full name (e.g., Monday, Tuesday)
df["day_of_week"] = df["timestamp"].dt.day_name()

# Feature 3: Is weekend? (Saturday or Sunday)
df["is_weekend"] = df["day_of_week"].isin(["Saturday", "Sunday"])

# Save the new DataFrame with engineered features
df.to_csv("feature_engineered_evidence.csv", index=False)

print("Feature engineering complete. Saved as 'feature_engineered_evidence.csv'.")
