import joblib

MODEL_PATH = "src\model\model_LR.pkl"
COLUMNS_PATH = "src\/artifacts\/artifacts_train_columns.pkl"

model = joblib.load(MODEL_PATH)
train_columns = joblib.load(COLUMNS_PATH)

ordinal_maps = {
    "sleep_quality": {
        "poor": 0,
        "average": 1,
        "good": 2
    },
    "facility_rating": {
        "low": 0,
        "medium": 1,
        "high": 2
    },
    "study_method" : {
        "self-study" : 1,
        "online videos": 2,
        "group study" : 3,
        "mixed" : 4,
        "coaching" : 5
    }
}