import pandas as pd

def predict_lung(model, features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    proba = model.predict_proba(df)

    return {
        "probability": round(proba[0][1] * 100, 2),
        "diagnosis": "Cancer" if prediction[0] == 1 else "No Cancer",
        "class": int(prediction[0]),
    }


def predict_breast(model, features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    proba = model.predict_proba(df)

    return {
        "probability": round(proba[0][1] * 100, 2),
        "diagnosis": "Cancer" if prediction[0] == 1 else "No Cancer",
        "class": int(prediction[0]),
    }


def predict_liver(model, features):
    df = pd.DataFrame([features])
    prediction = model.predict(df)
    proba = model.predict_proba(df)

    return {
        "probability": round(proba[0][1] * 100, 2),
        "diagnosis": "Cancer" if prediction[0] == 1 else "No Cancer",
        "class": int(prediction[0]),
    }