import pandas as pd
import numpy as np
from src.app.config.config import model, train_columns, ordinal_maps

def predict_exam_score(input_data: dict) -> float:
    df = pd.DataFrame([input_data])

    for col, mapping in ordinal_maps.items():
        df[col] = df[col].map(mapping)

    df = pd.get_dummies(
        df,
        columns=["study_method"],
        drop_first=True
    )

    df = df.reindex(columns=train_columns, fill_value=0)

    prediction = model.predict(df)[0]
    prediction = np.clip(prediction, 0, 100)

    return round(float(prediction), 2)

def get_pass_status(score: float) -> str:
    return "Pass" if score >= 70 else "Fail"