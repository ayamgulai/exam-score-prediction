from fastapi import APIRouter
from src.app.schemas.student import StudentInput
from src.app.services.prediction import predict_exam_score, get_pass_status

router = APIRouter(prefix="/api")

@router.post("/predict")
def predict(data: StudentInput):
    score = predict_exam_score(data.dict())
    status = get_pass_status(score)
    return {
        "predicted_exam_score": score,
        "status": status
    }