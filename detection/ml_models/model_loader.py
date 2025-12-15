import joblib
import os
from django.conf import settings

def safe_load_model(path, model_name):
    print(f"Trying to load: {path}")
    if os.path.exists(path):
        print(f"[OK] {model_name} loaded successfully!")
        return joblib.load(path)
    else:
        print(f"[ERROR] {model_name} not found at: {path}")
        return None

# Build absolute paths
MODEL_DIR = os.path.join(settings.BASE_DIR, "detection", "ml_models")

BRDA_model_path = os.path.join(MODEL_DIR, "BRDA_model.pkl")
Liver_cancer_model_path = os.path.join(MODEL_DIR, "Liver_cancer_model.pkl")
lung_cancer_model_path = os.path.join(MODEL_DIR, "lung_cancer_model.pkl")

# Load models
breast_model = safe_load_model(BRDA_model_path, "Breast Cancer Model")
liver_model = safe_load_model(Liver_cancer_model_path, "Liver Cancer Model")
lung_model = safe_load_model(lung_cancer_model_path, "Lung Cancer Model")

print(breast_model)
print(liver_model)
print(lung_model)