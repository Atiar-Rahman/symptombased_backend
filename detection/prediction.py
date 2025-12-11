import pandas as pd
from detection.ml_models.model_loader import breast_model, lung_model, liver_model


print("Breast model:", breast_model)
print("Liver model:", liver_model)
print("Lung model:", lung_model)

def predict_lung(model, features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    proba = model.predict_proba(df)

    return {
        "cancer_probability": round(proba[0][1] * 100, 2),
        "final_diagnosis": "Cirrhosis (Cancer)" if prediction[0] == 1 else "No Cirrhosis (No Cancer)",
        "prediction_class": int(prediction[0]),
    }


def predict_liver(model, features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    proba = model.predict_proba(df)

    return {
        "cancer_probability": round(proba[0][1] * 100, 2),
        "final_diagnosis": "Cancer Detected (High Risk)" if prediction[0] == 1 else "No Cancer Detected (Low Risk)",
        "prediction_class": int(prediction[0]),
    }


def predict_breast(model, features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    proba = model.predict_proba(df)

    return {
        "cancer_probability": round(proba[0][1] * 100, 2),
        "final_diagnosis": "Cancer Detected (High Risk)" if prediction[0] == 1 else "No Cancer Detected (Low Risk)",
        "prediction_class": int(prediction[0]),
    }
