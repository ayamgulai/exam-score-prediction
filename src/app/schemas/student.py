from pydantic import BaseModel

class StudentInput(BaseModel):
    study_hours: float
    class_attendance: float
    sleep_hours: float
    sleep_quality: str
    study_method: str
    facility_rating: str