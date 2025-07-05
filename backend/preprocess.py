import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df.dropna(inplace=True)

    # Select only the 9 features you use in the app
    selected_cols = [
        'age', 'gender', 'jundice', 'austim',
        'A1_Score', 'A2_Score', 'A3_Score', 'A4_Score', 'A5_Score'
    ]
    # Map your app's questions to the correct columns in your CSV

    # Encode categorical columns as needed
    df['gender'] = df['gender'].map({'m': 1, 'f': 0})
    df['jundice'] = df['jundice'].map({'yes': 1, 'no': 0})
    df['austim'] = df['austim'].map({'yes': 1, 'no': 0})

    X = df[selected_cols]
    y = df['Class/ASD'].map({'YES': 1, 'NO': 0})

    return X, y, None, None
