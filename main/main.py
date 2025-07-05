import os
import sys
from sklearn.model_selection import train_test_split

# Get the directory where main.py is located (App directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory (NEW PROJECT directory)
parent_dir = os.path.dirname(script_dir)
# Add the parent directory to Python path so we can import from backend
sys.path.insert(0, parent_dir)

# Now import your modules
try:
    from backend.preprocess import load_and_preprocess_data
    from backend.model import train_random_forest
    from backend.evaluate import evaluate_model
except ImportError as e:
    print(f"Import error: {e}")
    print("Current working directory:", os.getcwd())
    print("Python path:", sys.path)
    print("Parent directory:", parent_dir)
    print("Files in parent directory:", os.listdir(parent_dir) if os.path.exists(parent_dir) else "parent directory not found")
    print("Files in current directory:", os.listdir('.'))
    print("Backend directory exists in parent:", os.path.exists(os.path.join(parent_dir, 'backend')))
    if os.path.exists(os.path.join(parent_dir, 'backend')):
        print("Files in backend:", os.listdir(os.path.join(parent_dir, 'backend')))
    sys.exit(1)

# Ensure the model directory exists
os.makedirs("models", exist_ok=True)

# Step 1: Load and preprocess data
X, y, scaler, label_encoders = load_and_preprocess_data("Data/autism_screening.csv")

# Step 2: Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train model
model = train_random_forest(X_train, y_train)

# Step 4: Evaluate model
evaluate_model(model, X_test, y_test)