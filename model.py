import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from preprocess import prepare_fastf1_data
def train_model(data_path):
    df = pd.read_csv(data_path)
    features = df[['Grid', 'ConstructorPoints', 'DriverPoints']]
    target = df['Winner'] 

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, max_depth=8, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("🧪 Classic Data Model Accuracy:", round(acc * 100, 2), "%")
    print("📊 Report:\n", classification_report(y_test, y_pred))

    return model
def train_with_fastf1(csv_path):
    X, y, driver_map = prepare_fastf1_data(csv_path)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=150, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    return model, X.columns.tolist(), driver_map

