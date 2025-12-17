<<<<<<< HEAD
# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report
from features import extract_features  # your custom feature functions

# 1. Load dataset
data = pd.read_csv("datasets.csv")  # your CSV file
print("Dataset loaded successfully!")
print(data.head())

# 2. Extract features
X = data['url'].apply(lambda url: extract_features(url))
X = list(X)  # convert Series of lists to list of lists

# Convert labels to 0 (benign) and 1 (phishing)
y = data['label'].map(lambda x: 1 if x.lower()=='phishing' else 0)

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate model
y_pred = model.predict(X_test)
print("Training complete!")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 6. Model is in memory for predict.py or app.py
=======
# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report
from features import extract_features  # your custom feature functions

# 1. Load dataset
data = pd.read_csv("datasets.csv")  # your CSV file
print("Dataset loaded successfully!")
print(data.head())

# 2. Extract features
X = data['url'].apply(lambda url: extract_features(url))
X = list(X)  # convert Series of lists to list of lists

# Convert labels to 0 (benign) and 1 (phishing)
y = data['label'].map(lambda x: 1 if x.lower()=='phishing' else 0)

# 3. Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate model
y_pred = model.predict(X_test)
print("Training complete!")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# 6. Model is in memory for predict.py or app.py
>>>>>>> 6be99264d218af05c6ed951ba699d97a6e295199
