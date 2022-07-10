from pydantic import BaseModel, Field

class Payload(BaseModel):
    case_num: int
    patient_history: str